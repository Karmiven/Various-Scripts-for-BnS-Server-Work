RESTORE DATABASE AchievementDb
FROM DISK = 'D:\BK_DataDB_2017\AchievementDb.bak'
WITH
    MOVE 'AchievementDb' TO 'D:\DataDB_2017\AchievementDb.mdf',
    MOVE 'AchievementDb_log' TO 'D:\DataDB_2017\AchievementDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE ApiDb
FROM DISK = 'D:\BK_DataDB_2017\ApiDb.bak'
WITH
    MOVE 'ApiDb' TO 'D:\DataDB_2017\ApiDb.mdf',
    MOVE 'ApiDb_log' TO 'D:\DataDB_2017\ApiDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE AppDb
FROM DISK = 'D:\BK_DataDB_2017\AppDb.bak'
WITH
    MOVE 'AppDb' TO 'D:\DataDB_2017\AppDb.mdf',
    MOVE 'AppDb_log' TO 'D:\DataDB_2017\AppDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE AuctionDb
FROM DISK = 'D:\BK_DataDB_2017\AuctionDb.bak'
WITH
    MOVE 'AuctionDb' TO 'D:\DataDB_2017\AuctionDb.mdf',
    MOVE 'AuctionDb_log' TO 'D:\DataDB_2017\AuctionDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE AuctionMasterDb
FROM DISK = 'D:\BK_DataDB_2017\AuctionMasterDb.bak'
WITH
    MOVE 'AuctionMasterDb' TO 'D:\DataDB_2017\AuctionMasterDb.mdf',
    MOVE 'AuctionMasterDb_log' TO 'D:\DataDB_2017\AuctionMasterDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE AuctionSearchDb
FROM DISK = 'D:\BK_DataDB_2017\AuctionSearchDb.bak'
WITH
    MOVE 'AuctionSearchDb' TO 'D:\DataDB_2017\AuctionSearchDb.mdf',
    MOVE 'AuctionSearchDb_log' TO 'D:\DataDB_2017\AuctionSearchDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE BanDb
FROM DISK = 'D:\BK_DataDB_2017\BanDb.bak'
WITH
    MOVE 'BanDb' TO 'D:\DataDB_2017\BanDb.mdf',
    MOVE 'BanDb_log' TO 'D:\DataDB_2017\BanDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE BlGame01
FROM DISK = 'D:\BK_DataDB_2017\BlGame01.bak'
WITH
    MOVE 'BlGame01' TO 'D:\DataDB_2017\BlGame01.mdf',
    MOVE 'BlGame01_log' TO 'D:\DataDB_2017\BlGame01_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE CouponDb
FROM DISK = 'D:\BK_DataDB_2017\CouponDb.bak'
WITH
    MOVE 'CouponDb' TO 'D:\DataDB_2017\CouponDb.mdf',
    MOVE 'CouponDb_log' TO 'D:\DataDB_2017\CouponDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE CraftDb
FROM DISK = 'D:\BK_DataDB_2017\CraftDb.bak'
WITH
    MOVE 'CraftDb' TO 'D:\DataDB_2017\CraftDb.mdf',
    MOVE 'CraftDb_log' TO 'D:\DataDB_2017\CraftDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE DeliveryDb
FROM DISK = 'D:\BK_DataDB_2017\DeliveryDb.bak'
WITH
    MOVE 'DeliveryDb' TO 'D:\DataDB_2017\DeliveryDb.mdf',
    MOVE 'DeliveryDb_log' TO 'D:\DataDB_2017\DeliveryDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE FriendDb
FROM DISK = 'D:\BK_DataDB_2017\FriendDb.bak'
WITH
    MOVE 'FriendDb' TO 'D:\DataDB_2017\FriendDb.mdf',
    MOVE 'FriendDb_log' TO 'D:\DataDB_2017\FriendDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE GameWarehouseDb
FROM DISK = 'D:\BK_DataDB_2017\GameWarehouseDb.bak'
WITH
    MOVE 'GameWarehouseDb' TO 'D:\DataDB_2017\GameWarehouseDb.mdf',
    MOVE 'GameWarehouseDb_log' TO 'D:\DataDB_2017\GameWarehouseDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE GlobalNameDb
FROM DISK = 'D:\BK_DataDB_2017\GlobalNameDb.bak'
WITH
    MOVE 'GlobalNameDb' TO 'D:\DataDB_2017\GlobalNameDb.mdf',
    MOVE 'GlobalNameDb_log' TO 'D:\DataDB_2017\GlobalNameDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE GMToolLogDb
FROM DISK = 'D:\BK_DataDB_2017\GMToolLogDb.bak'
WITH
    MOVE 'GMToolLogDb' TO 'D:\DataDB_2017\GMToolLogDb.mdf',
    MOVE 'GMToolLogDb_log' TO 'D:\DataDB_2017\GMToolLogDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE GoodsDb
