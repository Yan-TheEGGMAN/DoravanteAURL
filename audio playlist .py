from pytubefix import YouTube as youtube
from pytubefix import Playlist as playlist
from pytubefix.cli import on_progress
import os
import time

# Função que limpa o terminal, Windows ou Linux/Mac
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')



url = input("Inserir url: ")
global atual
atual = 0

pl = playlist(url)

#cria pasta para as musicas
pasta = os.path.join(r"C:\Users\Yan_k_rocha\Downloads", pl.title)
os.makedirs(pasta, exist_ok=True)

for video in pl.videos:
  
  atual += 1
  
  video = youtube(video.watch_url, on_progress_callback=on_progress)
  ys = video.streams.filter(only_audio=True) .order_by("abr")\
    .desc()\
    .first()
  
  print("Baixando atualmente: ", atual,"\n")
  print(video.title)

  ys.download(output_path=pasta)
  time.sleep(2)
  limpar_tela()



 #https://www.youtube.com/playlist?list=PLvNp0Boas7205K42TtDtdUCCrtkD-X0id
