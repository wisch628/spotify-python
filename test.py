import requests
import os

CLIENT_ID=os.environ.get('CLIENT_ID')
CLIENT_SECRET=os.environ.get('CLIENT_SECRET')
AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})
auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']
BASE_URL = 'https://api.spotify.com/v1/'
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}
artist = '0TnOYISbd1XYRBk9myaseg'
r = requests.get(BASE_URL + 'artists/' + artist, headers=headers)
r = r.json()
print(r['name'])