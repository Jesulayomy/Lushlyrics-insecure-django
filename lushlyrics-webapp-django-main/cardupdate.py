import json
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
from urllib.request import urlopen
from youtube_search import YoutubeSearch


spot = 'https://open.spotify.com/playlist/'
PLAYLISTS = [
    [
        'Accidental',
        f'{spot}0zJ8hC8YJOcHYuk5nMPFm8?si=U6Kyom3XQ32reSuVgl2uhA',
        'PL59eqqQABruMQOPlUVcVsIid685ZdwDjf'
    ],
    [
        'TimePass',
        f'{spot}6gADLrLFK1kXgEEOsENi1c',
        'PL59eqqQABruMSx6VSy1hbkBhG4XwtgSuy'
    ],
    [
        'CHILLS',
        f'{spot}3zs3QOLX8bASY5oV2dmEQw',
        'PL59eqqQABruN3GyAPiPnQ6Jq-TngWjT-Y'
    ],
    [
        'Programming & Coding Music',
        f'{spot}6vWEpKDjVitlEDrOmLjIAj',
        'PL59eqqQABruNew5O0cRvomfbU6FI0RGyl'
    ],
    [
        'Spanish',
        f'{spot}75QJ1JeFaeSm0uH1znWxb0?si=Lt4kd-RARBu2TQz35RAQiQ',
        'PL59eqqQABruM3TLAGthvgW10c1R6omGwq'
    ]
]
client_credentials_manager = SpotifyClientCredentials(
    client_id='e5d66c188ef64dd89afa4d13f9555411',
    client_secret='d070988d7bd5479a9e0818fa23839544'
)
sp = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager
)


CONTAINER = []
for playlist in PLAYLISTS:
    Name, Link, playlistid = playlist
    playlistcard = []
    count = 0
    PlaylistLink = "http://www.youtube.com/watch_videos?video_ids="
    for i in (sp.playlist_tracks(Link)['items']):
        if count == 50:
            break
        try:
            song = i['track']['name'] + i['track']['artists'][0]['name']
            songdic = (YoutubeSearch(song, max_results=1).to_dict())[0]
            playlistcard.append(
                [
                    songdic['thumbnails'][0],
                    songdic['title'],
                    songdic['channel'],
                    songdic['id']
                ]
            )
            PlaylistLink += songdic['id'] + ','
        except Exception:
            continue
        count += 1

    req = urlopen(PlaylistLink)
    PlaylistLink = req.geturl()
    print(PlaylistLink)
    PlaylistId = PlaylistLink[PlaylistLink.find('list')+5:]

    CONTAINER.append([Name, playlistcard, playlistid])

json.dump(CONTAINER, open('card.json', 'w'), indent=6)
