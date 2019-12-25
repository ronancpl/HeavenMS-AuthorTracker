import os
import AuthorScanJsonReader

from authorscanner.patrons import AuthorPatronManager

nameDefinitions = set()
linkDefinitions = {}

patronNameAssociations = {}
patronNameAliases = {}


def processPatronEntry(patronData, patronType):
    patronName = patronManager.processSourcePatronName(patronData[0])
    nameDefinitions.add(patronName)

    if len(patronData) > 1:
        patronLinkName = patronManager.processSourcePatronName(patronData[1])

        if patronLinkName not in linkDefinitions:
            patronLinkNames = set()
            linkDefinitions[patronLinkName] = patronLinkNames
        else:
            patronLinkNames = linkDefinitions[patronLinkName]

        patronLinkNames.add(patronName)


def findPatronAliases(name, nameAliases, linkDefinitionsCopy):
    if name in nameAliases:
        return

    nameAliases.add(name)

    if name in linkDefinitionsCopy:
        for aliasName in linkDefinitionsCopy[name]:
            findPatronAliases(aliasName, nameAliases, linkDefinitionsCopy)


def findPatronNameInAliasesList(name, aliases):
    for alias in aliases.values():
        if name in alias:
            return True

    return False


def parseSourcePatrons():
    for link, associates in linkDefinitions.items():
        if link not in nameDefinitions:
            patronNameAssociations[link] = associates

    linkDefinitionsCopy = linkDefinitions.copy()

    for link in patronNameAssociations.keys():
        linkDefinitions.pop(link)

    nonPrimaryNames = set()
    for name in nameDefinitions:
        if name not in linkDefinitions.keys():  # primary names
            nameAliases = set()
            findPatronAliases(name, nameAliases, linkDefinitionsCopy)
            patronNameAliases[name] = nameAliases
        else:
            nonPrimaryNames.add(name)

    for name in nonPrimaryNames:
        if not findPatronNameInAliasesList(name, patronNameAliases):
            nameAliases = set()
            findPatronAliases(name, nameAliases, linkDefinitionsCopy)
            patronNameAliases[name] = nameAliases


def interpretSourcePatrons(patronsLibPath):

    for file in os.listdir(patronsLibPath):
        patronsJson = AuthorScanJsonReader.AuthorScanJsonReader().readFileRaw(patronsLibPath + '/' + file)[0]['content']['patrons']

        for patronsFile in patronsJson:
            fileName = patronsFile[0]
            filePatrons = patronsFile[1]

            if len(filePatrons) > 0:
                for patronData in filePatrons:
                    patronName = patronData[0]
                    patronType = patronData[1]

                    processPatronEntry(patronName, patronType)

            else:
                print('Encoding error on ' + fileName)

    parseSourcePatrons()


def parsePatronAssociations():
    organizations = []
    individuals = []

    # Organizations
    for name, assoc in sorted(patronNameAssociations.items(), key=lambda kv: kv[0]):
        organizations.append((name, assoc))

    # Individuals
    for name, assoc in sorted(patronNameAliases.items(), key=lambda kv: kv[0]):
        individuals.append((name, assoc))

    return (organizations, individuals)


def printPatronAssociations(associations):
    organizations, individuals = associations

    print('Organizations')
    for name, assoc in organizations:
        print('  ' + name + ' : ' + str(assoc))

    print('Individuals')
    for name, assoc in individuals:
        print('  ' + name + ' : ' + str(assoc))


class AuthorScanSourcePatrons:

    def scanFilePatronAssociations(self):
        global patronManager
        patronManager = AuthorPatronManager.patronManager

        interpretSourcePatrons('../../lib/patrons')

        associations = parsePatronAssociations()
        # printPatronAssociations(associations)

        return associations


def main():
    AuthorScanSourcePatrons().scanFilePatronAssociations()

if __name__ == '__main__':
    main()