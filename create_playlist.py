import json
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests
import youtube_dl

from secrets import spotify_user_id, spotify_token

class CreatePlaylist:
    def __init__(self):
        self.user_id=spotify_user_id
        self.spotify_token=spotify_token

    def get_youtube_client(self):
        pass

    def get_liked_videos(self):
        pass

    def create_playlist(self):
        request_body = json.dumps({
            "name": "YouTube bangers",
            "description": "All videos from 'bængers'.",
            "public": False
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
        response = requests.post(
            query,
            data = request_body,
            headers = {
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(spotify_token)
            }
        )

        response_json = response.json()

        #playlist id
        return response_json["id"]

    def get_spotify_url(self, song_name, artist):
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )

        
    
    
    def add_song_to_playlist(self):
        pass