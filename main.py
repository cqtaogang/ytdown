from __future__ import unicode_literals
import yt_dlp


ydl_opts = {
    'format': '141/137'
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=Pqf6PG1RqWw'])
