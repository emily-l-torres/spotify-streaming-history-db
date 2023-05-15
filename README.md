# spotify-streaming-history-db

Spotify Streaming History Database (Applications of Python + SQL)

** ~ Hello and welcome to the Spotify Streaming History Database! ~ **

*******************
TO RUN THE PROGRAM:

- Run 'spotify_main_menu.py' file
- Type 'spot_repl()' and enter
- Choose from the following prompts (some require inputs and some don't)
- There is no need to use quotes when typing in an input.
- Type "9" to Quit the program.

********************
ABOUT THE FUNCTIONS:

Menu Item 1: This query finds the name of an artist based on a user input track name. (This is only based on my personal streaming history data and does not serve as a general Spotify artist search)

Menu Item 2: This query counts the amount of times a track appears in the database in descending order.

Menu Item 3: This query counts the amount of times an artist appears in the database in descending order.

Menu Item 4: This query extracts the track history from a user input start date and end date.

Menu Item 5: This query extracts the top 50 songs with high danceability in order to create a dance party playlist in descending order.

Menu Item 9: Quits the program.

************
OTHER NOTES:

Because the Python REPL features only 5 of 10 queries written for this dataset, there is a separate file containing all 10 SQL queries. Feel free to run them in the DB Browser for SQLite. All non-SQL statements are commented out, so it's ready to run.

***********************
CONFERENCE PROJECT ARC:

Before I reached this final product, my original idea was to work with APIs in the productivity software, Notion. In order to do that, I started learning JavaScript, HTML, and CSS; however, because I was having difficulty with grasping JavaScript and slowly losing time to complete the benchmarks of my conference project, I decided to scrap the Notion API idea and go back to the drawing board to find a more simple project to complete in a reasonable amount of time. I remember talking about how I applied to a Spotify internship and it stemmed into finding a multitude of files under the Spotipy (Spotify Python) library. I played around with the library for a while to test different features and code examples until I had to develop an informal proposal for my conference project.

In the end, I decided to find/download my personal Spotify data from my Spotify settings and create a program similar to the family tree assignment assigned earlier in the semester. I would create a csv files of my streaming history (thanks to some open source code credited at the bottom of the document) and create a Python REPL in order to extract particular information from my history using various SQL queries.

There are a few adjustments and improvements that I would've liked to include if there was more time for this project. I would've loved to include all of my developed queries into my REPL (and possibly more complex queries). In addition, if there was more time, I would've liked to integrate other open source code to actually create a dance party playlist into one's Spotify and have it as something they could use for their own parties. 

********
CREDITS:

Spotipy Library: https://spotipy.readthedocs.io/en/2.22.1/

Interacting w/ Spotify Streaming History + Spotify API Open Source Code: https://github.com/vlad-ds/spoty-records


** ~ Thank you for using the Spotify Streaming History Database! ~ **
