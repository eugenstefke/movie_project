from sqlalchemy import create_engine, text
from sqlalchemy import event

# Define the database URL
DB_URL = "sqlite:///data/app.db"

# Create the engine
engine = create_engine(DB_URL, echo=False) # echo=True for debbuging print all SQL Commands
@event.listens_for(engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

# Create the movies table if it does not exist
with engine.connect() as connection:
    connection.execute(text("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, title TEXT NOT NULL,year INTEGER NOT NULL,rating REAL NOT NULL, cover_url TEXT NOT NULL, FOREIGN KEY (user_id) REFERENCES users(user_id))"))
    connection.commit()

# with engine.connect() as connection:
#     """Function for adding an additional table column.
#     Important: run this only once; comment it out again after execution! """
#     connection.execute(text("ALTER TABLE movies ADD COLUMN imdb_id TEXT"))
#     connection.commit()

def list_movies(user_id):
    """Retrieve all movies for a specific user from the database."""
    with engine.connect() as connection:
        result = connection.execute(text("""SELECT title, year, rating, cover_url, imdb_id FROM movies WHERE user_id = :user_id"""),
                                    {"user_id": user_id})
        movies = result.fetchall()

    return {row[0]: {"year": row[1], "rating": row[2], "cover_url": row[3], "imdb_id": row[4]} for row in movies}

def add_movie(title, year, rating, cover_url, user_id, imdb_id):
    """Add a new movie to the database."""
    with engine.connect() as connection:
        try:
            connection.execute(text("INSERT INTO movies (title, year, rating, cover_url, user_id, imdb_id) VALUES (:title, :year, :rating, :cover_url, :user_id, :imdb_id)"),
                               {"title": title, "year": year, "rating": rating, "cover_url": cover_url, "user_id": user_id, "imdb_id": imdb_id})
            connection.commit()
        except Exception as e:
            print(f"Error: {e}")

def delete_movie(title, user_id):
    """Delete a movie from the database."""
    with engine.connect() as connection:
        try:
            connection.execute(text("DELETE FROM movies WHERE title = :title AND user_id = :user_id"),
                               {"title": title, "user_id": user_id})
            connection.commit()
            print(f"Movie '{title}' deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")


def update_movie(title, rating, user_id):
    """Update a movie's rating in the database."""
    with engine.connect() as connection:
        try:
            connection.execute(text("UPDATE movies SET rating = :rating WHERE title = :title AND user_id = :user_id"),
                               {"title": title, "rating": rating, "user_id": user_id})
            connection.commit()
            print(f"Movie '{title}' successfully updated.")
        except Exception as e:
            print(f"Error: {e}")