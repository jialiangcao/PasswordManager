class ManageEntry:
    def __init__(self, website, password, username, notes):
        self.website = website
        self.password = password
        self.username = username
        self.notes = notes

    def generatePassword(self, length):
        import random
        import string
        password = ""
        for i in range(int(length)):
            password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        return password
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


class Main:
    hasAccount = False
    if not hasAccount:
        print("Please enter a username for your new account: ")
        username = input()
        print("Please enter a master password for your new account: ")
        password = input()
        hasAccount = True
        pwList = []

    print("Please enter the master password: ")
    attempt = input()
    if attempt == password:
        loggedIn = True
        print("Welcome back, " + username + ".")

    while loggedIn:
        print("What would you like to do?\n1. Add a new password\n2. View a password\n3. Delete a password\n4. Change "
              "your master password\n5. Exit")
        choice = input()
        if choice == "1":
            print("Please enter the name of the website: ")
            website = input()
            print("Please enter the username for the website: ")
            username = input()
            print("Please enter the password for the website: \nType 'gen' to generate a password.")
            password = input()
            if password == "gen":
                print("Please enter the length of the password: ")
                length = input()
                password = ManageEntry.generatePassword(length)
            print("Please enter any notes or comments: ")
            newEntry = ManageEntry(website, password, username, input())
            pwList.append(newEntry)
            print("Password added successfully.")
        if choice == "2":
            print("Please enter the name of the website: ")
            website = input()
            for entry in pwList:
                if entry.getWebsite() == website:
                    print("Username: " + entry.getUsername())
                    print("Password: " + entry.getPassword())
                    print("Notes: " + entry.getNotes())
        if choice == "3":
            print("Please enter the name of the website: ")
            website = input()
            for entry in pwList:
                if entry.getWebsite() == website:
                    pwList.remove(entry)
                    print("Password deleted successfully.")
        if choice == "4":
            print("Please enter your current master password: ")
            attempt = input()
            if attempt == password:
                print("Please enter your new master password: ")
                password = input()
                print("Master password changed successfully.")
            else:
                print("Incorrect password.")
        if choice == "5":
            print("Shutting down. Beep.")
            exit()
