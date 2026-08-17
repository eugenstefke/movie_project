from sqlalchemy import create_engine, text

# Define the database URL
DB_URL = "sqlite:///app.db"

# Create the engine
engine = create_engine(DB_URL, echo=False)  # echo=True for debbuging print all SQL Commands

# Create the user table if it does not exist
with engine.connect() as users_connection:
    users_connection.execute(text("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT UNIQUE NOT NULL)"))
    users_connection.commit()


def list_user():
    """Retrieve all movies from the database."""
    with engine.connect() as connection:
        result = connection.execute(text("SELECT user_id, name FROM users"))
        users = result.fetchall()

    return [{"user_id": row[0], "name": row[1]} for row in users]


def add_user(name):
    """Add a new user to the database."""
    with engine.connect() as connection:
        try:
            connection.execute(text("INSERT INTO users (name) VALUES (:name)"),
                               {"name": name})
            connection.commit()
        except Exception as e:
            print(f"Error: {e}")


def delete_user(name):
    """Delete a user from the database."""
    with engine.connect() as connection:
        try:
            connection.execute(text("DELETE FROM users WHERE name = :name"),
                               {"name": name})
            connection.commit()
            print(f"User: '{name}' deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")


def update_user(name, newname):
    """Update new user name of a user  in the database."""
    with engine.connect() as connection:
        try:
            connection.execute(text("UPDATE users SET name = :newname WHERE name = :name"),
                               {"name": name, "newname": newname})
            connection.commit()
            print(f"User: '{name}' successfully updated to '{newname}'.")
        except Exception as e:
            print(f"Error: {e}")