
def details():
    signup_dict = {}
    db = shelve.open('signup.db', 'r')
    signup_dict = db['SignUp']
    db.close()
    list = []
    for key in signup_dict:
        signup = signup_dict.get(key)
        list.append(signup)

    i = 0
    for a in values:
        i += 1

    return list

values = []

def write_list(list):
    jan_data = 0
    feb_data = 0
    march_data = 0
    april_data = 0
    may_data = 0
    june_data = 0
    july_data = 0
    august_data = 0
    september_data = 0
    october_data = 0
    november_data = 0
    december_data = 0

    for a in list:
        if a.get_date()[3:5] == "01":
            jan_data = jan_data + a.get_signup
        elif a.get_date()[3:5] == "02":
            feb_data = feb_data + float(a.get_amount)
        elif a.get_date()[3:5] == "03":
            feb_data = feb_data + float(a.get_amount)
        elif a.get_date()[3:5] == "04":
            feb_data = feb_data + float(a.get_amount)
        elif a.get_date()[3:5] == "05":
            feb_data = feb_data + float(a.get_amount)
        elif a.get_date()[3:5] == "06":
            feb_data = feb_data + float(a.get_amount)
        elif a.get_date()[3:5] == "07":
            feb_data = feb_data + float(a.get_amount)
        elif a.get_date()[3:5] == "08":
            feb_data = feb_data + float(a.get_amount)
        elif a.get_date()[3:5] == "09":
            feb_data = feb_data + float(a.get_amount)
        elif a.get_date()[3:5] == "10":
            feb_data = feb_data + float(a.get_amount)
        elif a.get_date()[3:5] == "11":
            feb_data = feb_data + float(a.get_amount)
        elif a.get_date()[3:5] == "12":
            feb_data = feb_data + float(a.get_amount)

    monthly_data = [jan_data, feb_data, march_data, april_data, may_data, june_data, july_data, august_data,
                    september_data, october_data, november_data, december_data]

    return monthly_data

import datetime
now = datetime.datetime.now()
print('***', now)
print('***', now.day, now.month, now.year)

# what is this detail function?

r_list = details()

i = 0

values = write_list(r_list)
for a in values:
    i += 1

from flask import Flask, render_template, request, redirect, url_for, flash, session, Markup
import shelve
app = Flask(__name__)
app.secret_key = 'SECRET_KEY'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

# values = [
#     967.67, 1190.89, 1079.75, 1349.19,
#     2328.91, 2504.28, 2873.83, 4764.87,
#     4349.29, 6458.30, 9907, 16297
# ]

values = [
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]


@app.route('/')
def line():
    line_labels = labels
    line_values = values

    signup_dict = {}
    db = shelve.open('signup.db', 'r')
    signup_dict = db['SignUp']
    db.close()
    lenVal = (len(signup_dict.keys()))

    return render_template('test.html', title='User Creation Statistics(Graph)', max=50, labels=line_labels, values=line_values, lenVal=lenVal)


if __name__ == '__main__':
    app.run()


