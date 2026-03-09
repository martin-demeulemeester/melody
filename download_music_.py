from __future__ import unicode_literals
import yt_dlp


# Try to find FFmpeg
ffmpeg_location = None
try:
    import imageio_ffmpeg
    ffmpeg_location = imageio_ffmpeg.get_ffmpeg_exe()
except ImportError:
    pass

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'opus',
        'preferredquality': '192',
    }],
    'prefer_ffmpeg': True,
    'keepvideo': False,
}

if ffmpeg_location:
    ydl_opts['ffmpeg_location'] = ffmpeg_location



def download_from_youtube(link):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print('done')



if __name__ == '__main__':
    download_from_youtube('https://youtu.be/l9MSAwb3YfY?si=1GfULdi7DCrAibg6')