
import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "chinook.db")

#conn = sqlite3.connect('rpg_db.sqlite3')
conn = sqlite3.connect(DB_FILEPATH)
# h/t: https://kite.com/python/examples/3884/sqlite3-use-a-row-factory-to-access-values-by-column-name
conn.row_factory = sqlite3.Row

curs = conn.cursor()

query = """
select
    artists.ArtistId
    ,artists.Name
    ,count(distinct tracks.TrackId) as track_count
from tracks
join albums on albums.AlbumId = tracks.AlbumId
join artists on artists.ArtistId = albums.ArtistId
group by artists.ArtistId;
"""

#curs.execute(query)
results = curs.execute(query).fetchall()

breakpoint()
