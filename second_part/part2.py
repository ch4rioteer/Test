#Необходимо создать функцию на python3, которая будет проверять 
#для каждого user, что есть запись для каждого дня в течении недели, 
#и если есть, то добавлять в другую таблицу user, message строку user, "есть запись".

import os
import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect(__file__.replace(os.path.basename(__file__),'part2.db'))
cursor = conn.cursor()

cursor.execute('SELECT DISTINCT user FROM reg_table')
users = cursor.fetchall()

for user in users:
    user = user[0]
    #Проверка наличия записей для каждого дня в течение недели
    counter = 0
    for i in range(7):
        check_date = (datetime.now() - timedelta(days=i)).strftime('%y%m%d')
        cursor.execute('SELECT COUNT(*) FROM reg_table WHERE user=? AND datastr LIKE ?', (user, f'{check_date}%'))
        counter += cursor.fetchone()[0]
    #Если есть записи для каждого дня в течение недели, добавляем запись во вторую таблицу
    if counter > 0:
        cursor.execute('INSERT INTO reg_ver (user, message) VALUES (?, ?)', (user, 'есть запись'))
#Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
