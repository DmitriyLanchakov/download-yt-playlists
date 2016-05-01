from __future__ import unicode_literals
import json
import youtube_dl
import logging

class Logger(object):
    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', filename='logger.txt', level=logging.DEBUG)
        self._logger = logging.getLogger('download_log')

    def debug(self, msg):
        pass

    def warning(self, msg):
        self._logger.warning(msg)

    def error(self, msg):
        self._logger.error(msg)

    def info(self, msg):
        self._logger.info(msg)


class Downloader(object):
    
    @staticmethod
    def hook(d):
        if d['status'] == 'finished':
            logger = Logger()
            logger.info('Done downloading, now converting %s' % d['filename'])
    
    def _get_playlists(self):
        with open('playlists.json') as data_file:
            return json.load(data_file)

    def run(self):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                # 'preferredquality': '192',
            }],
            'logger': Logger(),
            'progress_hooks': [Downloader.hook],
            'outtmpl': '~/Music/youtube-dl/%(playlist)s/%(title)s.%(ext)s',
            'sleep_interval': 10,
            'download_archive': 'downloaded_songs',
            'ignoreerrors': True
        }

        playlists = self._get_playlists()
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(list(playlists[name] for name in playlists))

if __name__ == '__main__':
    dwld = Downloader()
    dwld.run()