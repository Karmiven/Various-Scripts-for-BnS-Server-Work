import os
import subprocess
import sys

# Скрипт анализирует базы данных SQL Server, проверяя таблицы и колонки на наличие данных, с сохранением результатов в файл и поддержкой цветового вывода и выбора языка.
# Скрипт для анализа баз данных SQL Server, выполнения запросов по всем таблицам и записи результатов в файл.
# Скрипт подключается к серверу SQL Server с использованием библиотеки pyodbc и осуществляет анализ всех баз данных, таблиц и колонок.
# Для каждой базы данных проверяются таблицы и колонки на наличие данных. Исключаются системные таблицы и колонки.
# Результаты анализа отображаются в консоли с использованием цветового форматирования через библиотеку colorama.
# Итоги анализа сохраняются в файл analysis_results.txt.
# Если библиотеки pyodbc или colorama отсутствуют, они автоматически устанавливаются перед выполнением скрипта.
# Скрипт поддерживает выбор языка сообщений (русский или английский).

# The script analyzes SQL Server databases, checks tables and columns for data, saves the results to a file, and supports color-coded output and language selection.
# This script analyzes SQL Server databases, querying all tables and logging results to a file.
# It connects to the SQL Server using the pyodbc library and processes all databases, tables, and columns.
# Each database is analyzed to identify tables and columns containing data. System tables and columns are excluded.
# The results are displayed in the console with color formatting using the colorama library.
# The analysis summary is saved to the analysis_results.txt file.
# If pyodbc or colorama is not installed, the script automatically installs them before execution.
# It also supports language selection (Russian or English).

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

# Проверка и установка библиотеки pyodbc
try:
    import pyodbc
except ImportError:
    print("Библиотека 'pyodbc' не найдена. Устанавливаю...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyodbc"])
    print("Библиотека 'pyodbc' успешно установлена.")
    import pyodbc

# Инициализация colorama для работы с цветами в консоли
init(autoreset=True)

# Конфигурация подключения
server = 'localhost'  # Замените на адрес вашего сервера
user = 'SA'
password = 'FSmElsXuj3ls8Fq'

# Выбор языка
def choose_language():
    print(Fore.BLUE + "Choose language:")
    print(Fore.YELLOW + "1 - Русский (RU)")
    print(Fore.YELLOW + "2 - English (EN)")

    choice = input(Fore.CYAN + "Enter your choice (1 or 2): ").strip()

    if choice == '1':
        return 'RU'
    elif choice == '2':
        return 'EN'
    else:
        print(Fore.RED + "Invalid choice. Defaulting to English.")
        return 'EN'

# Переводы для сообщений
def get_translations(language):
    if language == 'RU':
        return {
            'no_databases': "Нет баз данных для анализа.",
            'no_tables_or_columns': "Нет таблиц или колонок в базе данных: {0}",
            'database_analysis': "Анализ базы данных: {0}",
            'no_records_found': "Нет записей в базе данных: {0}, таблице: {1}, колонке: {2}",
            'records_found': "Записи найдены в базе данных: {0}, таблице: {1}, колонке: {2}",
            'analysis_results_saved': "Результаты сохранены в файл 'analysis_results.txt'.",
            'final_report': "\nИтоги анализа:",
            'processed_databases': "Обработано баз данных: {0}",
            'processed_tables': "Обработано таблиц: {0}",
            'databases_with_records': "Баз с записями: {0}",
            'tables_with_records': "Таблиц с записями: {0}",
            'error': "Произошла ошибка: {0}",
            'press_enter': "\nНажмите Enter, чтобы выйти...",
            'query_log': "Выполняется запрос: {0} в базе данных: {1}, таблице: {2}, колонке: {3}, тип данных: {4}"
        }
    else:
        return {
            'no_databases': "No databases for analysis.",
            'no_tables_or_columns': "No tables or columns in database: {0}",
            'database_analysis': "Analyzing database: {0}",
            'no_records_found': "No records found in database: {0}, table: {1}, column: {2}",
            'records_found': "Records found in database: {0}, table: {1}, column: {2}",
            'analysis_results_saved': "Results saved to 'analysis_results.txt'.",
            'final_report': "\nAnalysis Results:",
            'processed_databases': "Processed databases: {0}",
            'processed_tables': "Processed tables: {0}",
            'databases_with_records': "Databases with records: {0}",
            'tables_with_records': "Tables with records: {0}",
            'error': "An error occurred: {0}",
            'press_enter': "\nPress Enter to exit...",
            'query_log': "Executing query: {0} in database: {1}, table: {2}, column: {3}, data type: {4}"
        }

# Подключение к серверу SQL Server
def connect_to_server(server, user, password, database=None):
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};UID={user};PWD={password}'
    if database:
        connection_string += f';DATABASE={database}'
    return pyodbc.connect(connection_string)

