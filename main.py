from __future__ import unicode_literals
import yt_dlp


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': '137+140',
    'outtmpl': r'd:\youtubedown' + '/%(title)s.%(ext)s',
    # 'postprocessors': [{
    #     'key': 'FFmpegExtractAudio',
    #     'preferredcodec': 'm4a',
    #     'preferredquality': '137',
    # }],
    # 'logger': MyLogger(),
    # 'progress_hooks': [my_hook],
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=Pqf6PG1RqWw'])
