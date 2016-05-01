# Download the audio from your youtube playlists!
This is a script that uses the amazing [youtube-dl](https://github.com/rg3/youtube-dl) utility. It reads a .json file where you specify the playlists you want downloaded and proceeds to download the audio in .mp3 format. 

Errors, warning and other informations are written into a logger. 
Also, a file named ```downloaded_songs``` is created and keeps track of the youtube IDs of the videos you have converted to audio. It will not attempt to download these same files a second time. 

The .json file needs to have the following format:
```
{
    "playlist_name1": "playlist_url1",
    "playlist_name2": "playlist_url2"
}
```

To run the script, use:
```sh
python dwl_pl.py
```

One important dependency is that you need to install ```ffmpeg``` on your system. 
