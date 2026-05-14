
    DROP TABLE IF EXISTS events;
    CREATE TABLE events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        date TEXT NOT NULL,
        location TEXT NOT NULL,
        available_seats INTEGER NOT NULL,
        price INTEGER NOT NULL
    );
    