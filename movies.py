import random
import movie_storage_sql as storage
from data_collector import retrieve_data

MAX_RATING = 10.0
MIN_RATING = 1.0
# MIN_AND_MAX_INDEX_FOR_A_CORRECT_YEAR = 4
# YEAR_OF_FIRST_MOVIE = 1888   # The first movie of the world Roundhay Garden Scene at the Year 1888
LOW_COMMAND_NUMBER = 0
HIGH_COMMAND_NUMBER = 10


def get_sort_year(year):
    """Any movies are a series and have a period as publication year example: 2010–2020
    and that’s what it is – not just a normal hyphen –
    This Function replace the – to normal hyphen and split the period.
    Return the first publication year"""

    if isinstance(year, str):
        year = year.replace("–", "-").strip()
        if "-" in year:
            first_year = year.split("-")[0].strip()
            return int(first_year)
    return int(year)

def print_menu():
    """Main menu printed all option for the user"""

    print("\nWelcome to my movies database")
    print("\nMenu:"
          "\n 0. Exit"
          "\n 1. List movies"
          "\n 2. Add movie"
          "\n 3. Delete movie"
          "\n 4. Update movie"
          "\n 5. Stats"
          "\n 6. Random movie"
          "\n 7. Search movie"
          "\n 8. Movies sorted by rating"
          "\n 9. Movies sorted by year"
          "\n 10. Filter movies")

def get_menu_choice():
    """Gets and validates the user's menu choice"""

    while True:
        try:
            user_input = int(input("\nEnter Choice (0-10): "))
            if LOW_COMMAND_NUMBER <= user_input <= HIGH_COMMAND_NUMBER:
                return user_input
            else:
                print('\nUnknown command, please enter a number between 0 and 10')
        except ValueError:
            print('\nUnknown command, please enter a number between 0 and 10.')

def end_of_program():
    """Exits the movie Database"""

    print('Bye!')
    raise SystemExit

def quit_function():
    """quit a function"""

    input("\nPress enter to continue")


def list_movies():
    """Retrieve and display all movies from the database"""

    all_movies = storage.list_movies()

    print(f"\nThe total of movies is {len(all_movies)}\n")
    for movie in all_movies: #### Hier müsste nochmal nachgeschaut werden ob es so #######
        print(f"Title: {movie} Rating: {all_movies[movie]['rating']}, Year of publication: {all_movies[movie]['year']}")

    quit_function()

def add_movie():
    """Function for add a new movie insert the table of movies"""

    all_movies = storage.list_movies()

    while True:
        userinput_movie_title = input("\nEnter movie title: ").strip()
        if not userinput_movie_title:
            print('Movie title cannot be empty.')
            continue

        break
    if not any(userinput_movie_title.lower() == key.lower() for key in all_movies):        # user_input.lower() here because otherwise .lower() would convert the entire entry in the database to lower case. For example: Transformers Part II == Transformers part ii
        movie_info = retrieve_data(userinput_movie_title)

        if movie_info == None:
            quit_function()
            return

        if movie_info["Response"] == "True":
            title = movie_info["Title"]
            publication_year = movie_info["Year"]
            movie_rating = movie_info["imdbRating"]
            movie_cover = movie_info["Poster"]
            storage.add_movie(title, publication_year, movie_rating, movie_cover)
            print(f"{title} successfully added to the database")
        else:
            print(movie_info["Error"])
    else: print("\nThe Movie is already in the database")

    quit_function()


def delete_movie():
    """Function for delete a movie"""

    all_movies = storage.list_movies()
    userinput_movie_title = input("\nWhich Movie do you want to delete?: ").lower().strip()

    movie_founder = False
    movie_key_founder = ''
    for movie in all_movies:
        if userinput_movie_title == movie.lower():
            movie_founder = True
            movie_key_founder = movie

    if movie_founder:
        storage.delete_movie(movie_key_founder)
        print("\nThe Movie is now deleted")
    else:
        print("\nMovie not found")

    quit_function()

def update_movie():
    """Function for update rating of a movie"""

    all_movies = storage.list_movies()
    userinput_movie_title = input("\nWhich Movie do you want to update?: ").lower().strip()

    movie_founder = False
    movie_key_founder = ''
    for movie in all_movies:
        if userinput_movie_title == movie.lower():
            movie_founder = True
            movie_key_founder = movie

    if movie_founder:
        while True:
            try:
                userinput_movie_rating = float(input("Enter the new rating: "))
                if userinput_movie_rating <= MAX_RATING and userinput_movie_rating >= MIN_RATING:
                    storage.update_movie(movie_key_founder, userinput_movie_rating)
                    print('Movie is now updated')
                    break
                else:
                    print('Select a rating between 1.0 and 10.0')
            except ValueError:
                print('Please enter a number rating')

    else:
        print("\nMovie not found")

    quit_function()

