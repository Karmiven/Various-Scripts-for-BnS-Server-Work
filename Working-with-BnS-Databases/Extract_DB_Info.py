import subprocess
import sys

# Скрипт анализирует структуры баз данных SQL Server, выводя информацию о таблицах, колонках, ключах и индексах.
# Подключение к серверу осуществляется через библиотеку pyodbc. При необходимости отсутствующие библиотеки автоматически устанавливаются.
# Скрипт предоставляет пользователю выбор между расширенным и простым режимами анализа данных.
# В расширенном режиме отображается подробная информация о колонках, первичных и внешних ключах, а также индексах.
# Результаты анализа сохраняются в файл database_structure.txt.
# Для удобства вывод в консоль оформляется с помощью цветового форматирования (colorama).
# Скрипт поддерживает выбор языка сообщений (русский или английский).

# The script analyzes the structure of SQL Server databases, providing information about tables, columns, keys, and indexes.
# It connects to the server using the pyodbc library. Missing libraries are automatically installed if necessary.
# The script allows the user to choose between detailed and simple modes of data analysis.
# In detailed mode, comprehensive information about columns, primary and foreign keys, and indexes is displayed.
# The results of the analysis are saved to the database_structure.txt file.
# Console output is formatted using colorama for better readability.
# The script supports language selection (Russian or English).


# Функция для установки библиотек
def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при установке {package}: {e}")
        sys.exit(1)

# Проверка и установка библиотек
try:
    import pyodbc
except ImportError:
    print("pyodbc library not found. Installing...")
    install_package('pyodbc')
    import pyodbc

try:
    from colorama import Fore, Style, init
except ImportError:
    print("colorama library not found. Installing...")
    install_package('colorama')
    from colorama import Fore, Style, init

try:
    from termcolor import colored
except ImportError:
    print("termcolor library not found. Installing...")
    install_package('termcolor')
    from termcolor import colored

# Инициализация colorama
init(autoreset=True)

# Настройки подключения к базе данных
conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=127.0.0.1;'  # Укажите ваш сервер
    r'DATABASE=master;'  # Подключаемся к системной базе данных
    r'UID=sa;'  # Укажите ваше имя пользователя
    r'PWD=FSmElsXuj3ls8Fq'  # Укажите ваш пароль
)

# Локализация: словари для разных языков
translations = {
    'ru': {
        'choose_language': "Выберите язык:",
        'language_ru': "1 - Русский",
        'language_en': "2 - Английский",
        'choose_mode': "Выберите режим:",
        'extended_info': "1 - Расширенная информация",
        'simple_info': "2 - Простая информация",
        'invalid_choice': "Неверный выбор. Пожалуйста, выберите 1 или 2.",
        'database_info_saved': "Информация о базах данных успешно сохранена в файл database_structure.txt",
        'database': "База данных: ",
        'table': "Таблица: ",
        'primary_keys': "Первичные ключи: ",
        'foreign_key': "Внешний ключ: ",
        'index': "Индекс: ",
        'error': "Ошибка: ",
        'total_databases': "Всего баз данных: ",
        'total_tables': "Всего таблиц: ",
        'column': "Колонка",
        'tables': "Таблицы"  # Добавлен перевод для "tables"
    },
    'en': {
        'choose_language': "Choose language:",
        'language_ru': "1 - Russian",
        'language_en': "2 - English",
        'choose_mode': "Choose mode:",
        'extended_info': "1 - Extended information",
        'simple_info': "2 - Simple information",
        'invalid_choice': "Invalid choice. Please choose 1 or 2.",
        'database_info_saved': "Database structure information successfully saved to database_structure.txt",
        'database': "Database: ",
        'table': "Table: ",
        'primary_keys': "Primary keys: ",
        'foreign_key': "Foreign key: ",
        'index': "Index: ",
        'error': "Error: ",
        'total_databases': "Total databases: ",
        'total_tables': "Total tables: ",
        'column': "Column",
        'tables': "Tables"  # Добавлен перевод для "tables"
    }
}

