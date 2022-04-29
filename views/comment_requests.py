import sqlite3
import json
from xml.etree.ElementTree import Comment

from models.post import Post
from models.user import User
from models.comment import CommentClass

def get_all_comments():
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content,
            p.id postId,
            p.title postTitle,
            u.id authorId,
            u.username
        FROM Comments c
        JOIN Posts p
            ON c.post_id = p.id
        JOIN Users u
            ON c.author_id = u.id
        """)

        # Initialize an empty list to hold all animal representations
        comments = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        for row in dataset:

            comment = CommentClass(row['id'], row['post_id'], row["author_id"], row["content"])

            comment.postId = row['postId']
            comment.postTitle = row['postTitle']
            comment.authorId = row ['authorId']
            comment.username = row['username']
            #post = Post(row['postId'], row['user_id'], row['category_id'], row['postTitle'], row['publication_date'], row['image_url'], row['content'])
            #user = User(row['authorId'], row['authorFirstName'],row['authorLastName'], row['username'])


            #comment.user = user.__dict__

            comments.append(comment.__dict__)

    return json.dumps(comments)

def create_comment(new_comment):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments
            (post_id, author_id, content)
        VALUES
            (?,?,?);
            """, (new_comment['post_id'], new_comment['author_id'], new_comment['content'], ))
            
        id = db_cursor.lastrowid
        
        new_comment['id'] = id
        
    return json.dumps(new_comment)