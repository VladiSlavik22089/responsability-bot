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

def deletings_func(id_note: int, user_id: int):
    a = cursor.execute('''
    DELETE FROM deals WHERE id_note = ? AND user_id = ?
    ''', (id_note, user_id))
    conn.commit()
show_db()