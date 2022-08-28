"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding = 'utf-8') as f:
        text = f.read()
    print(f"Длина строки {len(text)} символов.")
    print()

    text_modified = text.split()
    print(f"Количество слов в тексте: {len(text_modified)}")
    print()

    text_replaced = text.replace('.', '!')
    print(f"Текст после замены точек на восклицательные знаки")
    print(text_replaced)

if __name__ == "__main__":
    main()
    