# Функция для установки языка
def choose_language():
    print(f"{Fore.YELLOW}{translations['ru']['choose_language']}")
    print(f"  {Fore.GREEN}{translations['ru']['language_ru']}")
    print(f"  {Fore.GREEN}{translations['ru']['language_en']}")
    choice = input(f"{Fore.CYAN}{Style.BRIGHT}Enter 1 or 2: ")
    return 'ru' if choice == '1' else 'en' if choice == '2' else 'ru'

# Инициализация языка до его использования
language = choose_language()

# Функция для получения информации о базе данных
def extract_database_info(is_extended):
    conn = None
    cursor = None

    try:
        # Устанавливаем подключение
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Получаем список баз данных
        cursor.execute("SELECT name FROM sys.databases WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb');")
        databases = [row[0] for row in cursor.fetchall()]

        total_databases = len(databases)
        total_tables = 0
        output = ''

        for db in databases:
            print(f"{Fore.YELLOW}{'=' * 50}")
            print(f"{Fore.GREEN}{Style.BRIGHT}{translations[language]['database']}{db}")
            print(f"{Fore.YELLOW}{'=' * 50}")
            output += "=" * 50 + "\n"
            output += f"{translations[language]['database']}{db}\n{'=' * 50}\n"

            cursor.execute(f"USE [{db}];")

            # Получаем таблицы с их схемами
            cursor.execute("""
                SELECT TABLE_SCHEMA, TABLE_NAME
                FROM INFORMATION_SCHEMA.TABLES
                WHERE TABLE_TYPE = 'BASE TABLE';
            """)
            tables = cursor.fetchall()
            total_tables_in_db = len(tables)
            total_tables += total_tables_in_db

            for table in tables:
                schema, table_name = table
                if is_extended:
                    print(f"\n  {Fore.CYAN}{Style.BRIGHT}{translations[language]['table']}: {table_name} ({schema})")
                    output += f"\n  {translations[language]['table']}: {table_name} ({schema})\n"

                    # Проверяем, если таблица в схеме dbo
                    if schema == 'dbo':
                        print(f"    {Fore.GREEN}This table is in dbo schema.")
                        output += f"    This table is in dbo schema.\n"
                    else:
                        print(f"    {Fore.RED}This table is not in dbo schema, it is in schema {schema}.")
                        output += f"    This table is not in dbo schema, it is in schema {schema}.\n"

                    # Колонки таблицы
                    cursor.execute(f"""
                        SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE, COLUMN_DEFAULT
                        FROM INFORMATION_SCHEMA.COLUMNS 
                        WHERE TABLE_SCHEMA = '{schema}' AND TABLE_NAME = '{table_name}';
                    """)
                    columns = cursor.fetchall()
                    for column in columns:
                        column_name, data_type, max_length, is_nullable, column_default = column
                        print(f"    {Fore.MAGENTA}{translations[language]['column']}: {column_name} ({data_type}, MaxLength={max_length}, Nullable={is_nullable}, Default={column_default})")
                        output += f"    {translations[language]['column']}: {column_name} ({data_type}, MaxLength={max_length}, Nullable={is_nullable}, Default={column_default})\n"

                    # Первичные ключи
                    cursor.execute(f"""
                        SELECT kcu.COLUMN_NAME
                        FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS tc
                        JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS kcu
                            ON tc.CONSTRAINT_NAME = kcu.CONSTRAINT_NAME
                        WHERE tc.TABLE_SCHEMA = '{schema}' AND tc.TABLE_NAME = '{table_name}' AND tc.CONSTRAINT_TYPE = 'PRIMARY KEY';
                    """)
                    primary_keys = [row[0] for row in cursor.fetchall()]
                    if primary_keys:
                        print(f"    {Fore.YELLOW}{translations[language]['primary_keys']}: {', '.join(primary_keys)}")
                        output += f"    {translations[language]['primary_keys']}: {', '.join(primary_keys)}\n"

                    # Внешние ключи
                    cursor.execute(f"""
                        SELECT 
                            fk.name AS ForeignKeyName,
                            tp.name AS ParentTable,
                            cp.name AS ParentColumn,
                            tr.name AS ReferencedTable,
                            rc.name AS ReferencedColumn
                        FROM sys.foreign_keys AS fk
                        INNER JOIN sys.foreign_key_columns AS fkc ON fk.object_id = fkc.constraint_object_id
                        INNER JOIN sys.tables AS tp ON fk.parent_object_id = tp.object_id
                        INNER JOIN sys.columns AS cp ON tp.object_id = cp.object_id AND fkc.parent_column_id = cp.column_id
                        INNER JOIN sys.tables AS tr ON fk.referenced_object_id = tr.object_id
                        INNER JOIN sys.columns AS rc ON tr.object_id = rc.object_id AND fkc.referenced_column_id = rc.column_id
                        WHERE tp.name = '{table_name}' AND SCHEMA_NAME(tp.schema_id) = '{schema}';
                    """)
                    foreign_keys = cursor.fetchall()
                    for fk in foreign_keys:
                        foreign_key_name, parent_table, parent_column, referenced_table, referenced_column = fk
                        print(f"    {Fore.CYAN}{translations[language]['foreign_key']}: {foreign_key_name}, Column: {parent_column}, Referenced Table: {referenced_table}({referenced_column})")
                        output += f"    {translations[language]['foreign_key']}: {foreign_key_name}, Column: {parent_column}, Referenced Table: {referenced_table}({referenced_column})\n"

                    # Индексы
                    cursor.execute(f"""
                        SELECT i.name AS IndexName, i.type_desc AS IndexType, c.name AS ColumnName
                        FROM sys.indexes i
                        INNER JOIN sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
                        INNER JOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
                        WHERE i.object_id = OBJECT_ID('{schema}.{table_name}');
                    """)
                    indexes = cursor.fetchall()
                    for index in indexes:
                        index_name, index_type, column_name = index
                        print(f"    {Fore.BLUE}{translations[language]['index']}: {index_name} ({index_type}), Column: {column_name}")
                        output += f"    {translations[language]['index']}: {index_name} ({index_type}), Column: {column_name}\n"

                else:  # Для простой информации
                    print(f"  {Fore.CYAN}{Style.BRIGHT}{translations[language]['table']}: {table_name}")
                    output += f"  {translations[language]['table']}: {table_name}\n"

            print(f"{Fore.YELLOW}{'=' * 50}{translations[language]['tables']} \"{db}\" - Received")
            print(f"{Fore.GREEN}{'=' * 30}{translations[language]['total_tables']} - {total_tables_in_db}\n")
            output += f"{translations[language]['tables']} \"{db}\" - Received\n{translations[language]['total_tables']} - {total_tables_in_db}\n\n"

        print(f"{Fore.RED}{'=' * 50}{translations[language]['total_databases']} - {total_databases}")
        print(f"{Fore.RED}{'=' * 50}{translations[language]['total_tables']} - {total_tables}")

        # Сохраняем в файл
        with open('database_structure.txt', 'w', encoding='utf-8') as file:
            file.write(output)

        print(colored(translations[language]['database_info_saved'], 'green'))

    except Exception as e:
        print(f"{Fore.RED}{translations[language]['error']} {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Ввод пользователя для выбора режима
def user_choice():
    print(f"{Fore.YELLOW}{translations[language]['choose_mode']}")
    print(f"  {Fore.GREEN}{translations[language]['extended_info']}")
    print(f"  {Fore.GREEN}{translations[language]['simple_info']}")
    choice = input(f"{Fore.CYAN}{Style.BRIGHT}Enter 1 or 2: ")
    return choice

# Запуск
choice = user_choice()
if choice == '1':
    extract_database_info(is_extended=True)
elif choice == '2':
    extract_database_info(is_extended=False)
else:
    print(f"{Fore.RED}{translations[language]['invalid_choice']}")
input(f"{Fore.YELLOW}Press Enter to close...")