from __future__ import unicode_literals
import yt_dlp


url = ['https://www.youtube.com/shorts/ySBnYBLkaWA']

# url = ['https://www.bilibili.com/video/BV1Yv4y1g78C/?spm_id_from=333.788.recommend_more_video.-1&vd_source=2f8c1354ee224a9eb8d8bd87a032970b']
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
    # 'format': '137+140',
    # 'format': 'best',
    'listformats': True,
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
    ydl.download(url)
