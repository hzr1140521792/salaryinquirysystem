#!/usr/bin/env python
from __future__ import unicode_literals
# -*- coding: utf-8 -*-
# @Date    : 2017-12-07 20:16:48
# @Author  : hanzhengrong (1140521792@qq.com)
# @Link    : http://hanzhengrong.cn/
# @Version : $Id$

import os
from flask import Flask
from flask import render_template,request
app = Flask(__name__)
import pymysql,json


def getMonth():
	conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='salary',charset='utf8')
	#创建游标
	cursor=conn.cursor()
	cursor.execute('select DISTINCT(month) from t_salary order by month asc')
	month=cursor.fetchall()
	conn.close()
	return month

@app.route('/')
def hello_world():
	# return "Hello World"
	#创建mysql数据库连接
	month=getMonth()
	return render_template('index.html',month=month)

@app.route('/<school_no>/<monthvalue>')
def getResult(school_no,monthvalue):
	print(school_no)
	#创建mysql数据库连接
	conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='salary',charset='utf8')
	#创建游标
	cursor=conn.cursor()
	#执行SQL语句,返回受影响的行数
	result_num=cursor.execute('select * from t_salary where school_no=%s and month=%s'%(school_no,monthvalue))
	result=cursor.fetchall()
	month=getMonth()
	json_result=json.dumps(result,ensure_ascii=False)
	conn.close()
	return render_template('index.html',result=result,month=month)

if __name__ == '__main__':
	app.debug=True
	app.run(host='0.0.0.0',port=80)