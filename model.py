from flask import (Flask,Blueprint, g,redirect,render_template,request,url_for,jsonify)
import json,os
import requests
from config import BASEDIR,GLOBAL

modelbp = Blueprint('model', __name__, url_prefix='/model')
@modelbp.route('/info',methods=['GET'])
def info():
    return render_template('model/info.html')