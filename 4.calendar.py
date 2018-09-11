# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:39:38 2017

@author: ZHENGHAN ZHANG
"""
import flask
import datetime
import calendar

app = flask.Flask(__name__)
  
@app.route('/')
def ri():
    a=''
    for b in range(1,13):  
        i = datetime.datetime.now()
        c = calendar.monthrange(i.year, b)
        if b == i.month:
            a += '<table border = 1>'
            a += '<tr>' + '<td>' * c[0]
            for j in range(7-c[0]):
                if j+1 == i.day:
                    a += '<td bgcolor="yellow">' + str(j+1)
                else:
                    a += '<td>' + str(j+1)
            m = (c[1]- 7 + c[0]) // 7
            n = (c[1]- 7 + c[0]) % 7
            l = 7-c[0]
            for x in range(m):
                a += '<tr>'
                for y in range(7):
                    l += 1
                    if l == i.day:
                        a += '<td bgcolor="yellow">' + str(l)
                    else:
                        a += '<td>' + str(l)
            if n > 0:
                a += '<tr>'
                for z in range(n):
                    l += 1
                    if l == i.day:
                        a += '<td bgcolor="yellow">' + str(l)
                    else:
                        a += '<td>' + str(l)
                a += '<td>' * (7-n)
            a += '</table>'
        else:
            a += '<table border = 1>'
            a += '<tr>' + '<td>' * c[0]
            for j in range(7-c[0]):
                a += '<td>' + str(j+1)
            m = (c[1]- 7 + c[0]) // 7
            n = (c[1]- 7 + c[0]) % 7
            l = 7-c[0]
            for x in range(m):
                a += '<tr>'
                for y in range(7):
                    l += 1
                    a += '<td>' + str(l)
            if n > 0:
                a += '<tr>'
                for z in range(n):
                    l += 1
                    a += '<td>' + str(l)
                a += '<td>' * (7-n)
            a += '</table>'
    return a
    
  
app.run(host='0.0.0.0', debug = True, threaded = True)

