import os
import subprocess

# Описание скрипта:
# Этот Python скрипт предназначен для автоматического создания SQL-запросов для восстановления баз данных в SQL Server, для BnS-2017.
# из резервных копий (файлы с расширением .bak). Скрипт сначала создает файл DBList.txt, в котором будет
# содержаться список всех файлов .bak в указанной директории. Затем на основе этого списка генерируются SQL-запросы,
# которые могут быть использованы для восстановления баз данных в SQL Server.
# Для каждой базы данных в списке скрипт проверяет наличие необходимых папок для восстановления данных (.mdf) и журналов (.ldf)
# и создает их, если это необходимо. Все запросы записываются в файл restore_databases_2017.sql.

# Script description:
# This Python script is designed to automatically create SQL queries to restore databases in SQL Server, for BnS-2017.
# from backup files (with .bak extension). The script first creates the file DBList.txt, which contains 
# a list of all .bak files in the specified directory. Based on this list, SQL queries are generated 
# that can be used for restoring databases in SQL Server.
# For each database in the list, the script checks if the necessary folders for data (.mdf) and log (.ldf) files 
# exist and creates them if needed. All the queries are written to the file restore_databases_2017.sql.

import os
import subprocess

# Путь к директории с резервными копиями
# Path to the directory with backup files
backup_dir = "D:\\SQL-Data-Backups\\"

# Создаем список .bak файлов в указанной директории и записываем в DBList.txt
# Create a list of .bak files in the specified directory and write it to DBList.txt
list_command = f'dir "{backup_dir}*.bak" /b > "D:\\DBList.txt"'
subprocess.run(list_command, shell=True)

# Открываем файл DBList.txt для чтения
# Open the DBList.txt file for reading
with open("D:\\DBList.txt", "r") as file:
    databases = file.readlines()

# Очищаем список от лишних пробелов и символов новой строки
# Clean the list from unnecessary spaces and newlines
databases = [db.strip() for db in databases]

# Путь, куда будут восстанавливаться базы данных
# Path where databases will be restored
output_dir = "D:\\DataDB\\"

# Проверяем, существует ли папка для базы данных, если нет - создаем
# Check if the folder for database files exists, if not, create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Создаем новый файл для записи SQL запросов
# Create a new file to write SQL queries
with open("restore_databases_2017.sql", "w") as sql_file:
    for db in databases:
        # Формируем SQL запрос для каждой базы данных
        # Create SQL query for each database
        db_name = db.replace('.bak', '')
        mdf_path = f"{output_dir}{db_name}.mdf"
        ldf_path = f"{output_dir}{db_name}_log.ldf"
        
        # Проверяем, существует ли папка для файлов базы данных
        # Check if the folder for database files exists
        if not os.path.exists(os.path.dirname(mdf_path)):
            os.makedirs(os.path.dirname(mdf_path))
        
        sql_query = f"""
RESTORE DATABASE {db_name}
FROM DISK = 'D:\\SQL-Data-Backups\\{db}'
WITH
    MOVE '{db_name}' TO '{mdf_path}',
    MOVE '{db_name}_log' TO '{ldf_path}',
    REPLACE,
    STATS = 10;
"""
        # Записываем запрос в файл
        # Write the query to the file
        sql_file.write(sql_query)

print("SQL script generated successfully: restore_databases_2017.sql")
# Скрипт успешно создан: restore_databases_2017.sql
# SQL script generated successfully: restore_databases_2017.sql
