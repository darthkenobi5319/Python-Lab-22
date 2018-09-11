# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:04:23 2017

@author: ZHENGHAN ZHANG
"""
import flask
import datetime

app = flask.Flask(__name__)

@app.route('/')
def r0():
    a = '<b>Choose One:</b>'
    a += '<br><a href="/currentyear">Current Year</a>'
    a += '<br><a href="/currentmonth">Current Month</a>'
    a += '<br><a href="/currentdate">Current Date</a>'
    a += '<br><a href="/ddmmyyyy">dd/mm/yyyy format</a>'
    a += '<br><a href="/currenthour">Current Hour</a>'
    a += '<br><a href="/currentminute">Current Minute</a>'
    a += '<br><a href="/currentsecond">Current Second</a>'
    a += '<br><a href="/hhmmss">hh:mm:ss format</a>'
    return a

@app.route('/currentyear')
def r1():
    i = datetime.datetime.now()
    a = '<b>Current Year : ' + str(i.year) + '</b>'
    a += '<br><a href="/">Return to Homepage </a>'
    return a

@app.route('/currentmonth')
def r2():
    i = datetime.datetime.now()
    a = '<b>Current Month : ' + str(i.month) + '</b>'
    a += '<br><a href="/">Return to Homepage </a>'
    return a

@app.route('/currentdate')
def r3():
    i = datetime.datetime.now()
    a = '<b>Current Date : ' + str(i.day) + '</b>'
    a += '<br><a href="/">Return to Homepage </a>'
    return a

@app.route('/ddmmyyyy')
def r4():
    i = datetime.datetime.now()
    a = '<b>dd/mm/yyyy format : ' + str(i.day) + '/' + str(i.month) + '/' + str(i.year) + '</b>'
    a += '<br><a href="/">Return to Homepage </a>'
    return a

@app.route('/currenthour')
def r5():
    i = datetime.datetime.now()
    a = '<b>Current Hour : ' + str(i.hour) + '</b>'
    a += '<br><a href="/">Return to Homepage </a>'
    return a

@app.route('/currentminute')
def r6():
    i = datetime.datetime.now()
    a = '<b>Current Minute : ' + str(i.minute) + '</b>'
    a += '<br><a href="/">Return to Homepage </a>'
    return a

@app.route('/currentsecond')
def r7():
    i = datetime.datetime.now()
    a = '<b>Current Second : ' + str(i.second) + '</b>'
    a += '<br><a href="/">Return to Homepage </a>'
    return a    

@app.route('/hhmmss')
def r8():
    i = datetime.datetime.now()
    a = '<b>hh:mm:ss format : ' + str(i.hour) + '/' + str(i.minute) + '/' + str(i.second) + '</b>'
    a += '<br><a href="/">Return to Homepage </a>'
    return a


app.run(host='0.0.0.0', debug = True, threaded = True)