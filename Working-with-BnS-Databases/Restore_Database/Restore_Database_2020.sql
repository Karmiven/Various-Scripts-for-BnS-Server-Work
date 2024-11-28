RESTORE DATABASE AchievementDb
FROM DISK = 'D:\BK_DataDB_2020\AchievementDb.bak'
WITH
    MOVE 'AchievementDb' TO 'D:\DataDB_2020\AchievementDb.mdf',
    MOVE 'AchievementDb_log' TO 'D:\DataDB_2020\AchievementDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE ApiDb
FROM DISK = 'D:\BK_DataDB_2020\ApiDb.bak'
WITH
    MOVE 'ApiDb' TO 'D:\DataDB_2020\ApiDb.mdf',
    MOVE 'ApiDb_log' TO 'D:\DataDB_2020\ApiDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE AppDb
FROM DISK = 'D:\BK_DataDB_2020\AppDb.bak'
WITH
    MOVE 'AppDb' TO 'D:\DataDB_2020\AppDb.mdf',
    MOVE 'AppDb_log' TO 'D:\DataDB_2020\AppDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE AssociationAcctDb
FROM DISK = 'D:\BK_DataDB_2020\AssociationAcctDb.bak'
WITH
    MOVE 'AssociationAcctDb' TO 'D:\DataDB_2020\AssociationAcctDb.mdf',
    MOVE 'AssociationAcctDb_log' TO 'D:\DataDB_2020\AssociationAcctDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE AuctionDb
FROM DISK = 'D:\BK_DataDB_2020\AuctionDb.bak'
WITH
    MOVE 'AuctionDb' TO 'D:\DataDB_2020\AuctionDb.mdf',
    MOVE 'AuctionDb_log' TO 'D:\DataDB_2020\AuctionDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE AuctionMasterDb
FROM DISK = 'D:\BK_DataDB_2020\AuctionMasterDb.bak'
WITH
    MOVE 'AuctionMasterDb' TO 'D:\DataDB_2020\AuctionMasterDb.mdf',
    MOVE 'AuctionMasterDb_log' TO 'D:\DataDB_2020\AuctionMasterDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE AuctionSearchDb
FROM DISK = 'D:\BK_DataDB_2020\AuctionSearchDb.bak'
WITH
    MOVE 'AuctionSearchDb' TO 'D:\DataDB_2020\AuctionSearchDb.mdf',
    MOVE 'AuctionSearchDb_log' TO 'D:\DataDB_2020\AuctionSearchDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE BanDb
FROM DISK = 'D:\BK_DataDB_2020\BanDb.bak'
WITH
    MOVE 'BanDb' TO 'D:\DataDB_2020\BanDb.mdf',
    MOVE 'BanDb_log' TO 'D:\DataDB_2020\BanDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE BlGame
FROM DISK = 'D:\BK_DataDB_2020\BlGame.bak'
WITH
    MOVE 'BlGame' TO 'D:\DataDB_2020\BlGame.mdf',
    MOVE 'BlGame_log' TO 'D:\DataDB_2020\BlGame_log.ldf',
    REPLACE,
    STATS = 10;
	
RESTORE DATABASE ContentBanDb
FROM DISK = 'D:\BK_DataDB_2020\ContentBanDb.bak'
WITH
    MOVE 'ContentBanDb' TO 'D:\DataDB_2020\ContentBanDb.mdf',
    MOVE 'ContentBanDb_log' TO 'D:\DataDB_2020\ContentBanDb_log.ldf',
    REPLACE,
    STATS = 10;	

RESTORE DATABASE CouponDb
FROM DISK = 'D:\BK_DataDB_2020\CouponDb.bak'
WITH
    MOVE 'CouponDb' TO 'D:\DataDB_2020\CouponDb.mdf',
    MOVE 'CouponDb_log' TO 'D:\DataDB_2020\CouponDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE DeliveryDb
