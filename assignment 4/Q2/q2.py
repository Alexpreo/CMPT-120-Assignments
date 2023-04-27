def get_songs_by_artist(artist):
    songs = []
    f = open('spotify.txt', 'r', encoding='utf-8')
    for line in f:
        line = line.strip().split(',')
        if line[4] == artist:
            song = {'acousticness': float(line[0]), 'danceability': float(line[1]),
                    'duration': int(line[2]), 'title': line[3], 'artist': line[4]}
            songs.append(song)
    return songs

def bubble_sort(songs):
    n = len(songs)
    for i in range(n):
        for j in range(0, n-i-1):
            if songs[j]['danceability'] < songs[j+1]['danceability']:
                songs[j], songs[j+1] = songs[j+1], songs[j]
    return songs

while True:

    artist_name = input()
    artist_name_lower = artist_name.lower()
    artist_name_final = artist_name_lower.title()

    songs_by_artist = get_songs_by_artist(artist_name_final)
    songs_sorted_by_danceability = bubble_sort(songs_by_artist)
    
    if len(songs_by_artist) > 0:

        highest_danceability_song = songs_sorted_by_danceability[0]

        print("{}\n{}".format(highest_danceability_song['title'], highest_danceability_song['danceability']))
        break
    else:
        break
