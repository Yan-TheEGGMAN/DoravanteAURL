from pytubefix import YouTube as youtube
from pytubefix.cli import on_progress



url = input("Inserir url: ")

yt = youtube(url, on_progress_callback=on_progress)
ys = yt.streams.get_highest_resolution()
print(yt.title)
ys.download(output_path= r"C:\Users\Yan_k_rocha\Downloads")