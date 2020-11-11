### Requirements

- python3.x
- pip

#### Create Backup your_cacti_database

#### Create new table

```sql
USE your_cacti_database;

CREATE TABLE IF NOT EXISTS plugin_telegram_bot (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    description varchar(255) NOT NULL,
    plugin_thold_log_id INT NOT NULL
);
```

```shell
[user@localhost~]# pip install virtualenv
[user@localhost~]# #cd ~ or cd /your/path
[user@localhost~]# virtualenv -p python3 virtualenv
```

#### Clone this repository into your virtualenv

```shell
[user@localhost~]# cd /path/to/virtualenv/
[user@localhost~]# git clone url_repo
[user@localhost~]# cd /path/to/virtualenv/telegrambot-cacti
[user@localhost~]# source /path/to/virtualenv/bin/activate
[user@localhost~]# pip install -r requirement.txt
[user@localhost~]# deactivate
```

#### Create new file name .env into /path/to/virtualenv/telegrambot-cacti/ and changue values .env

#### Create new cron / Execute every five minutes like poller.php cacti

```shell
[user@localhost~]# crontab -e

*/5 * * * * sh /path/to/virtualenv/telegrambot-cacti/execute.sh

[user@localhost~]# crontab -l
*/5 * * * * sh /path/to/virtualenv/telegrambot-cacti/execute.sh
```
