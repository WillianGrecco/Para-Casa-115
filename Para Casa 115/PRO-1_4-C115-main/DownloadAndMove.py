import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "DIGITE O CAMINHO DA PASTA DE DOWNLOAD (USE " / ") no VSC"
# to_dir = "DIGITE A PASTA DE CAMINHO DE DESTINO (USE " / ") no VSC"

from_dir = "/Users/Gamer/Downloads"
to_dir = "/Users/Gamer/Downloads/Arquivos_baixados"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Classe Gerenciadora de Eventos

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name, extension = os.path.splitext(event.src_path)
        
        time.sleep(1)
        
        for key, value in dir_tree.items():
            time.sleep(1)
            
            if extension in value:
                file_name = os.path.basename(event.src_path)
                
                path1 = from_dir + "/" + file_name
                path2 = to_dir + "/" + key
                path3 = path2 + "/" + file_name
                
                if os.path.exists(path2):
                    if os.path.exists(path3):
                        new_name, new_extension = os.path.splitext(file_name)
                        new_file_name = new_name + str(random.randint(0, 999)) + new_extension
                        
                        path4 = path2 + "/" + new_file_name
                        
                        print("Movendo arquivo novo...")
                        shutil.move(path1, path4)
                    else: 
                        print("Movendo...")
                        shutil.move(path1, path3)
                else:
                    print("Criando a pasta...")
                    os.makedirs(path2)
                    print("Movendo...")
                    shutil.move(path1, path3)


# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileMovementHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicie o Observer
observer.start()


while True:
    time.sleep(2)
    print("executando...")
