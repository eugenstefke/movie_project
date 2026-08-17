import user_storage_sql as storage
import movies

LOW_COMMAND_NUMBER = 1

def welcome_screen():
    """The welcome screen from the App"""
    all_users = storage.list_user()
    print("\nWelcome to the Movie App!")

    print("\nSelect a user:")
    for i in range(len(all_users)):
        print(f"{i + 1}. {all_users[i]["name"]}")

    print(f"{len(all_users) +1}. Create a new user")
    print(f"{len(all_users) +2}. Update the name of user")
    print(f"{len(all_users) +3}. Delete a user")


def user_query():
    """The function for querying the user's command"""
    all_users = storage.list_user()
    while True:
        try:
            user_input = int(input(f"\nEnter Choice ({LOW_COMMAND_NUMBER} - {len(all_users) + 3}): "))
            if LOW_COMMAND_NUMBER <= user_input <= len(all_users) + 3:
                return user_input, all_users
            else:
                print(f'\nUnknown command, please enter a number between {LOW_COMMAND_NUMBER} and {len(all_users) + 3}')
        except ValueError:
            print(f'\nUnknown command, please enter a number between {LOW_COMMAND_NUMBER} and {len(all_users) + 3}')

def creat_user():
    """Function for adding a new user.
    It asks the user for the name to be created and checks whether that name is already in use.
    If it is not, the new username is passed to the ‘add_user’ function in the ‘user_storage_sql.py’ file. """

    all_users = storage.list_user()
    while True:
        new_username = input("Enter the name of the user: ").strip()
        if not any(new_username == key["name"] for key in all_users):
            if new_username:
                storage.add_user(new_username)
                break
            else:
                print("Username must contain at least 1 character, try again!")
                continue
        else:
            print("The username is already taken. Please choose a different one or add a number after your name.")
            continue

def update_user():
    """The `list_user` function from the `user_storage_sql` file is called, and all users are stored in `all_users`.
    Ask the user for the name to be updated for one of the users.
    Check whether this name already exists; if so, a further prompt is displayed asking for the new name the user should be given.
    The new username is then passed to the `update_user` function from the file `user_storage_sql.py`."""

    all_users = storage.list_user()
    while True:
        old_username = input("Enter the name of the user which do you want updated: ").strip()
        for user in all_users:
            if old_username == user["name"]:
                while True:
                    new_username = input("Enter the new name of the user: ").strip()
                    if not new_username:
                        print("Username must contain at least 1 character, try again!")
                    else:
                        storage.update_user(old_username, new_username)
                        break
                break
        else:
            print("Username not recognised. Please note that upper and lower case letters are important, try again!")
            continue
        break

def delete_user():
    """The function `list_user` from the file `user_storage_sql` is called, and all users are stored in `all_users`.
    The user is prompted to enter the name of one of the users to be deleted.
    A check is carried out to see if this name already exists; if so, the name is passed to the `delete_user` function from the file `user_storage_sql.py`."""

    all_users = storage.list_user()
    while True:

        username = input("Enter the name of the user which do you want delete: ")
        for user in all_users:
            if username == user["name"]:
                storage.delete_user(username)
                return
        else:
            print("Username not recognised. Please note that upper and lower case letters are important, try again!")

def main():

    while True:
        welcome_screen()
        userinput, all_users = user_query()

        if LOW_COMMAND_NUMBER <= userinput <= len(all_users):
            movies.main(all_users[userinput - 1])
        elif userinput == len(all_users) + 1:
            creat_user()
        elif userinput == len(all_users) + 2:
            update_user()
        elif userinput == len(all_users) + 3:
            delete_user()

if __name__ == "__main__":
    main()