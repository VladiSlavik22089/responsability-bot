import sqlite3

conn = sqlite3.connect("deals.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS deals (
id_note INTEGER PRIMARY KEY AUTOINCREMENT,
id_user INT,
name VARCHAR(50),
time VARCHAR(50),
f INT
)''')
conn.commit()
def add_deal(user_id,name,time,f):
    cursor.execute('''
    INSERT INTO deals (id_user,name,time,f)
    VALUES (?,?,?,?)
    
    ''',(user_id,name,time,f))
    conn.commit()
def show_db():
    all_lines = cursor.execute('''
        SELECT * FROM deals  
    ''')
    return all_lines.fetchall()
def show_deals(user_id):
    all_deals = show_db()
    for i in range(len(all_deals)):
        print(i)
        print(all_deals)
        print(user_id)
        if int(all_deals[i][1]) == int(user_id):
            print("123456")
            print(all_deals[i][2],all_deals[i][3])
    conn.commit()