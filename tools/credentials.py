def requests_headers():
    ''' Set API get request headers'''
    f = open('token.txt', 'r')
    
    TOKEN = f.read().splitlines()[0]
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {TOKEN}'
    }
    return headers

