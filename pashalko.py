# -------------------------------------------------------------------------------------------------------------------- #
# 1
# data = list(map(str.strip, sys.stdin))

# def read_txt(txt):
#     with open(txt, "r") as file:
#         data = list(map(lambda x: x.strip(), file.readlines()))
#     return data
# -------------------------------------------------------------------------------------------------------------------- #
# 2
# import csv
# import json
#
# with open('houses.csv', encoding="utf8") as csvfile:
#     req = [row for row in csv.reader(csvfile, delimiter=';', quotechar='"')]
#
# ans = 0
#
# with open("unusual.json", "w") as jsonfile:
#     json.dump(ans, jsonfile)
# -------------------------------------------------------------------------------------------------------------------- #
# 3
# url = f"http://{server}:{port}"
# response = requests.get(url)
# json_response = response.json()
# -------------------------------------------------------------------------------------------------------------------- #
# 4
# import sqlite3
# con = sqlite3.connect(r"data\savings\starsRecorder.sqlite")
# cur = con.cursor()
# var 1
# def check_passing(whatLevel):
#     req = f"""SELECT isPassing FROM stars WHERE levelID = {whatLevel}"""
#     result = int(cur.execute(req).fetchone()[0])
#     return result
# var 2
# def get_human(user_id):
#     req = """SELECT name FROM people WHERE user_id = ?"""
#     return con.execute(req, (str(user_id),)).fetchone()[0]
# SELECT column_name(s)
# FROM table1
# INNER JOIN table2
# ON table1.column_name = table2.column_name;

# var 1
# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
# var 2
# def save_2_csv(self):
#     with open('results.csv', 'w', newline='') as csvfile:
#         writer = csv.writer(
#             csvfile, delimiter=';', quotechar='"',
#             quoting=csv.QUOTE_MINIMAL)
#         # Получение списка заголовков
#         writer.writerow(
#             [self.tableWidget.horizontalHeaderItem(i).text()
#              for i in range(self.tableWidget.columnCount())])
#         for i in range(self.tableWidget.rowCount()):
#             row = []
#             for j in range(self.tableWidget.columnCount()):
#                 item = self.tableWidget.item(i, j)
#                 if item is not None:
#                     row.append(item.text())
#             writer.writerow(row)
# -------------------------------------------------------------------------------------------------------------------- #
# 5
# import sqlite3
# from flask import Flask
#
# app = Flask(__name__)
#
#
# con = sqlite3.connect("boring.db")
# cur = con.cursor()
#
#
# def func(star):
#     req = f"""SELECT planet, climate_type FROM climate WHERE star = ?"""
#     result = cur.execute(req, (star, )).fetchall()
#     return result
#
#
# print(func(str("Kepler 22")))
# a = func(str("Kepler 22"))
#
# names = set([x[0] for x in a])
# print(names)
# d = {}
# for i in names:
#     d[i] = []
# for z in a:
#     d[z[0]] = list(set(d[z[0]] + [z[1]]))
#
#
# @app.route('/boring')
# def index():
#     return d
#
#
# if __name__ == '__main__':
#     app.run(port=8080, host='127.0.0.1')
