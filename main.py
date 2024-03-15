import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
scope = "user-modify-playback-state"
client_id = "bb5798b2ae5149d19e35d3b9b3170534"  # Replace with your actual client ID
client_secret = "94f3d314f618497ab5b4efc49988f6df"  # Replace with your actual client secret
redirect_uri = "http://localhost:8888/callback"  # Replace with your actual redirect URI
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))


# Generate random heart rate
heart_rate = random.randint(60, 180)
print(heart_rate)

if heart_rate > 100:
    # High heart rate - play calming music
    desired_music_characteristics = "calm piano music"
else:
    # Low heart rate - play upbeat music
    desired_music_characteristics = "upbeat music"

# Use the Spotify API to search for music based on the desired characteristics
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))
results = sp.search(q=desired_music_characteristics, limit=1, type='track')

# Play the retrieved track
if results['tracks']['items']:
    track_uri = results['tracks']['items'][0]['uri']
    sp.start_playback(uris=[track_uri])




import requests

# Replace 'YOUR_ACCESS_TOKEN' with the actual access token obtained after the user completes the OAuth flow
headers = {
    'Authorization': 'Bearer ${token}',
}

# Make a GET request to the Spotify API to retrieve the currently playing track
response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers)

if response.status_code == 200:
    # Extract and analyze information about the currently playing track from the response JSON
    data = response.json()
    print(data)
else:
    print('Error fetching currently playing track:', response.text)



