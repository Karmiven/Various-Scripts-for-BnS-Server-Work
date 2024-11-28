import subprocess
import sys

# Скрипт для подключения к серверу SQL Server, выполнения поиска по всем базам данных и записи результатов в файл.
# Подключение к серверу происходит через библиотеку pyodbc. Скрипт осуществляет поиск заданного слова в различных таблицах 
# и столбцах баз данных, исключая системные таблицы. Результаты поиска записываются в файл.
# Если библиотека pyodbc не установлена, она будет автоматически установлена перед выполнением поиска.
#
# This script connects to a SQL Server, performs a search across all databases, and logs the results to a file.
# The connection is made using the pyodbc library. The script searches for a given word across different tables 
# and columns in databases, excluding system tables. Search results are saved to a file.
# If pyodbc is not installed, it will be automatically installed before performing the search.

# Проверка и установка библиотеки pyodbc
try:
    import pyodbc
except ImportError:
    print("pyodbc library not found. Installing...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyodbc"])
    except subprocess.CalledProcessError as e:
        print(f"Error installing pyodbc: {e}")
        input("Press Enter to exit...")
        sys.exit(1)
    import pyodbc

# Конфигурация подключения
server = 'localhost'  # Адрес сервера
user = 'SA'
password = 'FSmElsXuj3ls8Fq'

def connect_to_server(server, user, password, database=None):
    """Установление соединения с сервером SQL Server"""
    connection_string = f"DRIVER={{SQL Server}};SERVER={server};UID={user};PWD={password}"
    if database:
        connection_string += f";DATABASE={database}"
    return pyodbc.connect(connection_string)

def search_in_all_databases(search_word):
    """Поиск во всех базах данных"""
    results = []
    formatted_results = []
    total_databases = 0
    total_tables = 0
    total_results = 0

    try:
        conn = connect_to_server(server, user, password)
        cursor = conn.cursor()

        # Получение всех баз данных, исключая системные
        cursor.execute("SELECT name FROM sys.databases WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb')")
        databases = cursor.fetchall()

        if not databases:
            print("Databases not found.")
            return results, formatted_results, total_databases, total_tables, total_results

        for database in databases:
            db_name = database[0]
            total_databases += 1
            print(f"\n{'='*50}\nSearching in database: {db_name}\n{'='*50}")
            formatted_results.append(f"\n{'='*50}\nDatabase: {db_name}\n{'='*50}")
            conn_db = connect_to_server(server, user, password, database=db_name)
            cursor_db = conn_db.cursor()

            # Получение всех таблиц и колонок
            cursor_db.execute("""
                SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_NAME NOT LIKE 'sys%' AND TABLE_NAME NOT LIKE 'queue%'
            """)
            columns = cursor_db.fetchall()

            if not columns:
                print(f"No tables found in database: {db_name}")
                formatted_results.append(f"No tables found in database: {db_name}")
                continue

            for table_name, column_name, data_type in columns:
                total_tables += 1
                query = None
                search_value = None
                try:
                    # Поиск по строкам
                    if data_type in ('varchar', 'nvarchar', 'text', 'ntext', 'char', 'varchar(max)', 'nvarchar(max)'):
                        query = f"SELECT * FROM {table_name} WHERE {column_name} LIKE ?"
                        search_value = f"%{search_word}%"

                    # Поиск по числовым данным
                    elif data_type in ('int', 'bigint', 'decimal', 'float', 'smallint', 'tinyint', 'numeric', 'real'):
                        try:
                            search_value = float(search_word) if '.' in search_word else int(search_word)
                            query = f"SELECT * FROM {table_name} WHERE {column_name} = ?"
                        except ValueError:
                            print(f"Value '{search_word}' is not valid for numeric column {column_name}")
                            continue
                    
                    # Поиск по датам
                    elif data_type in ('datetime', 'datetimeoffset', 'date', 'time', 'smalldatetime'):
                        query = f"SELECT * FROM {table_name} WHERE CONVERT(VARCHAR, {column_name}, 120) LIKE ?"
                        search_value = f"%{search_word}%"
                    
                    # Поиск по уникальным идентификаторам (GUID)
                    elif data_type == 'uniqueidentifier':
                        if len(search_word) == 36:  # Длина GUID
                            query = f"SELECT * FROM {table_name} WHERE {column_name} = ?"
                            search_value = search_word
                        else:
                            print(f"Invalid GUID: {search_word}")
                            continue
                    
                    # Поиск по булевым значениям
                    elif data_type == 'bit':
                        if search_word.lower() in ('true', 'false', '1', '0'):
                            search_value = 1 if search_word.lower() in ('true', '1') else 0
                            query = f"SELECT * FROM {table_name} WHERE {column_name} = ?"
                        else:
                            print(f"Invalid bit value: {search_word}")
                            continue
                    
                    # Прочие типы
                    elif data_type in ('binary', 'varbinary', 'image', 'cursor', 'sql_variant', 'xml', 'geometry', 'geography'):
                        print(f"Unsupported data type '{data_type}' in column {column_name}")
                        continue
                    
                    else:
                        print(f"Unknown or unsupported data type '{data_type}' in column {column_name}")
                        continue

                    # Выполнение запроса
                    if query:
                        cursor_db.execute(query, search_value)
                        rows = cursor_db.fetchall()
                        if rows:
                            total_results += len(rows)
                            print(f"  Table: {table_name} | Column: {column_name}")
                            formatted_results.append(f"  Table: {table_name} | Column: {column_name}")
                            for row in rows:
                                formatted_row = ", ".join(map(str, row))
                                result = f"Database: {db_name}, Table: {table_name}, Column: {column_name}, Row: {formatted_row}"
                                print(f"  Row: {formatted_row}")
                                results.append(result)
                                formatted_results.append(f"  Row: {formatted_row}")
                        else:
                            formatted_results.append(f"  No results in table {table_name}, column {column_name}")
                except Exception as e:
                    print(f"Error processing column {column_name} in table {table_name}: {e}")

            conn_db.close()

        conn.close()

    except Exception as e:
        print(f"An error occurred: {e}")

    # Сохранение результатов в файлы
    try:
        with open('search_results_raw.txt', 'w', encoding='utf-8') as raw_file:
            raw_file.write("\n".join(results))
        print("\nRaw results saved to search_results_raw.txt")

        with open('search_results_formatted.txt', 'w', encoding='utf-8') as formatted_file:
            formatted_file.write("\n".join(formatted_results))
        print("Formatted results saved to search_results_formatted.txt")
    except Exception as e:
        print(f"Error writing to file: {e}")

    return results, total_databases, total_tables, total_results


# Запуск поиска
if __name__ == "__main__":
    search_word = input("Enter a word or number to search: ")
    print(f"\nStarting search for: {search_word}\n{'='*50}")
    results, total_databases, total_tables, total_results = search_in_all_databases(search_word)

    print(f"\n{'='*50}\nSearch Results:\n{'='*50}")
    for result in results:
        print(result)

    print(f"\n{'='*50}")
    print(f"Total databases processed: {total_databases}")
    print(f"Total tables processed: {total_tables}")
    print(f"Total results found: {total_results}")
    
    input("Press Enter to exit...")
