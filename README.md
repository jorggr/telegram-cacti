# Crear base de datos

```sql
CREATE TABLE IF NOT EXISTS plugin_telegram_bot (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    description varchar(255) NOT NULL,
    plugin_thold_log_id INT NOT NULL,
    telegram_date date default now()
);

INSERT INTO plugin_telegram_bot (description, plugin_thold_log_id) VALUES ('MESSAGE', 999999999999999);

SELECT plugin_thold_log.id, host.hostname, plugin_thold_log.description FROM plugin_thold_log INNER JOIN host ON host.id = plugin_thold_log.host_id WHERE plugin_thold_log.id NOT IN (SELECT plugin_thold_log_id FROM plugin_telegram_bot);
```

```
https://core.telegram.org/bots/api#getme

https://medium.com/@vipinc.007/python-a-database-interaction-class-using-pymysql-3338fb90f38c

https://pynative.com/python-mysql-select-query-to-fetch-data/

https://pynative.com/python-mysql-insert-data-into-database-table/

https://dev.mysql.com/doc/connector-python/en/connector-python-api-errors-error.html
```