# Проверка наличия таблицы с учетом схемы
def check_table_exists(cursor, schema, table_name):
    cursor.execute(f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{schema}' AND TABLE_NAME = '{table_name}'")
    return cursor.fetchone()[0] > 0

# Проверка наличия колонки
def check_column_exists(cursor, schema, table_name, column_name):
    cursor.execute(f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '{schema}' AND TABLE_NAME = '{table_name}' AND COLUMN_NAME = '{column_name}'")
    return cursor.fetchone()[0] > 0

# Обработчик для имен колонок с зарезервированными словами
def escape_reserved_keyword(column_name):
    return f"[{column_name}]"

# Анализ всех баз данных, таблиц и колонок
def analyze_databases_for_records(language):
    translations = get_translations(language)
    results = []
    total_databases = 0
    total_tables = 0
    databases_with_records = 0
    tables_with_records = 0

    try:
        # Подключаемся к серверу без указания базы данных, чтобы получить список баз
        conn = connect_to_server(server, user, password)
        cursor = conn.cursor()

        # Получение списка всех баз данных
        cursor.execute("SELECT name FROM sys.databases WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb')")
        databases = cursor.fetchall()

        if not databases:
            results.append(Fore.YELLOW + translations['no_databases'])
        
        # Перебираем все базы данных
        for database in databases:
            db_name = database[0]
            results.append(Fore.CYAN + translations['database_analysis'].format(db_name))
            print(Fore.CYAN + translations['database_analysis'].format(db_name))
            total_databases += 1
            conn_db = connect_to_server(server, user, password, database=db_name)
            cursor_db = conn_db.cursor()

            # Получение всех таблиц и их колонок с указанием типов данных
            cursor_db.execute("""
                SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, DATA_TYPE
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_NAME NOT LIKE 'sys%' AND TABLE_NAME NOT LIKE 'queue%'
            """)
            columns = cursor_db.fetchall()

            if not columns:
                results.append(Fore.YELLOW + translations['no_tables_or_columns'].format(db_name))
            
            # Перебираем таблицы и колонки
            database_has_records = False  # Для подсчета, если в базе есть хотя бы одна таблица с записями
            for schema, table_name, column_name, data_type in columns:
                if not check_table_exists(cursor_db, schema, table_name):
                    results.append(Fore.RED + f"Table {schema}.{table_name} does not exist in database: {db_name}")
                    continue  # Переходим к следующей таблице

                if not check_column_exists(cursor_db, schema, table_name, column_name):
                    results.append(Fore.RED + f"Column {column_name} does not exist in table {schema}.{table_name} in database: {db_name}")
                    continue  # Переходим к следующей колонке

                # Обрабатываем колонку с зарезервированным словом
                escaped_column_name = escape_reserved_keyword(column_name)
                query = f"SELECT COUNT(*) FROM {schema}.{table_name} WHERE {escaped_column_name} IS NOT NULL"
                
                # Логируем запрос для отладки
                print(Fore.MAGENTA + translations['query_log'].format(query, db_name, schema, table_name, escaped_column_name, data_type))

                try:
                    cursor_db.execute(query)
                    count = cursor_db.fetchone()[0]

                    # Если в колонке есть записи, выводим информацию
                    if count > 0:
                        results.append(Fore.GREEN + translations['records_found'].format(db_name, schema, table_name))
                        tables_with_records += 1
                        database_has_records = True  # Если хотя бы в одной таблице базы есть записи

                    total_tables += 1  # Мы всегда увеличиваем счетчик обработанных таблиц

                except Exception as e:
                    results.append(Fore.RED + f"Error executing query on table: {schema}.{table_name}, column: {escaped_column_name}. Error: {e}")

            if database_has_records:
                databases_with_records += 1

            conn_db.close()

        conn.close()

    except Exception as e:
        results.append(Fore.RED + translations['error'].format(e))

    # Вывод результатов в консоль
    print(Fore.CYAN + translations['final_report'])
    for line in results:
        print(line)

    # Запись результатов в файл
    try:
        with open("analysis_results.txt", "w") as file:
            for line in results:
                file.write(f"{line}\n")
        print(Fore.GREEN + translations['analysis_results_saved'])
    except Exception as e:
        print(Fore.RED + f"Error saving results to file: {e}")

    # Итоги
    print(Fore.CYAN + translations['final_report'])
    print(Fore.YELLOW + translations['processed_databases'].format(total_databases))
    print(Fore.YELLOW + translations['processed_tables'].format(total_tables))
    print(Fore.YELLOW + translations['databases_with_records'].format(databases_with_records))
    print(Fore.YELLOW + translations['tables_with_records'].format(tables_with_records))
    input(Fore.CYAN + translations['press_enter'])

# Главная функция
def main():
    language = choose_language()
    analyze_databases_for_records(language)

# Запуск программы
if __name__ == "__main__":
    main()
