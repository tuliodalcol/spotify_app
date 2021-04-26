import requests
import json
from tools import credentials as c

def get_tracks(playlist_id):
    '''Extracts tha tracks from a playlist'''
    headers = c.requests_headers()
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    r = requests.get(url, headers = headers)
    data = r.json()
    status = r.status_code
    if status == 200:
        return data
    else:
        raise Exception(f'status code: {status} | Reason: {r.reason} \n'
                        f'{data}')

class TracksData:
    def __init__(self, basic_info: dict()):
        #self.basic_info = basic_info
        self.id = basic_info['id']
        self.name = basic_info['name']
        self.playlist_data = get_tracks(self.id)
      
    def formatter(self):
        '''Returns a nested dic with track's info from a playlist'''
        
        data = dict()
        # Get basic playlist's info
        data['playlist_id'] = self.id
        data['playlist_name'] = self.name
        
        # get tracks info
        data['tracks'] = list()
        for dic_items in self.playlist_data['items']:
            
            temp = dict() 
            # get track's info
            temp['added_at'] = dic_items['added_at']   
            temp['track_name'] = dic_items['track']['name']
            temp['track_number'] = dic_items['track']['track_number']
            temp['track_id'] = dic_items['track']['id']
            temp['track_duration_seg'] = dic_items['track']['duration_ms']/1000
            # get album's info
            temp['album_name'] = dic_items['track']['album']['name']
            temp['album_id'] = dic_items['track']['album']['id']
            temp['album_release_date'] = dic_items['track']['album']['release_date']
            temp['album_total_tracks'] = dic_items['track']['album']['total_tracks']
               
            # Get artist's info
            temp['n_artists'] = len(dic_items['track']['artists'])
            temp['artists'] = list()
            for art in dic_items['track']['artists']:
                
                temp_artist = dict()
                temp_artist['artist_name'] =  art['name']
                temp_artist['artist_id'] = art['id']
                temp['artists'].append(temp_artist)
                
            data['tracks'].append(temp)
        self.data = data
        return self.data
        
    def save_to_local(self):
        '''Saves track's info from a playlist as .json in data/'''
        with open(f'data/playlistTracks_{self.name}.json', 'wt') as outfile:
            json.dump(self.data, outfile, indent=4, sort_keys=True)
 
    
