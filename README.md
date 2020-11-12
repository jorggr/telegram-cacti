#### Sorry for the translation :bowtie:

### Only works with thold 1.0.4 plugin (tested with cacti 1.2.15)

#### Requirements

- Linux (tested in RHEL)
- python3.x
- pip
- Token Telegrambot
- ID User/Group Telegram
- virtualenv with python3

#### Create Backup cacti_database

#### Create your virtualenv

```shell
[user@localhost~]# cd ~
[user@localhost~]# pip install virtualenv
[user@localhost~]# virtualenv -p python3 virtualenv
```

#### Clone this repository into your virtualenv

```shell
[user@localhost~]# cd /path/to/virtualenv/
[user@localhost~]# git clone url_repo
```

#### Create new file name .env into /path/to/virtualenv/telegrambot-cacti/ and changue values .env take sample .env.example file

#### Activate virtualenv first time and running once time run_once.py file

```shell
[user@localhost~]# source /path/to/virtualenv/bin/activate
[user@localhost~] (virtualenv) # cd /path/to/virtualenv/telegrambot-cacti
[user@localhost~] ~/path/to/virtualenv/telegrambot-cacti (virtualenv) # pip install -r requirement.txt
[user@localhost~] ~/path/to/virtualenv/telegrambot-cacti (virtualenv) # python run_once.py
[user@localhost~] ~/path/to/virtualenv/telegrambot-cacti (virtualenv) # deactivate
[user@localhost~] ~/path/to/virtualenv/telegrambot-cacti (virtualenv) # cd ~
[user@localhost~]#
```

#### Create new cron / Execute every five minutes like poller.php cacti

```shell
[user@localhost~]# crontab -e

*/5 * * * * sh /path/to/virtualenv/telegrambot-cacti/execute.sh

[user@localhost~]# crontab -l
*/5 * * * * sh /path/to/virtualenv/telegrambot-cacti/execute.sh
```

#### How do I create a bot?

[Create new bots with BotFather :sunglasses:](https://core.telegram.org/bots#6-botfather)
