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
        ydl.download(link)
    print('done')



if __name__ == '__main__':
    liste = ['https://youtu.be/l9MSAwb3YfY?si=1GfULdi7DCrAibg6',
             'https://youtu.be/_LUFMHvvNt4?si=XUXFrgPc0NdKjlpG',
             'https://youtu.be/atgjKEgSqSU?si=1UC0ISLEoaF7rQfz',
             'https://youtu.be/6pV-Qm0o6Rg?si=ss9nKmCIIKaTJbIg',
             'https://youtu.be/7DjspOrDTUk?si=JQwg_v4O5x7NZ5Yf',
             'https://youtu.be/guN5p5ALnjE?si=Xtuf24R4lAA2Y0Vk']
    download_from_youtube(liste)