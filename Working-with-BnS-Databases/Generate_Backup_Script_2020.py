import os

# Папка, куда будем сохранять бекапы
backup_folder = 'D:\\SQL-DATA-BK\\'

# Список баз данных (без расширений)
databases = [
    'AchievementDB',
    'ApiDb',
    'AppDb',
    'AssociationAcctDb',
    'AuctionDb',
    'AuctionMasterDb',
    'AuctionSearchDb',
    'BanDb',
    'BlGame',
    'ContentBanDb',
    'CouponDb',
    'DeliveryDb',
    'FriendDb',
    'GameWarehouseDB',
    'GlobalNameDb',
    'GMToolLogDB',
    'GoodsDb',
    'GradeMembersDb',
    'GradeSubscriptionDb',
    'LevelDb',
    'LimitDb',
    'LobbyDB',
    'ManagementDB',
    'MarketDB',
    'MyAuctionSearchDb',
    'PlatformAcctDb',
    'PlatformGameDb',
    'PlatformMasterDb',
    'PlatformSessionDb',
    'PlatformSlotDb',
    'PostOfficeDB',
    'PrivacyDb',
    'ProfileDb',
    'PromotionStampDb',
    'PurchaseAdminDb',
    'PurchaseDb',
    'RankingDB',
    'RefundDb',
    'ReportingDb',
    'RewardDb',
    'RoleDb',
    'ShowcaseDb',
    'SmartCouponDB',
    'VirtualCurrencyDb',
    'WarehouseDb',
    'WishDb'
]

# Функция для создания скрипта бекапов для каждой базы
def generate_backup_script():
    backup_script = ""

    for db_name in databases:
        # Формирование пути с двойными слэшами
        backup_script += f"BACKUP DATABASE {db_name}\n"
        backup_script += f"TO DISK = '{backup_folder}{db_name}.bak'\n"
        backup_script += "WITH FORMAT, INIT, SKIP, NOREWIND, NOUNLOAD, STATS = 10;\n\n"

    try:
        # Записываем скрипт в файл
        with open("Backup_Database.sql", "w") as file:
            file.write(backup_script)
        print("Скрипт для бекапов был успешно сгенерирован и сохранен в файл 'Backup_Database.sql'.")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")

# Запускаем функцию генерации скрипта
generate_backup_script()
