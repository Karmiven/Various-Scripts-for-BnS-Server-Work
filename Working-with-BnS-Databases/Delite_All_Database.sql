-- Отключение внешних ключей и перевод всех баз в режим SINGLE_USER
EXEC sp_MSforeachdb 'IF DB_ID(''?'') > 4 BEGIN 
    ALTER DATABASE [?] SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
END';

-- Удаление всех баз данных, кроме системных
DECLARE @dbName NVARCHAR(MAX);
DECLARE db_cursor CURSOR FOR
SELECT name
FROM sys.databases
WHERE database_id > 4; -- Исключаем системные базы

OPEN db_cursor;
FETCH NEXT FROM db_cursor INTO @dbName;

WHILE @@FETCH_STATUS = 0
BEGIN
    DECLARE @sql NVARCHAR(MAX) = 'DROP DATABASE [' + @dbName + ']';
    PRINT 'Удаление базы данных: ' + @dbName;
    EXEC sp_executesql @sql;
    FETCH NEXT FROM db_cursor INTO @dbName;
END;

CLOSE db_cursor;
DEALLOCATE db_cursor;

PRINT 'Все пользовательские базы данных успешно удалены.';
