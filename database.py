import sqlite3

conn = sqlite3.connect("deals.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS deals (
id_note INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INT,
name VARCHAR(50),
time VARCHAR(2),
data VARCHAR(2)
)''')
conn.commit()

def add_deal(user_id,name,data,time):
    cursor.execute('''
    INSERT INTO deals (user_id,name,data,time)
    VALUES (?,?,?,?)
    
    ''',(user_id,name,data,time))
    conn.commit()
    last_id = cursor.lastrowid
    return last_id
def show_db():
    all_lines = cursor.execute('''
        SELECT * FROM deals  
    ''')
    return all_lines.fetchall()

def show_deals(user_id):
    all_lines = cursor.execute('''
            SELECT name,data,time FROM deals WHERE user_id = ?
        ''', (user_id,))
    conn.commit()
    return all_lines.fetchall()

def show_deals_del(user_id):
    all_lines = cursor.execute('''
            SELECT name,id_note FROM deals WHERE user_id = ?
        ''', (user_id,))
    conn.commit()
    return all_lines.fetchall()

def deletings_func(id_note: int):
    a = cursor.execute('''
    DELETE FROM deals WHERE id_note = ?
    ''', (id_note,))
    conn.commit()
show_db()