FROM DISK = 'D:\BK_DataDB_2020\DeliveryDb.bak'
WITH
    MOVE 'DeliveryDb' TO 'D:\DataDB_2020\DeliveryDb.mdf',
    MOVE 'DeliveryDb_log' TO 'D:\DataDB_2020\DeliveryDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE FriendDb
FROM DISK = 'D:\BK_DataDB_2020\FriendDb.bak'
WITH
    MOVE 'FriendDb' TO 'D:\DataDB_2020\FriendDb.mdf',
    MOVE 'FriendDb_log' TO 'D:\DataDB_2020\FriendDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE GameWarehouseDb
FROM DISK = 'D:\BK_DataDB_2020\GameWarehouseDb.bak'
WITH
    MOVE 'GameWarehouseDb' TO 'D:\DataDB_2020\GameWarehouseDb.mdf',
    MOVE 'GameWarehouseDb_log' TO 'D:\DataDB_2020\GameWarehouseDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE GlobalNameDb
FROM DISK = 'D:\BK_DataDB_2020\GlobalNameDb.bak'
WITH
    MOVE 'GlobalNameDb' TO 'D:\DataDB_2020\GlobalNameDb.mdf',
    MOVE 'GlobalNameDb_log' TO 'D:\DataDB_2020\GlobalNameDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE GMToolLogDb
FROM DISK = 'D:\BK_DataDB_2020\GMToolLogDb.bak'
WITH
    MOVE 'GMToolLogDb' TO 'D:\DataDB_2020\GMToolLogDb.mdf',
    MOVE 'GMToolLogDb_log' TO 'D:\DataDB_2020\GMToolLogDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE GoodsDb
FROM DISK = 'D:\BK_DataDB_2020\GoodsDb.bak'
WITH
    MOVE 'GoodsDb' TO 'D:\DataDB_2020\GoodsDb.mdf',
    MOVE 'GoodsDb_log' TO 'D:\DataDB_2020\GoodsDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE GradeMembersDb
FROM DISK = 'D:\BK_DataDB_2020\GradeMembersDb.bak'
WITH
    MOVE 'GradeMembersDb' TO 'D:\DataDB_2020\GradeMembersDb.mdf',
    MOVE 'GradeMembersDb_log' TO 'D:\DataDB_2020\GradeMembersDb_log.ldf',
    REPLACE,
    STATS = 10;
	
RESTORE DATABASE GradeSubscriptionDb
FROM DISK = 'D:\BK_DataDB_2020\GradeSubscriptionDb.bak'
WITH
    MOVE 'GradeSubscriptionDb' TO 'D:\DataDB_2020\GradeSubscriptionDb.mdf',
    MOVE 'GradeSubscriptionDb_log' TO 'D:\DataDB_2020\GradeSubscriptionDb_log.ldf',
    REPLACE,
    STATS = 10;	

RESTORE DATABASE LevelDb
FROM DISK = 'D:\BK_DataDB_2020\LevelDb.bak'
WITH
    MOVE 'LevelDb' TO 'D:\DataDB_2020\LevelDb.mdf',
    MOVE 'LevelDb_log' TO 'D:\DataDB_2020\LevelDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE LimitDb
FROM DISK = 'D:\BK_DataDB_2020\LimitDb.bak'
WITH
    MOVE 'LimitDb' TO 'D:\DataDB_2020\LimitDb.mdf',
    MOVE 'LimitDb_log' TO 'D:\DataDB_2020\LimitDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE LobbyDb
FROM DISK = 'D:\BK_DataDB_2020\LobbyDb.bak'
WITH
    MOVE 'LobbyDb' TO 'D:\DataDB_2020\LobbyDb.mdf',
    MOVE 'LobbyDb_log' TO 'D:\DataDB_2020\LobbyDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE ManagementDb
FROM DISK = 'D:\BK_DataDB_2020\ManagementDb.bak'
WITH
    MOVE 'ManagementDb' TO 'D:\DataDB_2020\ManagementDb.mdf',
    MOVE 'ManagementDb_log' TO 'D:\DataDB_2020\ManagementDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE MarketDb
