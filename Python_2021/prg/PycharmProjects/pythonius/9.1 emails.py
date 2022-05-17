"""
Write a program that keeps names and email addresses in a dictionary as key-value pairs. The program should display
a menu that lets the user look up a person's email address by name, add a new name and email address, change an
existing email address, and delete an existing name and email address. The program should pickle the dictionary and
save it to a file when the user exits the program. Each time the program starts, it should retrieve the dictionary from
the file and unpickle it.
"""
import pickle


def main():
    # test names and values

    try:  # opens email file and tests where it is present
        email_file = open('email.dat', 'rb')
        emails = pickle.load(email_file)
        email_file.close()
    except FileNotFoundError:
        emails = dict()

    loop_exit = 0
    selection = int(input(
        "\nWhat action would you like to do? \n1. Look up Email by name\n2. Add a new Entry\n3. Change a persons Email\n4. Delete an entry\n5. Quit"))
    try:
        while loop_exit == 0:  # while loop houses the different options the user can choose
            if selection == 1:
                lookup(emails)
                loop_exit = 1
            if selection == 2:
                add_entry(emails)
                loop_exit = 1
            if selection == 3:
                change_entry(emails)
                loop_exit = 1
            if selection == 4:
                delete(emails)
                loop_exit = 1
            if selection == 5:
                print("Ending Program, Goodbye")
                loop_exit = 2
            if selection > 5:
                print("Invalid number, please enter a number 1-5")
                main()
    except ValueError:
        print("Please use a valid number")
        main()


def lookup(searchmail):  # searches emails and displays the found result
    user_name = str(input("Please enter your name to search the database for your email: ")).capitalize()  #
    if user_name in searchmail:
        print("\nYour email", user_name, 'has been found: ', searchmail[user_name])
    else:
        print("\nYour mail was not found")
    main()


def add_entry(addmail):  # adds new entries to mail
    user = input("Enter your name: ")
    mail = input("Enter your email: ")
    addmail[user.capitalize()] = mail
    save(addmail)  # saves the new dictionary


def change_entry(cmail):
    savedchanges = False
    search = input("Input your name and search for your email").capitalize()
    for names in cmail.keys():  # only searches keys
        if names == search:  # tests to see if the searched name is in mails dictionary
            newmail = input("Input your new email")
            cmail[search] = newmail
            save(cmail)
            savedchanges = True
    if not savedchanges:
        print("Error name not found")
        main()


def delete(removal):
    tempsearch = ""
    search = input("Input your name and search for your email").capitalize()
    for names in removal.keys():  # essentialy the same loop as change_entry, just reversed
        if names == search:
            tempsearch = search  # because dictionaties cant remove during iteration, temp holds users search
    try:
        del removal[tempsearch]
        print("Removing", tempsearch)
        save(removal)
    except KeyError:
        print("Error, name not found")
        main()


def save(email):  # saves the dictionary to email.dat
    try:
        save_file = open('email.dat', 'wb')
        pickle.dump(email, save_file)
        save_file.close()
        print("\nSave successful")
        main()
    except KeyError:
        print("\nThere was an error saving to the file")
        main()


main()
