#!/usr/bin/env python
import gammu
import xlrd, xlwt
import data_clients

sm = gammu.StateMachine()
sm.ReadConfig()
sm.Init()

wb_read = xlrd.open_workbook('D:/Program Files/Gammu/bin/clients.xlsx')
sheet = wb_read.sheet_by_index(0)
contacts = dict(zip(sheet.col_values(0, 0), sheet.col_values(1, 0)))
formated_contacts = data_clients.clients_dict(contacts)
chunk_contacts = data_clients.split_dict_equally(formated_contacts)
phone_numbers = chunk_contacts[2]

for key in phone_numbers:
    sms_message = {'Text': 'Название работает по обычному графику. Адрес', 'SMSC': {'Location': 1}, 'Number': phone_numbers[key], 'Coding': 'Unicode_No_Compression'}
    try:
        sm.SendSMS(sms_message)
        print(f'Отправлено на номер {phone_numbers[key]}')
    except:
        with open('D:/projects/sms/error_log.txt', 'a') as file: 
            file.write('\n' + phone_numbers[key])
for key in phone_numbers:
    sms_message = {'Text': 'Скидка на ремонт по коду Код. Телефон', 'SMSC': {'Location': 1}, 'Number': phone_numbers[key], 'Coding': 'Unicode_No_Compression'}
    try:
        sm.SendSMS(sms_message)
        print(f'Отправлено на номер {phone_numbers[key]}')
    except:
        with open('D:/projects/sms/error_log.txt', 'a') as file: 
            file.write('\n' + phone_numbers[key])