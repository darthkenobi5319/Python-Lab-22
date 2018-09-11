# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:25:02 2017

@author: ZHENGHAN ZHANG
"""
import flask

app = flask.Flask(__name__)

#build a list of list,and loop it thru
listall=[[0,1,2,3,4,5,6,7,8,9,10]]
for i in range(1,11):
    n=[i]
    for j in range(10):
        n.append(i * listall[0][j+1])
    listall.append(n)
@app.route('/')
def r():
    a = '<table border=1>'
    for i in listall:
        a += '<tr>'
        for j in i:
            a += '<td>' + str(j)
    a += '</table>'
    return a

app.run(host='0.0.0.0', debug=True, threaded=True)