# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:09:27 2017

@author: ZHENGHAN ZHANG
"""

import flask

app = flask.Flask(__name__)


fp = open('list.txt','r')
a = fp.readlines()
n=''
for i in a:
    p = i.strip('\n')
    if p != '':
        if p[0] == ' ' and p[1] == 'o':
            p = '<ul style="list-style-type:circle">' + p
            p = p.replace(' o ', '<li>')
            p += '</li>'
            p += '</ul>'
    else:
        p += '<br>'
    n += p    
n = n.replace('</ul><ul style="list-style-type:circle">','')


@app.route('/')
def r():
    a = n
    return a

app.run(host='0.0.0.0', debug=True, threaded=True)
