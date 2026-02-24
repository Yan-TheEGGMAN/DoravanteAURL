from pytubefix import YouTube as youtube
from pytubefix.cli import on_progress
import os
import time
import re

def nome_seguro(nome):
    return re.sub(r'[\\/*?:"<>|]', "", nome)

url = input("Inserir url: ")

yt = youtube(url, on_progress_callback=on_progress)

titulo = nome_seguro(yt.title)

# Cria pasta temporária
os.makedirs("temp", exist_ok=True)

#baixa o video
video = yt.streams.filter(
    adaptive=True,
    only_video=True,
    file_extension="mp4"
).order_by("resolution").desc().first()


#Baixa o audio
audio = yt.streams.filter(
    adaptive=True,
    only_audio=True
).order_by("abr").desc().first()

print("Baixando vídeo...")
video_file = video.download("temp")

print("Baixando áudio...")
audio_file = audio.download("temp")

output_path = r"C:\Users\Yan_k_rocha\Downloads"
output_file = os.path.join(output_path, f"{titulo}.mp4")

print("Unindo vídeo + áudio...")

os.system(
    f'ffmpeg -i "{video_file}" -i "{audio_file}" -c copy "{output_file}"'
)

# Remove arquivos temporários
os.remove(video_file)
os.remove(audio_file)
os.rmdir("temp")

print("Download concluído ✅")

#https://www.youtube.com/watch?v=QhiNklwDo1Y&t=399s