import time
import os
import lyricsgenius as lg


genius = lg.Genius("BoI01P-rwaozXg13Tz2I_YqFayWUfjdyKNqHxBtytaKMkzdHxYhRJKPzQ41NEntR")


artist = genius.search_artist('Chief Keef', max_songs=1)
page = 1
songs = []
while page:
    request = genius.artist_songs(artist._id,
                                  sort='popularity',
                                  per_page=50,
                                  page=page,
                                  )
    songs.extend(request['songs'])
    page = request['next_page']
least_popular_song = genius.search_song(songs[-1]['title'], artist.name)
print(least_popular_song.lyrics)

