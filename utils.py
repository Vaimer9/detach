from typing import Tuple
import os

def my_hook(d):
    if d['status'] == 'finished':
        print(f"-------{ d['filename'] } was finished downloading-------")
    elif d['status'] == 'downloading':
        print(f"Downloading {d['filename']}: {d['_percent_str']}% complete")


def getCredentialsfromEnv() -> Tuple[str, str]:
    if "SPOTIFY_KEY" in os.environ and "SPOTIFY_SECRET" in os.environ:
        return (os.environ["SPOTIFY_KEY"], os.environ["SPOTIFY_SECRET"])
    else:
        client_id = input('Enter client ID: ')
        client_secret = input('Enter Client Secret: ')
        return (client_id, client_secret)
