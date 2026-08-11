import requests
import os
from dotenv import load_dotenv # to load the .env file

def retrieve_data(title):
    """Retrieve the movie data."""


    load_dotenv()
    api_key = os.getenv("API_KEY")

    URL = "http://www.omdbapi.com/?"
    PARAMETERS = {"t" : title}
    HEADERS = {"apikey" : api_key}

    get_requ = requests.get(URL, params=PARAMETERS, headers=HEADERS)

    if get_requ.status_code == 200:
        movie_infos = get_requ.json()
        write_data(movie_infos)
        return animal_infos
    else:
        print(f"Data Error: Status {get_requ.status_code}")
        return []