import requests
import json
import sys
from tools import credentials as c

def get_playlists():
    ''' Extract user's playlists info'''
    headers = c.requests_headers()
    url = 'https://api.spotify.com/v1/me/playlists'
    r = requests.get(url, headers = headers)
    data = r.json()
    status = r.status_code
    if status == 200:
        return data
    else:
        raise Exception(f'status code: {status} | Reason: {r.reason} \n'
                        f'{data}')

class Playlists:
    def __init__(self):
        self.data = get_playlists()
    
    def formatter(self):
        # Data validation
        while True:
            if len(self.data) == 0:
                print('Playlists has returned no data')
                sys.exit()
            else:
                break
    
        try:
            # Saves playlist name & ID to a list of dict
            self.playlists_info = list()
            for i,dic in enumerate(self.data['items']):
                print(dic['name'])
                temp_dic = dict()    
                temp_dic['id'] = dic['id']
                temp_dic['name'] = dic['name']
                self.playlists_info.append(temp_dic)      
        except:
            print('Not able to get playlist name & ID from API request')

    def save_to_local(self):
        '''Saves Playlist's NAME & ID to .json in ../data/'''
        with open('data/playlists_info.json', 'wt') as outfile:
            json.dump(self.playlists_info, outfile, indent=2, sort_keys=True)