def stats():
    """Function of stats average rating, median, hightest and worst movie by rating"""

    if len(storage.list_movies()) == 0:
        print("Statistics cannot be displayed as there are no movies in the database.")
        quit_function()
        return

    all_movies = storage.list_movies()
    list_of_rating = []
    for movie in all_movies:
        list_of_rating.append(all_movies[movie]["rating"])
    highest_rating = max(list_of_rating)
    lowest_rating = min(list_of_rating)

    print(f"\nThe average rating: {sum(list_of_rating) / len(all_movies):.2f}")

    if len(all_movies) % 2 != 0:
        print(f"The Median is: {sorted(list_of_rating)[len(all_movies) // 2]}")
    else:
        print(f"The Median is: {(sorted(list_of_rating)[len(all_movies) // 2 -1] +
                                 sorted(list_of_rating)[len(all_movies) // 2]) / 2}")

    print("\nThe movie(s) with the highest rating is:")
    for movie in all_movies:
        if all_movies[movie]["rating"] == highest_rating:
            print(f'The movie "{movie}" rated {all_movies[movie]["rating"]}')

    print("The movie(s) with the lowest rating is:")
    for movie in all_movies:
        if all_movies[movie]["rating"] == lowest_rating:
            print(f'The movie "{movie}" rated {all_movies[movie]["rating"]}')

    quit_function()

def random_movie():
    """Function for random movie"""

    if len(storage.list_movies()) == 0:
        print("No movies can be recommended to you as there are no movies in the database.")
        quit_function()
        return

    all_movies = storage.list_movies()
    choice_movie = random.choice(list(all_movies))
    print(f"Your movie for to night, {choice_movie} rated by {all_movies[choice_movie]['rating']}")
    quit_function()


def search_movie():
    """Function for search a movie by user input"""

    if len(storage.list_movies()) == 0:
        print("No movies found to search.")
        quit_function()
        return

    user_input_search_movie = input("Which movie are you searching for?: ").lower().strip()
    movie_founder = False
    all_movies = storage.list_movies()
    for movie in all_movies:
        if user_input_search_movie in movie.lower():
            print(f"{movie} : {all_movies[movie]['rating']}")
            movie_founder = True
    if not movie_founder:
        print("Movie not found")
    quit_function()


def movies_sorted_by_rating():
    """Function movie sorted by rating"""

    if len(storage.list_movies()) == 0:
        print("No movies found to sort.")
        quit_function()
        return

    all_movies = storage.list_movies()
    list_of_movie_tuple = []
    for movie in all_movies:
        list_of_movie_tuple.append((all_movies[movie]["rating"], movie))

    for movie_tuple in sorted(list_of_movie_tuple, reverse=True):
            print(movie_tuple[1] , movie_tuple[0])

    quit_function()

def movies_sorted_by_year():
    """Function movie sorted by year"""

    if len(storage.list_movies()) == 0:
        print("No movies found to sort.")
        quit_function()
        return

    all_movies = storage.list_movies()
    list_of_movie_tuple = []
    for movie in all_movies:
        year = all_movies[movie]["year"]
        sort_year = get_sort_year(year)
        list_of_movie_tuple.append((sort_year, movie))
    user_input = input('Do you want the latest movies first? (Y/N) ').lower().strip()

    while True:

        if user_input == 'y':
            print('')
            for movie_tuple in sorted(list_of_movie_tuple, reverse=True):
                print(movie_tuple[0], movie_tuple[1])
            break

        elif user_input == 'n':
            print('')
            for movie_tuple in sorted(list_of_movie_tuple):
                print(movie_tuple[0], movie_tuple[1])
            break

        else:
            print('please only "Y" or "N"')
            user_input = input('Do you want the latest movies first? (Y/N) ').lower().strip()

    quit_function()

def filter_movies():
    """
    Filters movies based on user-defined criteria.

    The user can enter a minimum rating, a start year, and an end year.
    Empty inputs are treated as no filter for the corresponding criteria.

    The function checks all movies from the movie storage and prints
    all movies matching the selected filters. If no movies match the
    criteria, a message is displayed.
    """
    all_movies = storage.list_movies()

    prompts = [
                (
                    "Enter minimum rating (leave blank for no minimum rating): ",
                    float,
                    "Invalid input. Please enter a valid rating."
                ),
                (
                    "Enter start year (leave blank for no start year): ",
                    int,
                    "Invalid input. Please enter a valid start year."
                ),
                (
                    "Enter end year (leave blank for no end year): ",
                    int,
                    "Invalid input. Please enter a valid end year."
                )
                ]

    values = []

    for prompt, data_type, error_message in prompts:
        while True:
            user_input = input(prompt)

            if user_input == "":
                values.append(None)
                break

            try:
                values.append(data_type(user_input))
                break
            except ValueError:
                print(error_message)

    min_rating, start_year, end_year = values

    filter_movie = []

    for movie in all_movies:
        sort_year = get_sort_year(all_movies[movie]["year"])
        if min_rating is None or min_rating <= all_movies[movie]["rating"]:
            if start_year is None or start_year <= sort_year:
                if end_year is None or end_year >= sort_year:
                    filter_movie.append((movie, sort_year, all_movies[movie]['rating']))

    if filter_movie:
        for movie in filter_movie:
            print(f'{movie[0]} ({movie[1]}): {movie[2]}')
    else:
        print('No movie found')

    quit_function()

def main():

    dict_of_functions = {0: end_of_program,
                         1: list_movies,
                         2: add_movie,
                         3: delete_movie,
                         4: update_movie,
                         5: stats,
                         6: random_movie,
                         7: search_movie,
                         8: movies_sorted_by_rating,
                         9: movies_sorted_by_year,
                         10: filter_movies
                         }

    while True:
        print_menu()
        user_input_command = get_menu_choice()
        dict_of_functions[user_input_command]()

if __name__ == "__main__":
    main()
