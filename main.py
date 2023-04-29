import random
import string

class ManageEntry:
    def __init__(self, website, password, username, notes):
        self.website = website
        self.password = password
        self.username = username
        self.notes = notes

    def generatePassword(length):
        letters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(letters) for i in range(length))
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
    global length
    hasAccount = False
    if not hasAccount:
        print("Please enter a username for your new account: ")
        username = input()
        print("Please enter a master password for your new account: ")
        password = input()
        hasAccount = True
        pwList = []

    loggedIn = False
    tries = 3
    while not loggedIn:
        if tries == 0:
            exit()
        print("Please enter the master password: ")
        attempt = input()
        if attempt == password:
             print("Welcome back, " + username + ".")
             loggedIn = True
        else:
            tries-=1
            print("Incorrect password. You have " + str(tries) + " tries remaining.")

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
                password = ManageEntry.generatePassword(8)
                print("Password generated: " + password)
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
