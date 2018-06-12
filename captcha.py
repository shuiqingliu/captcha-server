from flask import (Flask,Blueprint, g,redirect,render_template,request,url_for,jsonify)
import json,os
import requests
from config import BASEDIR,GLOBAL

bp = Blueprint('captcha', __name__, url_prefix='/captcha')

@bp.route('/api',methods=['GET'])
def api():
    return render_template('captcha/api.html')

@bp.route('/test',methods=['GET','POST'])
def test():
    if request.method == 'POST':
        pass

    return render_template('captcha/test.html')

@bp.route('/api/upload', methods=['POST'])
def upload():
    response = {}
    if request.method == 'POST':
        img = request.files.get("file")
        path = BASEDIR + "/static/imgs/"
        file_path = path
        filenameArray = img.filename.split('.')

        if not os.path.exists(path):
            os.makedirs(path)

        if not os.path.isfile(file_path+img.filename):
            img.save(file_path + img.filename)
        else:
            img.save(file_path + filenameArray[0].strip() + "_." + filenameArray[1])
        print("uploaded image:" + img.filename)
        response['status'] = 200
        response['message'] = 'success'
        return jsonify(response)
    else:
        response['status'] = 405
        response['message'] = "不支持的方法"
        return jsonify(response)

# def imgrec(path):
#     #read img
#     #TODO：
#
#     url = GLOBAL["Server"]
#     resonse = requests.post(url)
#     result = json.loads(resonse.text)