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
            SELECT name FROM deals WHERE user_id = ?
        ''', (user_id,))
    conn.commit()
    return all_lines.fetchall()

def show_date(user_id):
    all_lines = cursor.execute('''
            SELECT data FROM deals WHERE user_id = ?
        ''', (user_id,))
    conn.commit()
    return all_lines.fetchall()

def show_time(user_id):
    all_lines = cursor.execute('''
            SELECT time FROM deals WHERE user_id = ?
        ''', (user_id,))
    conn.commit()
    return all_lines.fetchall()
show_db()