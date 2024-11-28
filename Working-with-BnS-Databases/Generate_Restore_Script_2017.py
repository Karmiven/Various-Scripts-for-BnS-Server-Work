import os

# Описание скрипта:
# Этот Python скрипт предназначен для автоматического создания SQL-запросов для восстановления баз данных в SQL Server.
# Скрипт работает с резервными копиями, хранящимися в файлах с расширением .bak.
# Он генерирует SQL-скрипты для каждой базы данных в списке.
# В каждом скрипте указывается путь к файлу резервной копии и папке для восстановления данных (.mdf) и журналов (.ldf).
# Для каждой базы данных создается запрос с использованием команды RESTORE DATABASE.
# В запросах указывается путь к .bak файлу и новое расположение для данных и журналов базы данных.
# Все сгенерированные запросы записываются в файл Restore_Database_2017.sql.

# Script description:
# This Python script is designed to automatically create SQL queries to restore databases in SQL Server.
# The script works with backup files stored in .bak files.
# It generates SQL scripts for each database in the list.
# Each script specifies the path to the backup file and the folder for restoring data (.mdf) and log (.ldf) files.
# For each database, a query is created using the RESTORE DATABASE command.
# The queries specify the path to the .bak file and the new location for the data and log files of the database.
# All generated queries are saved in the Restore_Database_2017.sql file.

# Папка с бекапами
# Folder with backup files
backup_folder = 'D:\\SQL-DATA\\'

# Папка, куда будем восстанавливать базы данных
# Folder where databases will be restored
restore_folder = 'D:\\DataDB\\'

# Список баз данных (файлы .bak)
# List of databases (with .bak files)
bak_files = [
    'AchievementDb',
    'ApiDb',
    'AppDb',
    'AuctionDb',
    'AuctionMasterDb',
    'AuctionSearchDb',
    'BanDb',
    'BlGame01',
    'CouponDb',
    'CraftDb',
    'DeliveryDb',
    'FriendDb',
    'GameWarehouseDb',
    'GlobalNameDb',
    'GMToolLogDb',
    'GoodsDb',
    'GradeMembersDb',
    'LevelDb',
    'LimitDb',
    'LobbyDb',
    'LoginDb',
    'ManagementDb',
    'MarketDb',
    'MyAuctionSearchDb',
    'PlatformAcctDb',
    'PlatformGameDb',
    'PlatformMasterDb',
    'PlatformSessionDb',
    'PlatformSlotDb',
    'PostOfficeDb',
    'PrivacyDb',
    'ProfileDb',
    'PromotionStampDb',
    'PurchaseAdminDb',
    'PurchaseDb',
    'RankingDb',
    'RefundDb',
    'ReportingDb',
    'RewardDb',
    'RoleDb',
    'ShowcaseDb',
    'VirtualCurrencyDb',
    'WarehouseDb_bnsgrnTH'
]

# Функция для создания скрипта восстановления для каждой базы
# Function to generate restore script for each database
def generate_restore_script():
    restore_script = ""
    
    for bak_file in bak_files:
        # Извлекаем имя базы из файла .bak
        # Extract database name from the .bak file
        db_name = os.path.splitext(bak_file)[0]
        
        # Создаем шаблон для каждой базы
        # Create template for each database
        restore_script += f"RESTORE DATABASE {db_name}\n"
        restore_script += f"FROM DISK = '{backup_folder}{bak_file}'\n"
        restore_script += "WITH\n"
        restore_script += f"    MOVE '{db_name}' TO '{restore_folder}{db_name}.mdf',\n"
        restore_script += f"    MOVE '{db_name}_log' TO '{restore_folder}{db_name}_log.ldf',\n"
        restore_script += "    REPLACE,\n    STATS = 10;\n\n"

    try:
        # Записываем скрипт в файл
        # Write the script to the file
        with open("Restore_Database_2017.sql", "w") as file:
            file.write(restore_script)
        print("Скрипт восстановления баз данных был успешно сгенерирован и сохранен в файл 'Restore_Database_2017.sql'.")
        # The restore script has been successfully generated and saved to 'Restore_Database_2017.sql'.
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")
        # Error while creating the file.

# Запускаем функцию генерации скрипта
# Run the function to generate the restore script
generate_restore_script()