FROM DISK = 'D:\BK_DataDB_2017\GoodsDb.bak'
WITH
    MOVE 'GoodsDb' TO 'D:\DataDB_2017\GoodsDb.mdf',
    MOVE 'GoodsDb_log' TO 'D:\DataDB_2017\GoodsDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE GradeMembersDb
FROM DISK = 'D:\BK_DataDB_2017\GradeMembersDb.bak'
WITH
    MOVE 'GradeMembersDb' TO 'D:\DataDB_2017\GradeMembersDb.mdf',
    MOVE 'GradeMembersDb_log' TO 'D:\DataDB_2017\GradeMembersDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE LevelDb
FROM DISK = 'D:\BK_DataDB_2017\LevelDb.bak'
WITH
    MOVE 'LevelDb' TO 'D:\DataDB_2017\LevelDb.mdf',
    MOVE 'LevelDb_log' TO 'D:\DataDB_2017\LevelDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE LimitDb
FROM DISK = 'D:\BK_DataDB_2017\LimitDb.bak'
WITH
    MOVE 'LimitDb' TO 'D:\DataDB_2017\LimitDb.mdf',
    MOVE 'LimitDb_log' TO 'D:\DataDB_2017\LimitDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE LobbyDb
FROM DISK = 'D:\BK_DataDB_2017\LobbyDb.bak'
WITH
    MOVE 'LobbyDb' TO 'D:\DataDB_2017\LobbyDb.mdf',
    MOVE 'LobbyDb_log' TO 'D:\DataDB_2017\LobbyDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE LoginDb
FROM DISK = 'D:\BK_DataDB_2017\LoginDb.bak'
WITH
    MOVE 'LoginDb' TO 'D:\DataDB_2017\LoginDb.mdf',
    MOVE 'LoginDb_log' TO 'D:\DataDB_2017\LoginDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE ManagementDb
FROM DISK = 'D:\BK_DataDB_2017\ManagementDb.bak'
WITH
    MOVE 'ManagementDb' TO 'D:\DataDB_2017\ManagementDb.mdf',
    MOVE 'ManagementDb_log' TO 'D:\DataDB_2017\ManagementDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE MarketDb
FROM DISK = 'D:\BK_DataDB_2017\MarketDb.bak'
WITH
    MOVE 'MarketDb' TO 'D:\DataDB_2017\MarketDb.mdf',
    MOVE 'MarketDb_log' TO 'D:\DataDB_2017\MarketDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE MyAuctionSearchDb
FROM DISK = 'D:\BK_DataDB_2017\MyAuctionSearchDb.bak'
WITH
    MOVE 'MyAuctionSearchDb' TO 'D:\DataDB_2017\MyAuctionSearchDb.mdf',
    MOVE 'MyAuctionSearchDb_log' TO 'D:\DataDB_2017\MyAuctionSearchDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PlatformAcctDb
FROM DISK = 'D:\BK_DataDB_2017\PlatformAcctDb.bak'
WITH
    MOVE 'PlatformAcctDb' TO 'D:\DataDB_2017\PlatformAcctDb.mdf',
    MOVE 'PlatformAcctDb_log' TO 'D:\DataDB_2017\PlatformAcctDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PlatformGameDb
FROM DISK = 'D:\BK_DataDB_2017\PlatformGameDb.bak'
WITH
    MOVE 'PlatformGameDb' TO 'D:\DataDB_2017\PlatformGameDb.mdf',
    MOVE 'PlatformGameDb_log' TO 'D:\DataDB_2017\PlatformGameDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PlatformMasterDb
FROM DISK = 'D:\BK_DataDB_2017\PlatformMasterDb.bak'
WITH
    MOVE 'PlatformMasterDb' TO 'D:\DataDB_2017\PlatformMasterDb.mdf',
    MOVE 'PlatformMasterDb_log' TO 'D:\DataDB_2017\PlatformMasterDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PlatformSessionDb
FROM DISK = 'D:\BK_DataDB_2017\PlatformSessionDb.bak'
WITH
    MOVE 'PlatformSessionDb' TO 'D:\DataDB_2017\PlatformSessionDb.mdf',
    MOVE 'PlatformSessionDb_log' TO 'D:\DataDB_2017\PlatformSessionDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PlatformSlotDb
FROM DISK = 'D:\BK_DataDB_2017\PlatformSlotDb.bak'
WITH
    MOVE 'PlatformSlotDb' TO 'D:\DataDB_2017\PlatformSlotDb.mdf',
    MOVE 'PlatformSlotDb_log' TO 'D:\DataDB_2017\PlatformSlotDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PostOfficeDb
