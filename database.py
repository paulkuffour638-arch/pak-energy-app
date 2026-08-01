import os


DATABASE_FILE = "reservoir_database.txt"


def save_record(record):

    try:
        if record.strip() == "":
            return "Please enter a record"

        with open(DATABASE_FILE, "a") as file:
            file.write(record + "\n")

        return "Record saved successfully"

    except Exception as e:
        return f"Error: {e}"


def read_records():

    try:
        if not os.path.exists(DATABASE_FILE):
            return "No records found"

        with open(DATABASE_FILE, "r") as file:
            data = file.read()

        if data.strip() == "":
            return "No records found"

        return data

    except Exception as e:
        return f"Error: {e}"


def clear_database():

    try:
        with open(DATABASE_FILE, "w"):
            pass

        return "Database cleared"

    except Exception as e:
        return f"Error: {e}"