FROM DISK = 'D:\BK_DataDB_2020\MarketDb.bak'
WITH
    MOVE 'MarketDb' TO 'D:\DataDB_2020\MarketDb.mdf',
    MOVE 'MarketDb_log' TO 'D:\DataDB_2020\MarketDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE MyAuctionSearchDb
FROM DISK = 'D:\BK_DataDB_2020\MyAuctionSearchDb.bak'
WITH
    MOVE 'MyAuctionSearchDb' TO 'D:\DataDB_2020\MyAuctionSearchDb.mdf',
    MOVE 'MyAuctionSearchDb_log' TO 'D:\DataDB_2020\MyAuctionSearchDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PlatformAcctDb
FROM DISK = 'D:\BK_DataDB_2020\PlatformAcctDb.bak'
WITH
    MOVE 'PlatformAcctDb' TO 'D:\DataDB_2020\PlatformAcctDb.mdf',
    MOVE 'PlatformAcctDb_log' TO 'D:\DataDB_2020\PlatformAcctDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PlatformGameDb
FROM DISK = 'D:\BK_DataDB_2020\PlatformGameDb.bak'
WITH
    MOVE 'PlatformGameDb' TO 'D:\DataDB_2020\PlatformGameDb.mdf',
    MOVE 'PlatformGameDb_log' TO 'D:\DataDB_2020\PlatformGameDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PlatformMasterDb
FROM DISK = 'D:\BK_DataDB_2020\PlatformMasterDb.bak'
WITH
    MOVE 'PlatformMasterDb' TO 'D:\DataDB_2020\PlatformMasterDb.mdf',
    MOVE 'PlatformMasterDb_log' TO 'D:\DataDB_2020\PlatformMasterDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PlatformSessionDb
FROM DISK = 'D:\BK_DataDB_2020\PlatformSessionDb.bak'
WITH
    MOVE 'PlatformSessionDb' TO 'D:\DataDB_2020\PlatformSessionDb.mdf',
    MOVE 'PlatformSessionDb_log' TO 'D:\DataDB_2020\PlatformSessionDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PlatformSlotDb
FROM DISK = 'D:\BK_DataDB_2020\PlatformSlotDb.bak'
WITH
    MOVE 'PlatformSlotDb' TO 'D:\DataDB_2020\PlatformSlotDb.mdf',
    MOVE 'PlatformSlotDb_log' TO 'D:\DataDB_2020\PlatformSlotDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PostOfficeDb
FROM DISK = 'D:\BK_DataDB_2020\PostOfficeDb.bak'
WITH
    MOVE 'PostOfficeDb' TO 'D:\DataDB_2020\PostOfficeDb.mdf',
    MOVE 'PostOfficeDb_log' TO 'D:\DataDB_2020\PostOfficeDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PrivacyDb
FROM DISK = 'D:\BK_DataDB_2020\PrivacyDb.bak'
WITH
    MOVE 'PrivacyDb' TO 'D:\DataDB_2020\PrivacyDb.mdf',
    MOVE 'PrivacyDb_log' TO 'D:\DataDB_2020\PrivacyDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE ProfileDb
FROM DISK = 'D:\BK_DataDB_2020\ProfileDb.bak'
WITH
    MOVE 'ProfileDb' TO 'D:\DataDB_2020\ProfileDb.mdf',
    MOVE 'ProfileDb_log' TO 'D:\DataDB_2020\ProfileDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PromotionStampDb
FROM DISK = 'D:\BK_DataDB_2020\PromotionStampDb.bak'
WITH
    MOVE 'PromotionStampDb' TO 'D:\DataDB_2020\PromotionStampDb.mdf',
    MOVE 'PromotionStampDb_log' TO 'D:\DataDB_2020\PromotionStampDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PurchaseAdminDb
FROM DISK = 'D:\BK_DataDB_2020\PurchaseAdminDb.bak'
WITH
    MOVE 'PurchaseAdminDb' TO 'D:\DataDB_2020\PurchaseAdminDb.mdf',
    MOVE 'PurchaseAdminDb_log' TO 'D:\DataDB_2020\PurchaseAdminDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE PurchaseDb
