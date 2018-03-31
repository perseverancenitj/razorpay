import razorpay
import json
from flask import Flask, flash, redirect, render_template, request, session, url_for
import psycopg2
import urllib

#api key
import globalData
globalData.init()
key = 'rzp_test_zw6KM4FOmFlj3H'
secret = 'RAHkCH4lujRFAq3V931pE6Cs'

app = Flask(__name__, static_folder = "static",template_folder='templates')
client = razorpay.Client(auth=(key,secret))

conn = psycopg2.connect(host="tantor.db.elephantsql.com",database="xnokayxj", user="xnokayxj", password="M_Pslc43o7UDPq5rTRc9WlQbFaEN4IEa")
cur = conn.cursor()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        globalData.vehNum = request.form.get('vn')
        phone = request.form.get('phone')
        name = request.form.get('name')
        print(globalData.vehNum, name, phone)
        cur.execute("Select owner_name, no_plate, default_type, mobile, email,fine, paid  from Defaulters where no_plate = %s;", globalData.vehNum)
        query = cur.fetchone()
        return render_template("app.html",name=query)


@app.route('/app')
def app_create():
    cur.execute(
        "Select owner_name, no_plate, default_type, mobile, email,fine, paid  from Defaulters where no_plate = %s;",
        globalData.vehNum)
    query = cur.fetchone()
    return render_template('app.html',name=query)

if __name__ == '__main__':
    app.run()

cur.close()