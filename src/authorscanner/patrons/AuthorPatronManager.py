class AuthorPatronManager:

    devteams = set()
    lowercaseNames = {}

    patron_alias_individuals = {}   # links alias name to the respective entity
    patron_alias_filiations = {}    # links alias name to a cojoint entity

    inexistent_patrons = set()


    def processPatronName(self, patronName):
        patronName = patronName.strip()
        if len(patronName) == 0:
            return None

        if patronName.endswith(' dev team'):
            patronName = patronName[:-9]
            lowercaseName = patronName.lower()
            self.devteams.add(lowercaseName)
        else:
            lowercaseName = patronName.lower()

        self.lowercaseNames[lowercaseName] = patronName
        return lowercaseName


    def processSourcePatronName(self, patronName):
        if patronName[-1] == u"\u000C":
            patronName = patronName[:-1]
            lowercaseName = patronName.lower()
            self.devteams.add(lowercaseName)
        else:
            lowercaseName = patronName.lower()

        self.lowercaseNames[lowercaseName] = patronName
        return lowercaseName


    def recoverPatronName(self, lowercaseName):
        # only recover when getting to "display" the name, use processed version for management

        if lowercaseName not in self.lowercaseNames:
            return None

        patronName = self.lowercaseNames[lowercaseName]

        if lowercaseName in self.devteams:
            patronName += ' dev team'

        return patronName


    def importPatrons(self, patrons_individuals, patrons_links, patrons_filiations):
        # links: alias name referencing main patron name

        for patron_name, patron_data in patrons_individuals.items():
            self.patron_alias_individuals[patron_name] = patron_data

        for alias_name, patron_name in patrons_links.items():
            self.patron_alias_individuals[alias_name] = self.patron_alias_individuals[patron_name]

        for filiation_name, filiation_members in patrons_filiations:
            filiation_team = set()
            for member_name in filiation_members:
                filiation_team.add(self.patron_alias_individuals[member_name])

            self.patron_alias_filiations[filiation_name] = filiation_team


    def getPatron(self, patron_alias):
        patron_alias_name = self.processPatronName(patron_alias)

        if patron_alias_name in self.patron_alias_individuals:
            return [self.patron_alias_individuals[patron_alias_name]]

        elif patron_alias_name in self.patron_alias_filiations:
            return self.patron_alias_filiations[patron_alias_name]

        self.inexistent_patrons.add(patron_alias)
        # print('[INVALID] Not found patron "' + patron_alias + '"')
        return []


    def exportPatronsList(self):
        patrons_list = set()

        for patron in self.patron_alias_individuals.values():
            patrons_list.add(patron)

        return patrons_list


    def dumpPatrons(self):
        print(' ----- patrons list -----')
        print('  Individuals:')
        for patron_name, patron_data in self.patron_alias_individuals.items():
            print(str(patron_name) + ' : ' + str(patron_data))

        print()
        print('  Filiations:')
        for patron_name, patron_data in self.patron_alias_filiations.items():
            fil_str = '('
            for patron_member in patron_data:
                fil_str += (str(patron_member) + ', ')
            fil_str += ')'

            print(patron_name + ' : ' + fil_str)


global patronManager
patronManager = AuthorPatronManager()