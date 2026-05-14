import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

# Reset everything
cur.execute("DROP TABLE IF EXISTS events")
cur.execute("""
    CREATE TABLE events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        date TEXT,
        location TEXT,
        available_seats INTEGER,
        price INTEGER
    )
""")

# Add sample data so the Marketplace isn't empty
sample_events = [
    ('Global AI Summit 2026', '2026-06-12', 'JECRC Main Hall', 150, 499),
    ('Eco-Tech Workshop', '2026-07-05', 'Jaipur Tech Hub', 45, 0),
    ('Corporate Leadership Seminar', '2026-08-10', 'Virtual (Zoom)', 500, 299)
]

cur.executemany("INSERT INTO events (title, date, location, available_seats, price) VALUES (?,?,?,?,?)", sample_events)

conn.commit()
conn.close()
print("Database reset and populated! Now refresh your browser.")