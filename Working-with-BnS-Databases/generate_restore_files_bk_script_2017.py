import os

# Этот скрипт предназначен для автоматической генерации SQL-запросов,
# которые восстанавливают базы данных из файлов бэкапа (.bak), 
# находящихся в указанной папке. Сгенерированные запросы будут записаны 
# в файл "restore_databases.sql". Файлы базы данных (.mdf) и 
# журналы транзакций (.ldf) будут помещены в заданный каталог восстановления.
#
# This script is designed to automatically generate SQL queries 
# that restore databases from backup files (.bak) located in a specified folder. 
# The generated queries will be written to the file "restore_databases.sql". 
# The database files (.mdf) and transaction logs (.ldf) will be placed 
# in the specified restore directory.

# Путь к папке с файлами бэкапа
backup_dir = r'D:\BnS-Server\SQL-Backups'
# Путь, куда будут восстанавливаться данные
restore_dir = r'D:\DataDB_2017'

# Создаем функцию для генерации SQL-запросов
def generate_restore_scripts(backup_directory, restore_directory):
    sql_script = ""

    # Получаем список файлов .bak в папке
    backup_files = [f for f in os.listdir(backup_directory) if f.endswith('.bak')]

    for backup_file in backup_files:
        # Извлекаем имя базы данных из имени файла
        db_name = os.path.splitext(backup_file)[0]

        # Создаем SQL-запрос для восстановления базы данных
        script = f"""
RESTORE DATABASE {db_name}
FROM DISK = '{os.path.join(backup_directory, backup_file)}'
WITH
    MOVE '{db_name}' TO '{os.path.join(restore_directory, db_name + ".mdf")}',
    MOVE '{db_name}_log' TO '{os.path.join(restore_directory, db_name + "_log.ldf")}',
    REPLACE,
    STATS = 10;
"""
        sql_script += script

    return sql_script

# Генерация скрипта
restore_script = generate_restore_scripts(backup_dir, restore_dir)

# Сохранение в файл
output_file = "Restore_Databases_2017.sql"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(restore_script)

print(f"Скрипт восстановления баз данных сохранен в файл {output_file}.")
