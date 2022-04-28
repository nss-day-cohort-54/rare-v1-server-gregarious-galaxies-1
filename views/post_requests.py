import sqlite3
import json


from models.category import Category
from models.post import Post
from models.user import User


def get_all_posts():
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            c.label category_label,
            u.first_name user_fn,
            u.last_name user_ln
        FROM Posts p
        JOIN Categories c
            ON c.id = p.category_id
        JOIN Users u
            ON u.id = p.user_id
        """)

        # Initialize an empty list to hold all animal representations
        posts = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            post = Post(row['id'], row['user_id'], row["category_id"], row["title"],
                        row["publication_date"], row["image_url"], row["content"])

            category = Category(row['category_id'], row['category_label'])

            user = User(row['user_id'], row['user_fn'],
                        row['user_ln'])

            post.category = category.__dict__

            post.user = user.__dict__

            posts.append(post.__dict__)

    return json.dumps(posts)


def create_post(new_post):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Posts
            (user_id, category_id, title, publication_date, image_url, content)
        VALUES
            ( ?, ?, ?, ?, ?, ?);
        """, (new_post['user_id'], new_post['category_id'], new_post['title'],new_post['publication_date'], new_post['image_url'], new_post['content'] ))

        id = db_cursor.lastrowid
        new_post['id'] = id

        # loop through the tags after adding new post
        # w/n loop execute SQL command to INSERT a row to posttag table
    
    #     for tag in new_post['tags']:

    #         db_cursor.execute("""
    #         INSERT INTO PostTag
    #             (post_id, tag_id)
    #         VALUES
    #             (?,?);
    #         """, (id, tag))
    return json.dumps(new_post)

def get_single_post(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            c.label category_label,
            u.first_name user_fn,
            u.last_name user_ln
        FROM Posts p
        JOIN Categories c
            ON c.id = p.category_id
        JOIN Users u
            ON u.id = p.user_id
        WHERE p.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row

        post = Post(data['id'], data['user_id'], data["category_id"], data["title"],
                    data["publication_date"], data["image_url"], data["content"])

        category = Category(data['category_id'], data['category_label'])

        user = User(data['user_id'], data['user_fn'],
                    data['user_ln'])

        post.category = category.__dict__

        post.user = user.__dict__

        return json.dumps(post.__dict__)
