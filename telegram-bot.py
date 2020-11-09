import os
import telegram
import mysql.connector as mysql_connector

from dotenv import load_dotenv


class MonitorTelegram:
    def __init__(self):
        """
        Inicializamos las variables
        """
        load_dotenv()
        self.host = os.getenv("HOST_DATABASE")
        self.database = os.getenv("NAME_DATABASE")
        self.user = os.getenv("USER_DATABASE")
        self.password = os.getenv("PASSWD_DATABASE")
        self.token = os.getenv("TOKEN_TELEGRAM")
        self.chat_id = os.getenv("GROUPID_TELEGRAM")

    def connect(self):
        """
        Creamos la conexión pasando los parametros de las
        variable virtuales
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
            print("Something went wrong: {}".format(Err.msg))

    def disconnect(self):
        """
        Terminar la conexión
        """
        self.connection.close()

    def fetch_all(self, sql):
        """
        Obtener todos los registros del query que se pase
        """
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.cursor.close()
            self.disconnect()
            return result
        except mysql_connector.Error as Err:
            print("Something went wrong: {}".format(Err.msg))

    def query_execution(self, sql):
        """
        Ejecute el query que te mande
        """
        try:
            self.connect()
            self.cursor.execute(sql)
            self.connection.commit()
            self.cursor.close()
            self.disconnect()
        except mysql_connector.Error as Err:
            print("Something went wrong: {}".format(Err.msg))

    def send_message(self, str_telegram, row_data):
        """
        Envia el mensaje de telegram y manda el registro
        a la base de datos que indica que ya fue notificado
        """
        try:
            bot = telegram.Bot(token=self.token)
            is_message_sent = bot.sendMessage(chat_id=self.chat_id, text=str_telegram)
            if is_message_sent:
                # si el mensaje fue enviado por el bot se registra en bd
                self.register_notification(row_data)
        except telegram.error.Unauthorized as msg_unauthorized:
            print("Token does not exist {}: ".format(msg_unauthorized))
        except telegram.error.BadRequest as chat_notfound:
            print("User ID or Group ID not found: {}".format(chat_notfound))
        except telegram.error.NetworkError:
            print("Cant establish connection error Network")

    def register_notification(self, row):
        """
        Todo lo que se notifica con el bot de telegram
        se registra en plugin_thold_log para mantener
        un historico de lo notificado
        """
        query = """INSERT INTO plugin_telegram_bot (description, plugin_thold_log_id) VALUES ('{}',{})""".format(
            row.get("description"), row.get("plugin_thold_log_id")
        )
        self.query_execution(query)

    def start_execute(self):
        """
        Obten lo notificado por el bot de telegram de la tabla
        Query: Obten todos los registros de la tabla plugin_thold_log (cacti)
        que no existan en la tabla plugin_telegram_bot (telegram bot)
        """
        query = (
            """SELECT plugin_thold_log.id, host.hostname, plugin_thold_log.description"""
            """ FROM plugin_thold_log INNER JOIN host ON host.id = plugin_thold_log.host_id"""
            """ WHERE plugin_thold_log.id NOT IN (SELECT plugin_thold_log_id FROM plugin_telegram_bot)"""
        )
        records = self.fetch_all(query)
        # itera cada registro obtenido
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
