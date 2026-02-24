from pytubefix import YouTube as youtube
from pytubefix.cli import on_progress
import os

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

url = input("Inserir url: ")

yt = youtube(url, on_progress_callback=on_progress)
ys = yt.streams.filter(only_audio=True) .order_by("abr")\
    .desc()\
    .first()
print(yt.title)
ys.download(output_path=downloads_path)