import sqlite3
import json

from models.tag import Tag

def get_all_tags():
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tags t
        ORDER by t.label ASC
        """)

        tags = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            
            tag = Tag(row['id'], row['label'])
            
            tags.append(tag.__dict__)

    return json.dumps(tags)

def get_single_tag(id):
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        From Tag t
        WHERE t.id = ?
        """, (id, ))
        
        data = db_cursor.fetchone()
        
        tag = Tag(data['id'], data['label'])
        
    return json.dumps(tag.__dict__)

def delete_tag(id):
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        DELETE FROM tags
        WHERE id = ?
        """, (id, ))
        
def edit_tag(id, editted_tag):
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        UPDATE Tags
            SET
                label = ?,
        WHERE id =?
        """, (editted_tag['label'], id, ))
        
        rows_affected = db_cursor.rowcount
        
        if rows_affected == 0:
            return False
        else:
            return True