# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:17:54 2019

@author: Joseph.Oladokun
"""

from flask import Flask, request

app = Flask(__name__)

@app.route ('/', methods=['POST'])

def add():
    a = request.args.get("a")
    b = request.args.get("b")
    
    return str( int(a) + int(b))

if __name__== '__main__':
    app.run()