FROM DISK = 'D:\BK_DataDB_2020\PurchaseDb.bak'
WITH
    MOVE 'PurchaseDb' TO 'D:\DataDB_2020\PurchaseDb.mdf',
    MOVE 'PurchaseDb_log' TO 'D:\DataDB_2020\PurchaseDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE RankingDb
FROM DISK = 'D:\BK_DataDB_2020\RankingDb.bak'
WITH
    MOVE 'RankingDb' TO 'D:\DataDB_2020\RankingDb.mdf',
    MOVE 'RankingDb_log' TO 'D:\DataDB_2020\RankingDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE RefundDb
FROM DISK = 'D:\BK_DataDB_2020\RefundDb.bak'
WITH
    MOVE 'RefundDb' TO 'D:\DataDB_2020\RefundDb.mdf',
    MOVE 'RefundDb_log' TO 'D:\DataDB_2020\RefundDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE ReportingDb
FROM DISK = 'D:\BK_DataDB_2020\ReportingDb.bak'
WITH
    MOVE 'ReportingDb' TO 'D:\DataDB_2020\ReportingDb.mdf',
    MOVE 'ReportingDb_log' TO 'D:\DataDB_2020\ReportingDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE RewardDb
FROM DISK = 'D:\BK_DataDB_2020\RewardDb.bak'
WITH
    MOVE 'RewardDb' TO 'D:\DataDB_2020\RewardDb.mdf',
    MOVE 'RewardDb_log' TO 'D:\DataDB_2020\RewardDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE RoleDb
FROM DISK = 'D:\BK_DataDB_2020\RoleDb.bak'
WITH
    MOVE 'RoleDb' TO 'D:\DataDB_2020\RoleDb.mdf',
    MOVE 'RoleDb_log' TO 'D:\DataDB_2020\RoleDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE ShowcaseDb
FROM DISK = 'D:\BK_DataDB_2020\ShowcaseDb.bak'
WITH
    MOVE 'ShowcaseDb' TO 'D:\DataDB_2020\ShowcaseDb.mdf',
    MOVE 'ShowcaseDb_log' TO 'D:\DataDB_2020\ShowcaseDb_log.ldf',
    REPLACE,
    STATS = 10;
	
RESTORE DATABASE SmartCouponDB
FROM DISK = 'D:\BK_DataDB_2020\SmartCouponDB.bak'
WITH
    MOVE 'SmartCouponDB' TO 'D:\DataDB_2020\SmartCouponDB.mdf',
    MOVE 'SmartCouponDB_log' TO 'D:\DataDB_2020\SmartCouponDB_log.ldf',
    REPLACE,
    STATS = 10;	

RESTORE DATABASE VirtualCurrencyDb
FROM DISK = 'D:\BK_DataDB_2020\VirtualCurrencyDb.bak'
WITH
    MOVE 'VirtualCurrencyDb' TO 'D:\DataDB_2020\VirtualCurrencyDb.mdf',
    MOVE 'VirtualCurrencyDb_log' TO 'D:\DataDB_2020\VirtualCurrencyDb_log.ldf',
    REPLACE,
    STATS = 10;

RESTORE DATABASE WarehouseDb
FROM DISK = 'D:\BK_DataDB_2020\WarehouseDb.bak'
WITH
    MOVE 'WarehouseDb' TO 'D:\DataDB_2020\WarehouseDb.mdf',
    MOVE 'WarehouseDb_log' TO 'D:\DataDB_2020\WarehouseDb_log.ldf',
    REPLACE,
    STATS = 10;
	
RESTORE DATABASE WishDb
FROM DISK = 'D:\BK_DataDB_2020\WishDb.bak'
WITH
    MOVE 'WishDb' TO 'D:\DataDB_2020\WishDb.mdf',
    MOVE 'WishDb_log' TO 'D:\DataDB_2020\WishDb_log.ldf',
    REPLACE,
    STATS = 10;	

