import user_storage_sql as storage
import movies

LOW_COMMAND_NUMBER = 1

def welcome_screen():
    all_users = storage.list_user()
    print("\nWelcome to the Movie App!")

    print("\nSelect a user:")
    for i in range(len(all_users)):
        print(f"{i + 1}. {all_users[i]["name"]}")

    print(f"{len(all_users) +1}. Create a new user")
    print(f"{len(all_users) +2}. Update the name of user")
    print(f"{len(all_users) +3}. Delete a user")


def user_query():
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
    all_users = storage.list_user()
    while True:
        new_username = input("Enter the name of the user: ")
        if not any(new_username.lower() == key["name"].lower() for key in all_users):
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
    all_users = storage.list_user()
    while True:
        old_username = input("Enter the name of the user which do you want updated: ").strip()
        for user in all_users:
            if old_username.lower() == user["name"].lower():
                while True:
                    new_username = input("Enter the new name of the user: ").strip()
                    if not new_username:
                        print("Username must contain at least 1 character, try again!")
                    else:
                        storage.update_user(old_username, new_username)
                        break
                break
        else:
            print("Username not recognised, try again!")
            continue
        break

def delete_user():
    all_users = storage.list_user()
    while True:

        username = input("Enter the name of the user which do you want delete: ").strip()
        for user in all_users:
            if username.lower() == user["name"].lower():
                storage.delete_user(username)
                break
        else:
            print("Username not recognised, try again!")
        break

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