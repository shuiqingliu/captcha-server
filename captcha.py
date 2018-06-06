from flask import (Flask,Blueprint, g,redirect,render_template,request,url_for)

bp = Blueprint('captcha', __name__, url_prefix='/captcha')

@bp.route('/api',methods=['GET'])
def api():
    return render_template('captcha/api.html')

@bp.route('/test',methods=['GET','POST'])
def test():
    if request.method == 'POST':
        pass

    return render_template('captcha/test.html')