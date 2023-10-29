'''
This is a console bot-assitant.
The bot works with following commands:

1) add [Name] [Phone]                      Add new contact with a "Name" and "Phone number".
2) change [Name] [New phone]               Change phone number to "New phone" for contact with "Name".
3) phone [Name]                            Show phohne number for contact "Name".
4) all                                     Show all contacts in AddressBook.
5) add-birthday [Name] [Date of Birth]     Add "Date of Birth" for contact "Name".
6) show-birthday [Name]                    Show Date of Birth for contact "Name".
7) birthdays                               Show all birthdays for the next week.
8) hello                                   Receive "Hello" from the bot.
9) close OR exit                           Close the program.
10) help                                   Get this list of commands.
'''



from classes import AddressBook, Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me correct data."
        except IndexError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name"

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args 
    rec = Record(name)
    rec.add_phone(phone)
    contacts.add_record(rec)
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name = args[0]
    rec = contacts.find(name)
    new_phone = args[1]
    old_phone = str(rec.find_old_phone())
    rec.edit_phone(old_phone, new_phone)
    return "Contact updated."

@input_error
def user_phone(args, contacts):
    name = args[0]
    rec = contacts.find(name)
    phone = contacts[name]
    return (phone)

def all_contacts(contacts):
   for name, record in contacts.data.items():
       print(record)

@input_error
def add_birthday(args, contacts):
    name = args[0]
    rec = contacts.find(name)
    birthday = args[1]
    rec.add_birthday(birthday)
    return "Birthday added."

def show_birthday(args, contacts):
    name = args[0]
    rec = contacts.find(name)
    return((rec.show_birthday()))

def birthdays(contacts):
    birthdays_dict = dict(contacts.week_birthdays(contacts))
    return(birthdays_dict)

def main():
    contacts = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if user_input == '':
            continue
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(user_phone(args, contacts))
        elif command == "all":
            all_contacts(contacts)
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            print(birthdays(contacts))
        elif command == "help":
            print(f"""
            This is a console bot-assitant.
            The bot works with following commands:
1) add [Name] [Phone]                      Add new contact with a "Name" and "Phone number".
2) change [Name] [New phone]               Change phone number to "New phone" for contact with "Name".
3) phone [Name]                            Show phohne number for contact "Name".
4) all                                     Show all contacts in AddressBook.
5) add-birthday [Name] [Date of Birth]     Add "Date of Birth" for contact "Name".
6) show-birthday [Name]                    Show Date of Birth for contact "Name".
7) birthdays                               Show all birthdays for the next week.
8) hello                                   Receive "Hello" from the bot.
9) close OR exit                           Close the program.
10) help                                   Get this list of commands.        """)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
