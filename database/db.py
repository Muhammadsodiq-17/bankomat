import  sqlite3

DATABASE_NAME = "bankomat.db"
def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
      CREATE TABLE IF NOT EXISTS users (
            id TEXT NOT NULL UNIQUE,
            full_name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            is_active INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS cards(  
           id TEXT NOT NULL UNIQUE,
           card_number TEXT UNIQUE,
           pin TEXT,
           user_id TEXT,
           is_blocked INTEGER,
           failed_attempts INTEGER,
           created_at TEXT,
           updated_at TEXT
         )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(
          id TEXT NOT NULL UNIQUE,
          card_id TEXT,
          balance REAL,
          currency TEXT,
          created_at TEXT,
          updated_at TEXT
     )""")
    conn.commit()
    conn.close()