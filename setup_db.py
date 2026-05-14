import sqlite3

def setup():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS events")
    cur.execute("""
        CREATE TABLE events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            date TEXT NOT NULL,
            location TEXT NOT NULL,
            description TEXT,
            available_seats INTEGER NOT NULL,
            price INTEGER NOT NULL DEFAULT 0
        )
    """)
    # Add one sample event with details
    cur.execute("INSERT INTO events (title, date, location, description, available_seats, price) VALUES (?,?,?,?,?,?)",
                ('Tech Summit 2026', '2026-05-20', 'JECRC Main Hall', 'Join industry leaders for a deep dive into AI and Cloud computing.', 100, 499))
    conn.commit()
    conn.close()
    print("Database updated!")

if __name__ == "__main__":
    setup()