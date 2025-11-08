import sys


jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'

def read_header(file_name, header_length):
    
    try:
        with open(file_name, 'rb') as f:
            return f.read(header_length)
    except Exception as e:
        print(f"Chyba při čtení souboru: {e}")
        return b''

def is_jpeg(file_name):
    header = read_header(file_name, len(jpeg_header))
    if header == jpeg_header:
        return True
    else:
        return False

def is_gif(file_name):
    header = read_header(file_name, 6)  # GIF hlavička má 6 bajtů
    if header == gif_header1 or header == gif_header2:
        return True
    else:
        return False

def is_png(file_name):
    header = read_header(file_name, len(png_header))
    if header == png_header:
        return True
    else:
        return False

def print_file_type(file_name):
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
        print_file_type(file_name)
    except Exception as e:
        print(f"Nastala chyba: {e}")