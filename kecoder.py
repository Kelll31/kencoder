import argparse
import base64
import urllib.parse
import hashlib

def encode_base64(text):
    return base64.b64encode(text.encode()).decode()

def encode_hex(text):
    return text.encode().hex()

def encode_rot13(text):
    return text.encode('rot_13')

def encode_url(text):
    return urllib.parse.quote(text)

def encode_md5(text):
    return hashlib.md5(text.encode()).hexdigest()

def main():
    parser = argparse.ArgumentParser(description='Шифрование строк текстового файла с использованием различных методов.')
    parser.add_argument('-i', '--input', required=True, help='Путь к входному текстовому файлу.')
    parser.add_argument('-o', '--output', required=True, help='Путь к выходному текстовому файлу.')
    parser.add_argument('-e', '--encryption', required=True, choices=['base64', 'hex', 'rot13', 'url', 'md5'], help='Метод шифрования для использования.')

    args = parser.parse_args()

    # Выбор функции шифрования на основе аргумента
    if args.encryption == 'base64':
        encode_function = encode_base64
    elif args.encryption == 'hex':
        encode_function = encode_hex
    elif args.encryption == 'rot13':
        encode_function = encode_rot13
    elif args.encryption == 'url':
        encode_function = encode_url
    elif args.encryption == 'md5':
        encode_function = encode_md5

    try:
        with open(args.input, 'r', encoding='utf-8') as infile, open(args.output, 'w', encoding='utf-8') as outfile:
            for line in infile:
                encrypted_line = encode_function(line.strip())
                outfile.write(encrypted_line + '\n')
        print(f"Файл успешно зашифрован и сохранен в {args.output}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    main()