import calendar
import datetime
import os
import logging.config
import re

from logging_config import LOGGING_CONFIG
from imap_tools import AND, MailBox

from config import mail_and_name, name_and_mail, year


IMAP: str = os.environ['SERVER_IMAP']
MAIL_USERNAME: str = os.environ['USERNAME_MAIL']
MAIL_PASSWORD: str = os.environ['PASS_MAIL']

list_data = []

debug_logger = logging.getLogger('log_debug')

class MoneyForMonth:
    def __init__(self, data: list):
        self.data = data
        self.message_list = []

    def create_list_of_data(self) -> list:
        month: int = int(self.data[0])
        start_day: int = int(self.data[1])
        day_finish: int = calendar.monthrange(year, month)[1] + 1
        return [datetime.date(year, month, day) for day in range(start_day, day_finish)]


    def request_messages_from_email(self) -> list:
        with MailBox(IMAP).login(MAIL_USERNAME, MAIL_PASSWORD) as mailbox:
            mailbox.folder.set('Отправленные')
            for day in self.create_list_of_data():
                for msg in mailbox.fetch(AND(date=day, text="гривен"), charset='utf-8'):
                    self.message_list.append([msg.uid, str(msg.date), msg.to, msg.text])
        return self.message_list


    @staticmethod
    def create_list_summ(temp_list: list) -> list:
        list_summ = []
        for msg in temp_list:
            money = re.search(r'\d{2,}', msg[3].split('гривен')[0])
            list_summ.append([msg[2][0], int(money.group())])
        return list_summ


    @staticmethod
    def create_output(data: list) -> dict:
        result = {}
        for email, amount in data:
            if email not in result:
                result[email] = [[], 0]
            result[email][0].append(amount)
            result[email][1] += amount
        return {mail_and_name.get(email): [values[0], values[1]] for email, values in result.items()}

    @staticmethod
    def format_output_translate(data: dict) -> str:
        return ''.join(
            f'<b><u>{office} </u></b>\n Суммы за период:  {str(money[0])[1:-1]}\n '
            f'Итоговая сумма за период:  <b><i>{money[1]}</i></b>\n'
            for office, money in data.items()
        )

    def request_summ(self) -> str:
        list_message = self.request_messages_from_email()
        messages = self.create_list_summ(list_message)
        output = self.create_output(messages)
        return self.format_output_translate(output)


class MoneyForPeriod(MoneyForMonth):

    def request_mail(self) -> list:
        mail: str = name_and_mail.get(self.data[2])
        # creating to connect to server
        with MailBox(IMAP).login(MAIL_USERNAME, MAIL_PASSWORD) as mailbox:
            # select the folder
            mailbox.folder.set('Отправленные')
            for _ in mail:
                for day in self.create_list_of_data():
                    for msg in mailbox.fetch(AND(date=day, text="гривен", to=_), charset='utf-8'):
                        self.message_list.append([msg.uid, str(msg.date), msg.to, msg.text])
        return self.message_list

    def create_list_of_data(self) -> list:
        list_of_days = []
        str_date:str = '.'.join(self.data[:2])
        today = datetime.datetime.today()
        date_:datetime = datetime.datetime.strptime(".".join([str(year),  str_date]), "%Y.%m.%date_")
        # creating a callendar
        while date_ <= today:
            list_of_days.append(datetime.datetime.date(date_))
            date_ += datetime.timedelta(days=1)
        return list_of_days




