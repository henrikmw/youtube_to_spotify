import json
import requests
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
            "name": "Bængere fra YouTube",
            "description": "All videos from 'bængers'.",
            "public": False
        })

        query = "https://api.spotify.com/v1/users/{user_id}/playlists".format()
        response = requests.post(
            query,
            data = request_body,
            headers = {
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(spotify_token)
            }
        )

        response_json = response.json()

        return response_json["id"]

    def get_spotify_url(self):
        pass

    def add_song_to_playlist(self):
        pass