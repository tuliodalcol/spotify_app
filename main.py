import json
from tools import playlists as p
from tools import tracks_data as t

if __name__ == '__main__':

    playlists = p.Playlists()
    playlists.formatter()
    playlists.save_to_local()

    # open playlist's info
    with open('data/playlists_info.json') as f:
        playlists_info = json.load(f)
    
    #info = playlists_info[0]    
    # Extract track's info for all playlists
    for info in playlists_info:
    	tracks = t.TracksData(info)
    	tracks.formatter()
    	tracks.save_to_local()


