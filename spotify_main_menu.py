#Emily Torres
#Spotify Database REPL

import sqlite3
import datetime

PROMPT = '%> '
SPOT_DB = 'spotify_database.db'

def spot_repl():
    print ('\nWelcome to Your Spotify Streaming History Database. \n')
    initialize_database()
    while True:
        main_menu() #?
        choice = input(PROMPT)
        if choice == '9':
            break
        elif choice == '1':
            artistFind()
        elif choice =='2':
            print('Your Top 10 Songs from March 2022 to March 2023: \n')
            topSongs()
        elif choice == '3':
            print('Your Top 10 Artists from March 2022 to March 2023: \n')
            topArtists()
        elif choice == '4':
            listenPeriod()
        elif choice == '5':
            print('Here is your dance party playlist...go forth and party hard! \n')
            print('Dance Party Playlist 2023 \n')
            danceParty()
    db.close()
    print('\nThanks for using the Spotify Streaming History Database. See you later!\n')

def main_menu():
    print("""
Spotify Streaming History Database Main Menu
=============================================
1) Find the artist of a track from my streaming history. 
2) Produce a list of my top 10 most popular songs. 
3) Produce a list of my top 10 most popular artists.
4) What songs did I listen to between (start date) and (end date)?
5) Create a dance party playlist from my streaming history!

9) Quit.
""")

def initialize_database():
    global db
    try:
        db = sqlite3.connect(SPOT_DB)
        bogus_query = 'SELECT * FROM Streaming_History'
        db.execute(bogus_query)
    except:
        raise RuntimeError(f'Unable to connect to "{SPOT_DB}" as expected.')

# Verify date input.
def validate(date_text):
        try:
            datetime.date.fromisoformat(date_text)
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return(date_text)

# If there's more than one artist with that song title...
def multi_choice(list_of_tracks):
    print ("\nThere is more than one track with that title in this database.\n\nEnter the number of the artist you're looking for:\n")
    count = 0
    for track in list_of_tracks:
        print (f"{count}. {track[0]}")
        count = count +1
    while True:
        try:
            answer = int(input("\nNumber here: "))
            if answer < len(list_of_tracks): break 
        except: print("The input was not a valid integer. Please try again.")
    return [list_of_tracks[answer]]


# QUERY #1: Find the artist of a track.
def artistFind():
    track_input = input("Please enter the name of the track: ").strip()

    q = """ SELECT DISTINCT artist_name
FROM Track_Info
WHERE track_name = ? """
    c = db.execute(q, (track_input,))
    t = c.fetchall()
    if not t: print (f"\nThere is no song titled {track_input} in the database. Please try again.")
    if len(t) > 1:
        t = multi_choice(t)
    for line in t:
        print('\n'f'{track_input} is a song by ' f'{line[0]}')
    

# QUERY #2: Produce a list of my top 10 most popular songs
def topSongs():
    q = """ SELECT track_name, COUNT(*) as n
FROM Streaming_History
GROUP BY track_name
ORDER BY n DESC
LIMIT 10;"""
    c = db.execute(q)
    t = c.fetchall()
    for line in t:
        print('-- ' 'You listened to ' f'{line[0]} {line[1]}' ' times')

# QUERY #3: Produce a list of my top 10 most popular artists
def topArtists():
    q = """ SELECT artist_name, COUNT(*) as n
FROM Streaming_History
GROUP BY artist_name
ORDER BY n DESC
LIMIT 10;"""
    c = db.execute(q)
    t = c.fetchall()
    for line in t:
        print('-- ' 'You listened to ' f'{line[0]} {line[1]}' ' times')

# QUERY #4: What songs did I listen to between (start date) and (end date)?
def listenPeriod():
    s_date = input("Please enter the date you want your streaming history to start: ").strip()
    e_date = input("Please enter the date you want your streaming history to end: ").strip()
    begin_date = validate(s_date)
    end_date = validate(e_date)
    q = """SELECT DISTINCT artist_name, track_name
FROM Streaming_History 
WHERE date(datetime) >= ? AND date(datetime) <= ? """
    c = db.execute(q, (begin_date, end_date))
    t = c.fetchall()
    if not t: print (f"\nYou did not listen to any tracks between {s_date} and {e_date}.")
    for line in t:
        print('\n'f'{line[1]}' ' by ' f'{line[0]}')

# QUERY #5: Create a dance party playlist from my streaming history!
def danceParty():
    q = """ SELECT DISTINCT track_name, artist_name
FROM Track_Features
ORDER BY danceability DESC
LIMIT 50;"""
    c = db.execute(q)
    t = c.fetchall()
    for line in t:
        print('-- ' f'{line[0]}' ' by ' f'{line[1]}')
