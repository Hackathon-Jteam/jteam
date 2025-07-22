from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from models import User , db
app = Flask(__name__)

base_dir = os.path.dirname(__file__)#ファイルの作成
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///' + os.path.join(base_dir, 'data.sqlite')#データベースとの接続
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #今作ったデータが変更さえているか追跡している　メモリ消費、警告が出るので基本はFalse

db = SQLAlchemy(app)





















#サインアップページの表示
@app.route('/signup', methods = ['GET'])
def signup ():
    return render_template('signup.html')

#サインアップの処理
@app.route('/signup', methods = ['POST'])
def signup_process():
    name = request.form['name']
    email = request.form['email']
    nickname = request.form['nickname']
    password = request.form['password']
    new_user = User(name = name,email=email,nickname=nickname,password=password)
    db.session.add(new_user)
    db.session.commit()
    return render_template('mypage.html')
   
  
  
  
  
  
  
  
  
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  