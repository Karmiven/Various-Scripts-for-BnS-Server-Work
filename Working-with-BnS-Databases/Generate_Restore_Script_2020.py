import os

# Папка с бекапами
backup_folder = 'D:\\SQL-DATA\\'

# Папка, куда будем восстанавливать базы данных
restore_folder = 'D:\\DataDB\\'

# Список баз данных (файлы .bak)
bak_files = [
    'AchievementDB.bak',
    'ApiDb.bak',
    'AppDb.bak',
    'AssociationAcctDb.bak',
    'AuctionDb.bak',
    'AuctionMasterDb.bak',
    'AuctionSearchDb.bak',
    'BanDb.bak',
    'BlGame.bak',
    'ContentBanDb.bak',
    'CouponDb.bak',
    'DeliveryDb.bak',
    'FriendDb.bak',
    'GameWarehouseDB.bak',
    'GlobalNameDb.bak',
    'GMToolLogDB.bak',
    'GoodsDb.bak',
    'GradeMembersDb.bak',
    'GradeSubscriptionDb.bak',
    'LevelDb.bak',
    'LimitDb.bak',
    'LobbyDB.bak',
    'ManagementDB.bak',
    'MarketDB.bak',
    'MyAuctionSearchDb.bak',
    'PlatformAcctDb.bak',
    'PlatformGameDb.bak',
    'PlatformMasterDb.bak',
    'PlatformSessionDb.bak',
    'PlatformSlotDb.bak',
    'PostOfficeDB.bak',
    'PrivacyDb.bak',
    'ProfileDb.bak',
    'PromotionStampDb.bak',
    'PurchaseAdminDb.bak',
    'PurchaseDb.bak',
    'RankingDB.bak',
    'RefundDb.bak',
    'ReportingDb.bak',
    'RewardDb.bak',
    'RoleDb.bak',
    'ShowcaseDb.bak',
    'SmartCouponDB.bak',
    'VirtualCurrencyDb.bak',
    'WarehouseDb.bak',
    'WishDb.bak'
]

# Функция для создания скрипта восстановления для каждой базы
def generate_restore_script():
    restore_script = ""
    
    for bak_file in bak_files:
        db_name = os.path.splitext(bak_file)[0]  # Извлекаем имя базы из файла .bak
        # Создаем шаблон для каждой базы
        restore_script += f"RESTORE DATABASE {db_name}\n"
        restore_script += f"FROM DISK = '{backup_folder}{bak_file}'\n"
        restore_script += "WITH\n"
        restore_script += f"    MOVE '{db_name}' TO '{restore_folder}{db_name}.mdf',\n"
        restore_script += f"    MOVE '{db_name}_log' TO '{restore_folder}{db_name}_log.ldf',\n"
        restore_script += "    REPLACE,\n    STATS = 10;\n\n"

    try:
        # Записываем скрипт в файл
        with open("Restore_Database.sql", "w") as file:
            file.write(restore_script)
        print("Скрипт восстановления баз данных был успешно сгенерирован и сохранен в файл 'Restore_Database.sql'.")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")

# Запускаем функцию генерации скрипта
generate_restore_script()
