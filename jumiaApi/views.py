
#from datetime import datetime
from flask import render_template
from jumiaApi import app
import mysql.connector
import io
import csv
import traceback
import os
import json
from flask import render_template
from flask import Flask,redirect,request,url_for,session,abort, Response
from flask import jsonify
import random
from jumiaApi.common.utils import *
from jumiaApi.common.jumiabot import *
import string
import time
import datetime
import schedule
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

config = {
  'user': 'cchap',
  'password': '9#ulJs64',
  'host': '163.172.192.138',
  'database': 'apicchap',
  'raise_on_warnings': True,
}


# @app.route('/',methods=["POST","GET"])
# def home():
#     try:
#         return render_template('index.html')
            
#     except:
#         return jsonify(apiResponse('201','Some internal error occurs ',responseData=[]))

@app.route('/jumia',methods=["POST","GET"])
def senddata():
    try:
        keyword = request.args['keywords']
        category = request.args['categorys']
        if category == '' or category == None:
            category = 'catalog'
        all_data_deals = scrapdatadeals(category,keyword)
        all_data_ = scrapdatajumia(keyword)
        all_deald_data = all_data_deals if all_data_deals else []
        all_ci_data = all_data_ if all_data_ else []
        join_data =  all_deald_data + all_ci_data
        connection = mysql.connector.connect(**config)
        connection.autocommit = True
        cursor = connection.cursor(dictionary=True)
        cursor.execute('TRUNCATE  searchdata')
        for one_data in join_data:
            if '✔' in one_data['Product_name']:
                Product_name = one_data['Product_name'].replace('✔','')
            else:
                Product_name = one_data['Product_name']
            cursor.execute("insert into searchdata (Product_name,Product_details,Product_image,Product_price,Product_url,Vender_name,Vender_location,Vender_contact,Site_name) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (Product_name,one_data['Product_details'],one_data['Product_image'],one_data['Product_price'],one_data['Product_url'],one_data['Vender_name'],one_data['Vender_location'],one_data['Vender_contact'],one_data['Site_name']))
            connection.commit()

        data = []
        data1 = []
        cursor.execute('select * from searchdata where Site_name="deals.jumia.ci" limit 10')
        data = cursor.fetchall()
        cursor.execute('select * from searchdata where Site_name="www.jumia.ci" limit 10')
        data1 = cursor.fetchall()
        cursor.close()
        connection.close()
        if data:
            jumiadeals = sorted(data, key = lambda i: eval(i['Product_price']),reverse=True)
        if data1:
            jumiaci = sorted(data1, key = lambda i: eval(i['Product_price']),reverse=True)
        
        return jsonify(apiResponse('200','Success',{'jumia_deals':jumiadeals,'jumia_ci':jumiaci}))
        # return render_template('index.html',data=data)
    except Exception as e:
        print("Error:"+str(e))
        return jsonify(apiResponse('201','Some internal error occurs',responseData=[]))
