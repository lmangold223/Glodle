import time
import os
import lyricsgenius as lg
import csv
import random

genius = lg.Genius("BoI01P-rwaozXg13Tz2I_YqFayWUfjdyKNqHxBtytaKMkzdHxYhRJKPzQ41NEntR")

albumsWanted = ["Finally Rich", "Finally Rich(Deluxe)", "Back from the dead", "Almighty So", "Big Gucci Sosa", "Back from the dead 2", "The Leek vol 1", "The Leek vol 2", "Bang 3", "Bang 3 pt 2", "Feed the streets", "Finally Rollin 2", "Nobody 2", "thot breaker", "The w", "Dedication", "the leek vol 4", "the leek vol 5", "the glofiles pt1", "the glofiles pt2", "Mansion Musick", "Back from the dead 3", "the leek vol 6", "the leek vol 7", "glotoven", "camp glotiggy", "the leek vol 8", "the glofiles pt3", "the glofiles pt4", "4nem", "dirty nachos", "almighty so 2" ]




#retrieves chief keef's entire discography and stores it in a csv file
def get_songs():

    albums_release_dict = {}
    album_tracklist_dict = {}
    album_art_dict = {}

    for album in albumsWanted:
        as_dict = genius.search_album(album, "Chief Keef").to_dict()
        print(as_dict)
        albums_release_dict[album] = as_dict['release_date_components'] 
        album_art_dict[album] = as_dict['cover_art_url']

        tracklist = []

        for track in as_dict['tracks']:
            tracklist.append(track['song']['full_title'].replace("\xa0", ""))
            album_tracklist_dict[album] = tracklist
            
    
    return albums_release_dict, album_tracklist_dict, album_art_dict


with open('website/songs.csv', 'w', newline='', encoding= "UTF-8") as csvfile:
    fieldnames = ['Album', 'Year', 'Cover', 'Tracklist']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    albums_release_dict, album_tracklist_dict, album_art_dict = get_songs()
    
    for album in albumsWanted:
        writer.writerow({'Album': album, 'Year': albums_release_dict[album], 'Cover': album_art_dict[album], 'Tracklist': album_tracklist_dict[album]})
        
    print("done")