import os
import subprocess
import sys

# Проверка и установка библиотеки colorama
try:
    from colorama import init, Fore, Style
except ImportError:
    print("Библиотека 'colorama' не найдена. Устанавливаю...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
        print("Библиотека 'colorama' успешно установлена.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка установки 'colorama': {e}")
    from colorama import init, Fore, Style

# Инициализация colorama для работы цвета в консоли
init(autoreset=True)

# Список поддерживаемых расширений для чтения текстовых файлов
SUPPORTED_EXTENSIONS = ['.txt', '.ini', '.xml', '.html', '.json', '.csv']

# Словарь с сообщениями для вывода на разных языках
MESSAGES = {
    "RU": {
        "welcome": "=== Поиск и замена текста в файлах ===\n",
        "enter_directory": "Введите путь к директории: ",
        "enter_search_text": "Введите текст для поиска: ",
        "enter_replace_text": "Введите текст для замены: ",
        "enter_extensions": "Введите расширения файлов через запятую (например, .txt,.py) или нажмите Enter для обработки всех файлов: ",
        "processing_file": "Обрабатываю файл: ",
        "file_modified": "[ИЗМЕНЁН] ",
        "error_in_file": "[ОШИБКА] ",
        "result_title": "\n=== РЕЗУЛЬТАТЫ ===",
        "total_files": "Обработано файлов: ",
        "modified_files": "Файлов с заменой: ",
        "errors_written": "\nОшибки записаны в 'error_log.txt', если они возникли.",
        "modified_files_list": "\nСписок изменённых файлов:",
        "no_files_modified": "Нет файлов с заменами.",
        "directory_not_found": "Указанная директория не найдена. Проверьте путь.",
        "exit_prompt": "\nНажмите Enter, чтобы выйти..."
    },
    "EN": {
        "welcome": "=== Search and Replace Text in Files ===\n",
        "enter_directory": "Enter the directory path: ",
        "enter_search_text": "Enter the text to search for: ",
        "enter_replace_text": "Enter the text to replace with: ",
        "enter_extensions": "Enter file extensions separated by commas (e.g., .txt,.py) or press Enter to process all files: ",
        "processing_file": "Processing file: ",
        "file_modified": "[MODIFIED] ",
        "error_in_file": "[ERROR] ",
        "result_title": "\n=== RESULTS ===",
        "total_files": "Files processed: ",
        "modified_files": "Files modified: ",
        "errors_written": "\nErrors logged to 'error_log.txt' if any.",
        "modified_files_list": "\nList of modified files:",
        "no_files_modified": "No files were modified.",
        "directory_not_found": "The specified directory was not found. Please check the path.",
        "exit_prompt": "\nPress Enter to exit..."
    }
}

# Функция для получения языка через цифровые кнопки
def get_language():
    while True:
        print(Fore.BLUE + "Choose language:")
        print(Fore.YELLOW + "1 - Русский (RU)")
        print(Fore.YELLOW + "2 - English (EN)")

        choice = input(Fore.CYAN + "Enter 1 or 2: ").strip()
        
        if choice == "1":
            return "RU"
        elif choice == "2":
            return "EN"
        else:
            print(Fore.RED + "Неверный ввод, попробуйте снова.")

def find_and_replace_in_files(directory, search_text, replace_text, file_extensions=None, error_log_file="error_log.txt", lang="EN"):
    """
    Функция для поиска и замены текста в файлах в указанной директории и подпапках.

    :param directory: Путь к директории.
    :param search_text: Текст для поиска.
    :param replace_text: Текст для замены.
    :param file_extensions: Список расширений файлов для обработки (например, ['.txt', '.py']). Если None, обрабатываются все файлы.
    :param error_log_file: Путь к файлу для записи ошибок.
    :param lang: Язык сообщений ("RU" или "EN").
    :return: Кортеж (общее количество файлов, количество измененных файлов, список изменённых файлов)
    """
    total_files = 0
    modified_files = 0
    modified_files_list = []

    # Открываем файл для записи ошибок
    with open(error_log_file, 'w', encoding='utf-8') as error_log:
        for root, _, files in os.walk(directory):
            for file_name in files:
                if file_extensions and not any(file_name.endswith(ext) for ext in file_extensions):
                    continue

                total_files += 1
                file_path = os.path.join(root, file_name)
                print(Fore.YELLOW + MESSAGES[lang]["processing_file"] + file_path)

                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()

                    if search_text in content:
                        updated_content = content.replace(search_text, replace_text)
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(updated_content)
                        modified_files += 1
                        modified_files_list.append(file_path)
                        print(Fore.GREEN + MESSAGES[lang]["file_modified"] + file_path)
                except Exception as e:
                    # Логируем ошибки в файл
                    error_log.write(f"{MESSAGES[lang]['error_in_file']} {file_path}: {e}\n")

    return total_files, modified_files, modified_files_list

if __name__ == "__main__":
    lang = get_language()  # Получаем язык через цифровые кнопки

    print(Fore.CYAN + Style.BRIGHT + MESSAGES[lang]["welcome"])

    directory_path = input(Fore.BLUE + MESSAGES[lang]["enter_directory"])
    text_to_search = input(Fore.BLUE + MESSAGES[lang]["enter_search_text"])
    text_to_replace = input(Fore.BLUE + MESSAGES[lang]["enter_replace_text"])
    extensions_input = input(Fore.BLUE + MESSAGES[lang]["enter_extensions"])

    if extensions_input.strip():
        file_types = [ext.strip() for ext in extensions_input.split(',')]
    else:
        file_types = SUPPORTED_EXTENSIONS  # по умолчанию обрабатываем текстовые файлы

    if os.path.isdir(directory_path):
        total, modified, modified_files = find_and_replace_in_files(directory_path, text_to_search, text_to_replace, file_types, lang=lang)

        print(Fore.CYAN + MESSAGES[lang]["result_title"])
        print(Fore.YELLOW + f"{MESSAGES[lang]['total_files']} {total}")
        print(Fore.GREEN + f"{MESSAGES[lang]['modified_files']} {modified}")
        print(Fore.MAGENTA + MESSAGES[lang]["errors_written"])

        # Выводим список изменённых файлов
        if modified_files:
            print(Fore.GREEN + MESSAGES[lang]["modified_files_list"])
            for file in modified_files:
                print(Fore.GREEN + f"- {file}")
        else:
            print(Fore.YELLOW + MESSAGES[lang]["no_files_modified"])
    else:
        print(Fore.RED + MESSAGES[lang]["directory_not_found"])

    input(Fore.MAGENTA + MESSAGES[lang]["exit_prompt"])
