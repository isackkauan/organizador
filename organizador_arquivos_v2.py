import sys
import os
import shutil

sys.stdout.reconfigure(encoding='utf-8')

environmental = os.environ
username = environmental['USERNAME']

downloads_path = rf'C:\Users\{username}\Downloads'
arquivos_path = rf'C:\Users\{username}\OneDrive\arquivos'

for file in os.listdir(downloads_path):
    filename, file_extension = os.path.splitext(file)
    file_path = f'{downloads_path}\{file}'
    num = 1

    # Para pastas
    if file_extension == '':
        folder = f'{arquivos_path}\PASTAS'
        
    # Para arquivos diversos
    else:    
        folder = f'{arquivos_path}\{file_extension[1:].upper()}'
    
    # Criar pasta
    if not os.path.isdir(folder):
        os.mkdir(folder)

    # Lidar com arquivos/pastas de nomes iguais
    while file in os.listdir(folder):
            
        file = f"{filename} ({num}){file_extension}"
        new_file_path = f'{downloads_path}\{file}'
        os.rename(file_path, new_file_path)
        file_path = new_file_path
        num = num + 1

    # Mova arquivo/pasta pra pasta determinada
    shutil.move(f'{file_path}', f'{folder}')