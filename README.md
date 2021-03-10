### Works with thold 1.0.4 plugin (tested with cacti 1.2.15)

#### Sorry for the translation :bowtie:

#### How do I create a bot? :sunglasses:

- Create new bot
  [Create new bots with BotFather](https://core.telegram.org/bots#6-botfather)
- Create new group
- add new bot as administrator new group
- get Token bot
- get ID group

#### Requirements

- Linux (tested in RHEL and Centos)
- python3.x
- pip
- Token Telegrambot
- ID User/Group Telegram
- virtualenv with python3

#### Create Backup cacti_database

#### Access your database

```shell
[user@localhost~]# mysql -h hostname_ip -u username -p cacti_database
> USE cacti_database
# CREATE NEW USER
# GRANT PRIVILEGES TO USER
> exit
```

#### Create your virtualenv

```shell
[user@localhost~]# cd ~
[user@localhost~]# pip install virtualenv
[user@localhost~]# virtualenv -p python3 virtualenv
```

#### Clone this repository into your virtualenv

```shell
[user@localhost~]# cd ~/path/to/virtualenv/
[user@localhost ~/path/to/virtualenv]# git clone git@github.com:jorg-gr/telegrambot-cacti.git
```

#### Create new file name .env into /path/to/virtualenv/telegrambot-cacti/ and changue values .env take sample .env.example file

```shell
[user@localhost ~/path/to/virtualenv]# cd telegrambot-cacti
[user@localhost ~/path/to/virtualenv/telegrambot-cacti]# cp .env.example .env
[user@localhost ~/path/to/virtualenv/telegrambot-cacti]# # open .env file and replace environment variables one by one
```

#### Activate virtualenv first time and running once time run_once.py file

```shell
[user@localhost ~/path/to/virtualenv/telegrambot-cacti]# source /path/to/virtualenv/bin/activate
[user@localhost ~/path/to/virtualenv/telegrambot-cacti] (virtualenv) # pip install -r requirement.txt
[user@localhost ~/path/to/virtualenv/telegrambot-cacti] (virtualenv) # python run_once.py
[user@localhost ~/path/to/virtualenv/telegrambot-cacti] (virtualenv) # Check if the table <plugin_telegram_bot> has been created in the cacti_database
[user@localhost ~/path/to/virtualenv/telegrambot-cacti] (virtualenv) # deactivate
[user@localhost ~/path/to/virtualenv/telegrambot-cacti] (virtualenv) # # if you want to delete the run_once.py file you can
[user@localhost ~/path/to/virtualenv/telegrambot-cacti] # rm -f run_once.py
```

#### Create new cron / Execute every five minutes like poller.php cacti

```shell
[user@localhost ~/path/to/virtualenv/telegrambot-cacti] # crontab -e
[user@localhost ~/path/to/virtualenv/telegrambot-cacti] # # the execute.sh file is inside this repository, replace path
[user@localhost ~/path/to/virtualenv/telegrambot-cacti] # # add these lines inside the crontab and save

*/5 * * * * sh /path/to/virtualenv/telegrambot-cacti/execute.sh

[user@localhost ~/path/to/virtualenv/telegrambot-cacti] # crontab -l
*/5 * * * * sh /path/to/virtualenv/telegrambot-cacti/execute.sh

[user@localhost ~] # # Check if the cron runs correctly or if any problem arises

[user@localhost ~] # # Ubuntu / debian
[user@localhost ~] # tail -f /var/log/syslog

[user@localhost ~] # # Centos / RHEL
[user@localhost ~] # tail -f /var/log/cron
```
