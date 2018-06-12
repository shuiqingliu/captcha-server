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
        file_path = ""
        filenameArray = img.filename.split('.')

        if not os.path.exists(path):
            os.makedirs(path)

        if not os.path.isfile(path +img.filename):
            img.save(path + img.filename)
            file_path = path + img.filename
        else:
            img.save(path + filenameArray[0].strip() + "_." + filenameArray[1])
            file_path = path + filenameArray[0].strip() + "_." + filenameArray[1]
        print("uploaded image:" + img.filename)

        recResult  = imgrec(file_path)
        response['data'] = recResult['data']
        response['status'] = recResult["status"]
        response['message'] = recResult["message"]
        return jsonify(response)
    else:
        response['status'] = 405
        response['message'] = "不支持的方法"
        return jsonify(response)

from PIL import Image
from io import BytesIO
import base64
def imgrec(path):
    #read img
    image = Image.open(path)
    buffered = BytesIO()
    image.save(buffered,format="png")
    imgBase64Str = base64.b64encode(buffered.getvalue())

    #get image result
    url = GLOBAL["APIServer"] + imgBase64Str.decode("utf-8")
    resonse = requests.post(url)
    result = json.loads(resonse.text)
    print(result)
    return result
