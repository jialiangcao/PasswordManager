class ManageEntry:
    def __init__(self, website, password, username, notes):
        self.website = website
        self.password = password
        self.username = username
        self.notes = notes

    def getWebsite(self):
        return self.website

    def getPassword(self):
        return self.password

    def getUsername(self):
        return self.username

    def getNotes(self):
        return self.notes

    def setWebsite(self, website):
        self.website = website

    def setPassword(self, password):
        self.password = password

    def setUsername(self, username):
        self.username = username

    def setNotes(self, notes):
        self.notes = notes