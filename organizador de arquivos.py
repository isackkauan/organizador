import os
import shutil

environmental = os.environ
username = environmental['USERNAME']
downloads_path = rf'C:\Users\{username}\Downloads'
arquivos_path = rf'C:\Users\{username}\OneDrive\arquivos'

for file in os.listdir(downloads_path):
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension[1:]

    #se file for um folder, pular loop
    if file_extension == '':
        continue 

    #criar pasta caso não exista
    folder = f'{arquivos_path}\{file_extension.upper()}'
    if not os.path.isdir(folder):
        os.mkdir(folder)
    
    #mova arquivo pra pasta
    shutil.move(f'{downloads_path}\{file}', f'{folder}')