FROM DISK = 'D:\BK_DataDB_2017\PostOfficeDb.bak'
WITH
    MOVE 'PostOfficeDb' TO 'D:\DataDB_2017\PostOfficeDb.mdf',
    MOVE 'PostOfficeDb_log' TO 'D:\DataDB_2017\PostOfficeDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PrivacyDb
FROM DISK = 'D:\BK_DataDB_2017\PrivacyDb.bak'
WITH
    MOVE 'PrivacyDb' TO 'D:\DataDB_2017\PrivacyDb.mdf',
    MOVE 'PrivacyDb_log' TO 'D:\DataDB_2017\PrivacyDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE ProfileDb
FROM DISK = 'D:\BK_DataDB_2017\ProfileDb.bak'
WITH
    MOVE 'ProfileDb' TO 'D:\DataDB_2017\ProfileDb.mdf',
    MOVE 'ProfileDb_log' TO 'D:\DataDB_2017\ProfileDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PromotionStampDb
FROM DISK = 'D:\BK_DataDB_2017\PromotionStampDb.bak'
WITH
    MOVE 'PromotionStampDb' TO 'D:\DataDB_2017\PromotionStampDb.mdf',
    MOVE 'PromotionStampDb_log' TO 'D:\DataDB_2017\PromotionStampDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PurchaseAdminDb
FROM DISK = 'D:\BK_DataDB_2017\PurchaseAdminDb.bak'
WITH
    MOVE 'PurchaseAdminDb' TO 'D:\DataDB_2017\PurchaseAdminDb.mdf',
    MOVE 'PurchaseAdminDb_log' TO 'D:\DataDB_2017\PurchaseAdminDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PurchaseDb
FROM DISK = 'D:\BK_DataDB_2017\PurchaseDb.bak'
WITH
    MOVE 'PurchaseDb' TO 'D:\DataDB_2017\PurchaseDb.mdf',
    MOVE 'PurchaseDb_log' TO 'D:\DataDB_2017\PurchaseDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE RankingDb
FROM DISK = 'D:\BK_DataDB_2017\RankingDb.bak'
WITH
    MOVE 'RankingDb' TO 'D:\DataDB_2017\RankingDb.mdf',
    MOVE 'RankingDb_log' TO 'D:\DataDB_2017\RankingDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE RefundDb
FROM DISK = 'D:\BK_DataDB_2017\RefundDb.bak'
WITH
    MOVE 'RefundDb' TO 'D:\DataDB_2017\RefundDb.mdf',
    MOVE 'RefundDb_log' TO 'D:\DataDB_2017\RefundDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE ReportingDb
FROM DISK = 'D:\BK_DataDB_2017\ReportingDb.bak'
WITH
    MOVE 'ReportingDb' TO 'D:\DataDB_2017\ReportingDb.mdf',
    MOVE 'ReportingDb_log' TO 'D:\DataDB_2017\ReportingDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE RewardDb
FROM DISK = 'D:\BK_DataDB_2017\RewardDb.bak'
WITH
    MOVE 'RewardDb' TO 'D:\DataDB_2017\RewardDb.mdf',
    MOVE 'RewardDb_log' TO 'D:\DataDB_2017\RewardDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE RoleDb
FROM DISK = 'D:\BK_DataDB_2017\RoleDb.bak'
WITH
    MOVE 'RoleDb' TO 'D:\DataDB_2017\RoleDb.mdf',
    MOVE 'RoleDb_log' TO 'D:\DataDB_2017\RoleDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE ShowcaseDb
FROM DISK = 'D:\BK_DataDB_2017\ShowcaseDb.bak'
WITH
    MOVE 'ShowcaseDb' TO 'D:\DataDB_2017\ShowcaseDb.mdf',
    MOVE 'ShowcaseDb_log' TO 'D:\DataDB_2017\ShowcaseDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE VirtualCurrencyDb
FROM DISK = 'D:\BK_DataDB_2017\VirtualCurrencyDb.bak'
WITH
    MOVE 'VirtualCurrencyDb' TO 'D:\DataDB_2017\VirtualCurrencyDb.mdf',
    MOVE 'VirtualCurrencyDb_log' TO 'D:\DataDB_2017\VirtualCurrencyDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE WarehouseDb_bnsgrnTH
FROM DISK = 'D:\BK_DataDB_2017\WarehouseDb_bnsgrnTH.bak'
WITH
    MOVE 'WarehouseDb_bnsgrnTH' TO 'D:\DataDB_2017\WarehouseDb_bnsgrnTH.mdf',
    MOVE 'WarehouseDb_bnsgrnTH_log' TO 'D:\DataDB_2017\WarehouseDb_bnsgrnTH_log.ldf',
    REPLACE,
    STATS = 10;

