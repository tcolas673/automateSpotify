

# Step 1: Log Into Youtube
# Step 2: Grab Our Liked Videos
# Step 3: Create A New Playlist
# Step 4: Search For the Song
# Step 5: Add this song into the new Spotify Playlist

import json
import requests
from secrets import spotify_user_id, spotify_token


class CreatePlaylist:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token

    # Step 1: Log Into Youtube
    def get_youtube_client(self):
        pass
    # Step 2: Grab Our Liked Videos
    def get_liked_vieos(self):
        pass
    # Step 3: Create A New Playlist
    def create_playlist(self):
        requrest_body = json.dumps({
            "name": "Youtube Liked Vids",
            "description": "All Liked Youtube Videos",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
        
    # Step 4: Search For the Song
    def get_spotify_uri(self, song_name, artist):
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
        response = requests.get(
            query,
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()
        songs = response_json["tracks"]["items"]
        #only use the first song
        uri =songs[0]["uri"]
        return uri
        
    # Step 5: Add this song into the new Spotify Playlist
    def add_song_to_playlist(self):
        pass