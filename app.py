import sqlite3

# Connect to the database
conn = sqlite3.connect('concerts.db')
cursor = conn.cursor()

# Creating tables
def create_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS bands (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        hometown TEXT NOT NULL
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS venues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        city TEXT NOT NULL
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS concerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        band_id INTEGER,
        venue_id INTEGER,
        date TEXT,
        FOREIGN KEY(band_id) REFERENCES bands(id),
        FOREIGN KEY(venue_id) REFERENCES venues(id)
    )''')
    
    conn.commit()

# Insert sample data
def insert_sample_data():
    cursor.execute("INSERT INTO bands (name, hometown) VALUES ('The Beatles', 'Liverpool')")
    cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Queen', 'London')")
    cursor.execute("INSERT INTO venues (title, city) VALUES ('Madison Square Garden', 'New York')")
    cursor.execute("INSERT INTO venues (title, city) VALUES ('Wembley Stadium', 'London')")
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 1, '2024-05-10')")
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (2, 2, '2024-06-15')")
    conn.commit()

# Concert Methods
def get_band(concert_id):
    cursor.execute("""
    SELECT bands.* FROM bands
    JOIN concerts ON concerts.band_id = bands.id
    WHERE concerts.id = ?
    """, (concert_id,))
    return cursor.fetchone()

def get_venue(concert_id):
    cursor.execute("""
    SELECT venues.* FROM venues
    JOIN concerts ON concerts.venue_id = venues.id
    WHERE concerts.id = ?
    """, (concert_id,))
    return cursor.fetchone()

def hometown_show(concert_id):
    cursor.execute("""
    SELECT bands.hometown, venues.city FROM concerts
    JOIN bands ON concerts.band_id = bands.id
    JOIN venues ON concerts.venue_id = venues.id
    WHERE concerts.id = ?
    """, (concert_id,))
    band_hometown, venue_city = cursor.fetchone()
    return band_hometown == venue_city

def concert_introduction(concert_id):
    cursor.execute("""
    SELECT bands.name, bands.hometown, venues.city FROM concerts
    JOIN bands ON concerts.band_id = bands.id
    JOIN venues ON concerts.venue_id = venues.id
    WHERE concerts.id = ?
    """, (concert_id,))
    band_name, band_hometown, venue_city = cursor.fetchone()
    return f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"

# Band Methods
def get_concerts_for_band(band_id):
    cursor.execute("""
    SELECT * FROM concerts
    WHERE band_id = ?
    """, (band_id,))
    return cursor.fetchall()

def get_venues_for_band(band_id):
    cursor.execute("""
    SELECT DISTINCT venues.* FROM venues
    JOIN concerts ON concerts.venue_id = venues.id
    WHERE concerts.band_id = ?
    """, (band_id,))
    return cursor.fetchall()

def play_in_venue(band_id, venue_id, date):
    cursor.execute("""
    INSERT INTO concerts (band_id, venue_id, date) 
    VALUES (?, ?, ?)
    """, (band_id, venue_id, date))
    conn.commit()

def all_introductions(band_id):
    cursor.execute("""
    SELECT venues.city, bands.name, bands.hometown FROM concerts
    JOIN venues ON concerts.venue_id = venues.id
    JOIN bands ON concerts.band_id = bands.id
    WHERE bands.id = ?
    """, (band_id,))
    introductions = cursor.fetchall()
    return [f"Hello {city}!!!!! We are {name} and we're from {hometown}" for city, name, hometown in introductions]

def most_performances():
    cursor.execute("""
    SELECT bands.name FROM concerts
    JOIN bands ON concerts.band_id = bands.id
    GROUP BY bands.id
    ORDER BY COUNT(concerts.id) DESC
    LIMIT 1
    """)
    return cursor.fetchone()

# Venue Methods
def get_concerts_for_venue(venue_id):
    cursor.execute("""
    SELECT * FROM concerts
    WHERE venue_id = ?
    """, (venue_id,))
    return cursor.fetchall()

def get_bands_for_venue(venue_id):
    cursor.execute("""
    SELECT DISTINCT bands.* FROM bands
    JOIN concerts ON concerts.band_id = bands.id
    WHERE concerts.venue_id = ?
    """, (venue_id,))
    return cursor.fetchall()

def concert_on(venue_id, date):
    cursor.execute("""
    SELECT * FROM concerts
    WHERE venue_id = ? AND date = ?
    """, (venue_id, date))
    return cursor.fetchone()

def most_frequent_band(venue_id):
    cursor.execute("""
    SELECT bands.name FROM concerts
    JOIN bands ON concerts.band_id = bands.id
    WHERE venue_id = ?
    GROUP BY bands.id
    ORDER BY COUNT(concerts.id) DESC
    LIMIT 1
    """, (venue_id,))
    return cursor.fetchone()

# Initialize the database
if __name__ == "__main__":
    create_tables()
    insert_sample_data()

    # Test some methods
    print("Concert Band:", get_band(1))
    print("Concert Venue:", get_venue(1))
    print("Is Hometown Show:", hometown_show(1))
    print("Concert Introduction:", concert_introduction(1))
    print("Band's Concerts:", get_concerts_for_band(1))
    print("Band's Venues:", get_venues_for_band(1))
    print("All Introductions for Band:", all_introductions(1))
    print("Band with Most Performances:", most_performances())
    print("Venue's Concerts:", get_concerts_for_venue(1))
    print("Venue's Bands:", get_bands_for_venue(1))
    print("Concert on Date:", concert_on(1, '2024-05-10'))
    print("Venue's Most Frequent Band:", most_frequent_band(1))
