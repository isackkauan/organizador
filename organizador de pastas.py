import os
import shutil

documents_path = r'C:\Users\isack\OneDrive\Documentos'

# Documentação
Documentação = [
    'DOC',
    'DOCX',
    'ODT',
    'PDF',
    'RTF',
    'TXT'
]

# Planilhas
Planilhas = [
    'XLS', 'XLSX', 'ODS'
]

# Apresentações
Apresentações = [
    'PPT', 'PPTX', 'ODP'
]

# Imagens
Imagens = [
    'JPG', 'JPEG', 'PNG', 'GIF', 'BMP', 'TIFF', 'TIF', 'SVG', 'WEBP'
]

# Áudio
Áudio = [
    'MP3', 'WAV', 'AAC', 'FLAC', 'OGG'
]

# Vídeo
Vídeo = [
    'MP4', 'AVI', 'MKV', 'MOV', 'WMV', 'FLV'
]

# Compactação
Compactação = [
    'ZIP', 'RAR', 'TAR', 'GZ', '7Z'
]

# Código-Fonte
Código_Fonte = [
    'PY', 'JAVA', 'C', 'CPP', 'JS', 'HTML', 'CSS', 'PHP'
]

# Outros
Outros = [
    'EXE', 'DLL', 'ISO', 'APK', 'BIN', 'CSV', 'JSON', 'XML', 'YML', 'YAML', 'MDP'
]

folder_extension = (
    Documentação + Planilhas + Apresentações + Imagens + Áudio + Vídeo + Compactação + Código_Fonte + Outros
)
# Todas as extensões juntas
all_category = {
    'Documentação': Documentação,
    'Planilhas': Planilhas,
    'Apresentações': Apresentações,
    'Imagens': Imagens,
    'Áudio': Áudio,
    'Vídeo': Vídeo ,
    'Compactação': Compactação,
    'Código_Fonte': Código_Fonte,
    'Outros': Outros
}

for category in all_category:

    folder_path = f'{documents_path}\{category}'
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)

    for folder in os.listdir(documents_path):
        if folder in all_category[f'{category}']:
            shutil.move(f'{documents_path}\{folder}', folder_path)
