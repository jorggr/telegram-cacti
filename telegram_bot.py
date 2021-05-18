import os
import telegram
import mysql.connector as mysql_connector

from dotenv import load_dotenv
from datetime import datetime


class MonitorTelegram:
    def __init__(self):
        """
        Initialize all variables
        """
        load_dotenv()
        self.host = os.getenv("HOST_DATABASE")
        self.database = os.getenv("NAME_DATABASE")
        self.user = os.getenv("USER_DATABASE")
        self.password = os.getenv("PASSWD_DATABASE")
        self.token = os.getenv("TOKEN_TELEGRAM")
        self.chat_id = os.getenv("GROUPID_TELEGRAM")
        self.message = "Something went wrong:"

    def connect(self):
        """
        Create the connection passing the parameters
        """
        try:
            self.connection = mysql_connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
            )
            self.cursor = self.connection.cursor()
        except mysql_connector.errors.ProgrammingError as Err:
            print("{} {}".format(self.message, Err.msg))

    def disconnect(self):
        """
        End the connection
        """
        self.connection.close()

    def fetch_all(self, query):
        """
        Get all the records of the query
        """
        try:
            self.connect()
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.cursor.close()
            self.disconnect()
            return result
        except mysql_connector.Error as Err:
            print("{} {}".format(self.message, Err.msg))

    def query_execution(self, sql):
        """
        Execute the query that is sent
        """
        try:
            self.connect()
            self.cursor.execute(sql)
            self.connection.commit()
            self.cursor.close()
            self.disconnect()
        except mysql_connector.Error as Err:
            print("{} {}".format(self.message, Err.msg))

    def send_message(self, str_telegram, row_data):
        """
        Send the telegram message then send the registration
        to the database indicating that it has already been notified
        """
        try:
            bot = telegram.Bot(token=self.token)
            is_message_sent = bot.sendMessage(chat_id=self.chat_id, text=str_telegram)
            if is_message_sent:
                # if the message was sent by the bot it is registered in bd
                self.register_notification(row_data)
        except telegram.error.Unauthorized as msg_unauthorized:
            print("Token does not exist {}: ".format(msg_unauthorized))
        except telegram.error.BadRequest as chat_notfound:
            print("User ID or Group ID not found: {}".format(chat_notfound))
        except telegram.error.NetworkError:
            time = datetime.now()
            now = time.strftime("%d %B %Y - %H:%M:%S")
            print("""{} - Can't establish connection error Network""".format(now))

    def register_notification(self, row):
        """
        everything notified is saved in its own history in the table plugin_telegram_bot
        """
        query = """INSERT INTO plugin_telegram_bot (description, plugin_thold_log_id) VALUES ('{}',{})""".format(
            row.get("description"), row.get("plugin_thold_log_id")
        )
        self.query_execution(query)

    def start_execute(self):
        """
        Get all the records from the plugin_thold_log table (cacti)
        that do not exist in the table plugin_telegram_bot (telegram bot)
        """
        query = (
            """SELECT plugin_thold_log.id, host.hostname, plugin_thold_log.description"""
            """ FROM plugin_thold_log INNER JOIN host ON host.id = plugin_thold_log.host_id"""
            """ WHERE plugin_thold_log.id NOT IN (SELECT plugin_thold_log_id FROM plugin_telegram_bot)"""
        )
        records = self.fetch_all(query)

        for record in records:
            to_telegram = "{} {}".format(record[1], record[2])
            to_row = {
                "description": "{} {}".format(record[1], record[2]),
                "plugin_thold_log_id": record[0],
            }
            self.send_message(to_telegram, to_row)


if __name__ == "__main__":
    monitor_telegram = MonitorTelegram()
    monitor_telegram.start_execute()
