import os

# Описание скрипта:
# Этот Python скрипт предназначен для автоматического создания SQL-запросов для бекапа баз данных в SQL Server. 
# Скрипт формирует запросы для каждой базы данных из списка, сохраняет бекап в указанной директории и генерирует SQL-скрипт для выполнения этих бекапов. 
# Для каждой базы данных создается строка запроса, которая будет сохранять резервную копию в файл с расширением .bak. Все запросы записываются в файл Backup_Database_2017.sql.
#
# Script description:
# This Python script is designed to automatically generate SQL queries for backing up databases in SQL Server. 
# The script generates backup queries for each database from the list, saving the backup in the specified directory, 
# and creates an SQL script to execute these backups. For each database, a backup query is formed to save the backup to a .bak file. 
# All the queries are written to the file Backup_Database_2017.sql.

# Папка, куда будем сохранять бекапы
# Folder where backups will be saved
backup_folder = 'D:\\SQL-DATA-BK\\'

# Список баз данных (без расширений)
# List of databases (without extensions)
databases = [
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

# Функция для создания скрипта бекапов для каждой базы
# Function to generate backup script for each database
def generate_backup_script():
    backup_script = ""

    for db_name in databases:
        # Формирование пути с двойными слэшами
        # Forming the backup query for each database
        backup_script += f"BACKUP DATABASE {db_name}\n"
        backup_script += f"TO DISK = '{backup_folder}{db_name}.bak'\n"
        backup_script += "WITH FORMAT, INIT, SKIP, NOREWIND, NOUNLOAD, STATS = 10;\n\n"

    try:
        # Записываем скрипт в файл
        # Write the script to a file
        with open("Backup_Database_2017.sql", "w") as file:
            file.write(backup_script)
        print("Скрипт для бекапов был успешно сгенерирован и сохранен в файл 'Backup_Database_2017.sql'.")
        # The backup script has been successfully generated and saved to 'Backup_Database_2017.sql'.
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")
        # Error while creating the file.

# Запускаем функцию генерации скрипта
# Run the function to generate the backup script
generate_backup_script()
