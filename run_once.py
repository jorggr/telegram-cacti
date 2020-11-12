import sys
from telegram_bot import MonitorTelegram
import mysql.connector as mysql_connector


class OnceTime(MonitorTelegram):
    def create_table(self):
        """
        Create table contain history notifications been send by telegram bot
        """
        sql = (
            """CREATE TABLE IF NOT EXISTS plugin_telegram_bot ("""
            """id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"""
            """description varchar(255) NOT NULL,"""
            """plugin_thold_log_id INT NOT NULL);"""
        )

        try:
            self.connect()
            self.cursor.execute(sql)
            self.cursor.close()
            self.disconnect()
        except mysql_connector.Error as Err:
            print("{}".format(Err.msg))

    def syncronize_data(self):
        """
        Syncronize data from own cacti table <plugin_thold_log>
        to table contain history notifications <plugin_telegram_bot>
        """
        query = (
            """SELECT plugin_thold_log.id, host.hostname, plugin_thold_log.description"""
            """ FROM plugin_thold_log INNER JOIN host ON host.id = plugin_thold_log.host_id"""
            """ WHERE plugin_thold_log.id NOT IN (SELECT plugin_thold_log_id FROM plugin_telegram_bot)"""
        )

        records = self.fetch_all(query)

        for record in records:
            data = {
                "description": "{} {}".format(record[1], record[2]),
                "plugin_thold_log_id": record[0],
            }
            self.register_notification(data)


if __name__ == "__main__":
    once_time = OnceTime()
    once_time.create_table()
    once_time.syncronize_data()
