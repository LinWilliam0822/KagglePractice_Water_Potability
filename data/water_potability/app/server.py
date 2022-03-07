# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 22:03:51 2022

@author: Owner
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:58:31 2022

@author: Owner
"""

from flask import Flask
# Request
from flask import request, redirect
from flask import render_template
import ML_model

app = Flask(__name__ ,static_folder='templates/')

# 路徑
# "/"
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/detect",methods=["POST"])
def detect():
    input_json = request.get_json()
    output_data = ML_model.DNN_model(input_json)
    
    return output_data

# 127.0.0.1:5000 ，5000是Flask自動指定
# 也可以自己指定 port (前提無其他程式正在使用這個port)
# 每訪問一次都會顯示一次訊息
if __name__ == "__main__":
    
    # 若有變更Code則自動重啟
    app.debug = True
    # 0.0.0.0 把本機位置公開
    app.run(host='0.0.0.0',port=5000)