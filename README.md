# Утилита для Шифрования Строк

Добро пожаловать в **Утилиту для Шифрования Строк**! Этот универсальный скрипт на Python позволяет шифровать текст из файла, используя различные методы кодирования. Независимо от того, нужно ли вам защитить данные или просто преобразовать текст для других целей, этот инструмент предоставляет простое решение.

## Возможности

- **Кодирование Base64**: Преобразуйте ваш текст в строку, закодированную в формате base64, что является распространенным методом кодирования двоичных данных в текстовом формате.
- **Шестнадцатеричное Кодирование**: Преобразуйте ваш текст в шестнадцатеричное представление, полезное для отладки и анализа данных.
- **Кодирование ROT13**: Примените шифр ROT13, простой шифр подстановки, который заменяет букву на 13-ю букву после нее в алфавите.
- **URL Кодирование**: Закодируйте ваш текст для безопасной передачи в URL, преобразуя специальные символы в формат, который может быть передан через Интернет.
- **Хеширование MD5**: Создайте MD5-хеш вашего текста, широко используемую криптографическую хеш-функцию, которая производит 32-символьное шестнадцатеричное число.

## Использование

Для использования этого скрипта необходимо указать входной файл, выходной файл и метод шифрования, который вы хотите применить. Скрипт прочитает входной файл, зашифрует каждую строку с использованием выбранного метода и запишет зашифрованный текст в выходной файл.

### Аргументы Командной Строки

- `-i`, `--input`: Путь к входному текстовому файлу.
- `-o`, `--output`: Путь к выходному текстовому файлу.
- `-e`, `--encryption`: Метод шифрования для использования. Выберите из `base64`, `hex`, `rot13`, `url` или `md5`.

### Пример

```bash
python kencoder.py -i input.txt -o output.txt -e base64
```

Эта команда прочитает `input.txt`, закодирует каждую строку с использованием Base64 и сохранит результат в `output.txt`.

## Обработка Ошибок

Скрипт включает базовую обработку ошибок для управления проблемами доступа к файлам и другими исключениями, обеспечивая плавный пользовательский опыт.

## Начало Работы

Клонируйте репозиторий и начните шифровать ваши текстовые файлы с легкостью. Приветствуются вклады и отзывы!

---

Эта утилита идеально подходит для разработчиков, аналитиков данных и всех, кому нужен быстрый и надежный способ шифрования текстовых данных. Наслаждайтесь гибкостью и мощью нескольких методов шифрования в одном простом инструменте!
