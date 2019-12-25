'''
    This file is part of the HeavenMS MapleStory Server
    Copyleft (L) 2016 - 2018 RonanLana

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation version 3 as published by
    the Free Software Foundation. You may not use, modify or distribute
    this program under any other version of the GNU Affero General Public
    License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys

import json
import requests
import os
from datetime import datetime
import errno
import shutil
import time
import traceback

from authorscanner import AuthorScanRepository
from authorscanner.patrons import AuthorPatronManager


matchcustomDir = '../../lib/matchprofile_custom/'
matchdefaultDir = '../../lib/matchprofile_default/'


def loadAuthToken():
    file = open("C:/Nexon/auth.txt", 'r')
    tokens = file.read().splitlines()
    return tokens


def getRequestCall(nextLink, apiParams):
    while True:
        try:
            reqGet = requests.get(nextLink, headers=apiParams)

            if 'X-RateLimit-Remaining' in reqGet.headers and int(reqGet.headers['X-RateLimit-Remaining']) < 1:
                print('RateLimit exceeded for this hour...')

                time.sleep(max(20,float(reqGet.headers['X-RateLimit-Reset']) - float(datetime.utcnow().timestamp())))
                continue

            return reqGet
        except requests.exceptions.ConnectionError or ConnectionRefusedError:
            print('Connection lost. Retrying...')
            time.sleep(20)


def getRequest(nextLink, apiParams):
    global reqGet

    reqGet = getRequestCall(nextLink, apiParams)
    return reqGet


def postRequestCall(nextLink, nextLinkData, apiParams):
    while True:
        try:
            reqGet = requests.post(nextLink, data=nextLinkData, headers=apiParams)

            if 'X-RateLimit-Remaining' in reqGet.headers and int(reqGet.headers['X-RateLimit-Remaining']) < 1:
                print('RateLimit exceeded for this hour...')

                time.sleep(max(20,float(reqGet.headers['X-RateLimit-Reset']) - float(datetime.utcnow().timestamp())))
                continue

            return reqGet
        except requests.exceptions.ConnectionError or ConnectionRefusedError:
            print('Connection lost. Retrying...')
            time.sleep(20)


def postRequest(nextLink, nextLinkData, apiParams):
    global reqGet

    reqGet = postRequestCall(nextLink, nextLinkData, apiParams)
    return reqGet


def isCountryType(addressTypes):
    for addressType in addressTypes:
        if addressType.lower() == 'country':
            return True

    return False


def locateUserCountry(getResult):
    for addressInfo in getResult['address_components']:
        if isCountryType(addressInfo['types']):
            return [addressInfo['long_name'], addressInfo['short_name']]

    return None


def locateUser(user, apiParams):
    userLocations = user['location']
    if userLocations is not None:
        userLocation = userLocations.replace(' ', '+')

        nextLink = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + userLocation + '&key=' + apiParams['key']
        r = getRequest(nextLink, apiParams)

        # extracting data in json format
        data = r.json()

        dataRes = data['results']
        if len(dataRes) > 0:
            for geoResult in dataRes:
                userCountry = locateUserCountry(geoResult)

                if userCountry is not None:
                    return userCountry

    return None


def userCountryMessage(country):
    if country is not None:
        return country[0] + ' (' + country[1] + ')'
    else:
        return None


def userPatronName(user):
    name = user['name']
    if name is not None:
        patron_name = patronManager.processPatronName(name)
    else:
        patron_name = None

    return patron_name


def isDefaultImage(user, apiParams):
    # SHORTCUT -
    return True

    githubImg = 'https://avatars1.githubusercontent.com/u/' + str(user['id']) + '?v=4'
    gravatarImg = 'https://github.com/identicons/' + user['login'] + '.png'

    r = postRequest('https://api.deepai.org/api/image-similarity', {'image1': githubImg, 'image2': gravatarImg}, apiParams)

    # extracting data in json format
    data = r.json()
    return data['output']['distance'] < 10


def getRequest2(nextLink):
    while True:
        try:
            reqGet = requests.get(nextLink, stream=True)

            if 'X-RateLimit-Remaining' in reqGet.headers and int(reqGet.headers['X-RateLimit-Remaining']) < 1:
                print('RateLimit exceeded for this hour...')

                time.sleep(max(20,float(reqGet.headers['X-RateLimit-Reset']) - float(datetime.utcnow().timestamp())))
                continue

            return reqGet
        except requests.exceptions.ConnectionError or ConnectionRefusedError:
            print('Connection lost. Retrying...')
            time.sleep(20)


def processUserImages(user, apiParams):
    # SHORTCUT -
    return None

    githubImg = 'https://avatars1.githubusercontent.com/u/' + str(user['id']) + '?v=4'

    if isDefaultImage(user, apiParams):
        imageLocation = matchdefaultDir
        res = False
    else:
        imageLocation = matchcustomDir
        res = True

    response = getRequest2(githubImg)
    with open(imageLocation + user['login'] + '.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

    return res


def processUserData(individuals, user, apiParams, imageApiParams):
    profileName = patronManager.processPatronName(user['login'])
    if profileName is None:
        return

    profileImage = processUserImages(user, imageApiParams)
    userCountry = locateUser(user, apiParams)
    print('User "' + user["login"] + '" from ' + str(userCountryMessage(userCountry)) + ' has image: ' + str(profileImage))

    githubUserContent = ["public_repos", "public_gists", "followers", "following", "created_at"]

    githubUserData = {}
    for githubUserItem in githubUserContent:
        githubUserData[githubUserItem] = user[githubUserItem]

    githubUserData["name"] = userPatronName(user)
    githubUserData["login"] = profileName
    githubUserData["nationality"] = userCountryMessage(userCountry)
    githubUserData["custom_image"] = profileImage

    individuals.append((profileName, githubUserData))


def setupDir(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


class AuthorScanGithubPatrons:

    def scanGithubPatronAssociations(self, users_db):
        individuals = []

        reqGet = None
        try:
            global auth
            auth = loadAuthToken()

            apiParams = {'key': auth[2]}
            apiImageParams = {'api-key': auth[3]}

            setupDir(matchcustomDir + '/a.txt')
            setupDir(matchdefaultDir + '/a.txt')

            for userid, user in users_db.items():
                try:
                    processUserData(individuals, user, apiParams, apiImageParams)
                except KeyError:  # user data changed
                    pass

        except TypeError:
            traceback.print_exc(file=sys.stdout)
            print(reqGet.headers)

        return individuals


    def __init__(self):
        global patronManager
        patronManager = AuthorPatronManager.patronManager


def main():
    global scanner
    scanner = AuthorScanRepository.scanner

    AuthorScanGithubPatrons().scanGithubPatronAssociations(scanner.users_users)


if __name__ == '__main__':
    main()
