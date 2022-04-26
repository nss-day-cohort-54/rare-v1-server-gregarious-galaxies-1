import sqlite3
import json
from models.category import Category

def get_all_categories():
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Categories c
        ORDER BY Label ASC;
        """)

        # Initialize an empty list to hold all animal representations
        categories = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.

            category = Category(row['id'], row['label'])

            categories.append(category.__dict__)

    return json.dumps(categories)
