from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from models import User, db
from flask_login import UserMixin, LoginManager, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

base_dir = os.path.dirname(__file__)#ファイルの作成
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///' + os.path.join(base_dir, 'data.sqlite')#データベースとの接続
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #今作ったデータが変更さえているか追跡している　メモリ消費、警告が出るので基本はFalse
db.init_app(app)


#ログインマネージャーの設定
app.config['SECRET_KEY'] = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))





#トップページの表示
@app.route('/', methods = ['GET'])
def top ():
    return render_template('top.html')





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
    new_user = User(name = name,email=email,nickname=nickname,password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    return render_template('mypage.html')
   
  
  

#ログインページの表示
#画面の取得なのでGETメソッド
@app.route('/login', methods=['GET'])
#ログイン画面の定義
#render_templateを使い、templatesフォルダ内のlogin.htmlが返る
def login_view():
    return render_template('login.html')


#ログイン処理
#データを送るのでPOSTメソッド
@app.route('/login', methods=['POST'])
def login_process():
    #ログイン画面のフォームに入力されたemailを取得しemail変数に代入
    email = request.form.get('email')
    #ログイン画面のフォームに入力されたpasswordを取得しpassword変数に代入
    password = request.form.get('password')
    #もしemailフォームとpasswordフォームのどちらかが空欄だったら、「空のメッセージがあります」と表示
    if email =='' or password =='':
        flash('空のフォームがあります')
    #emailとpasswordが両方入力されていたら、Userテーブルからemailが一致するユーザーを取得
    else:
        user = User.query.filter_by(email=email).first()
        #emailが一致しなければ
        if user is None:
            flash('このユーザーは存在しません')
        #emailが一致したら今度はpasswordが一致しているか確認する
        else:
            #入力されたパスワードをハッシュ化したものとDBに保存されているハッシュ化されたパスワードを比較
            if not check_password_hash(user.password, password):
                flash('パスワードが間違っています')
            #パスワードが一致したらセッションにログイン中のユーザー情報を保存
            else:
                login_user(user)
                #チャンネル画面に遷移
                return redirect(url_for('channels_view'))
        
        #ログインできなければログインページに遷移
        return redirect(url_for('login_view'))
        

#ログアウト処理
@app.route('/logout')
def logout():
    #セッションからログイン中のユーザー情報を削除
    logout_user()
    #ログインページに遷移
    return redirect(url_for('login_view'))

#チャンネル一覧ページの作成
@app.route('/channels', methods=['GET'])
def channels_view():
    #セッションから取得したuidをuid変数に代入
    uid = session.get('uid')
    #もしuidがなければ、ログインページに遷移
    if uid is None:
        return redirect(url_for('login_view'))
    #uidがあったらChannnelのデータを取得する
    else:
        channels = Channel.get_all()
        #チャンネル一覧ページを返す
        return render_template('channels.html', channels=channels)

#チャンネルの作成
@app.route('/channels', methods=['POST'])
def create_channel():
    #セッションから取得したuid
    uid = session.get('uid')
    #もしuidがなければ、ログインページに遷移
    if uid is None:
        return redirect(url_for('login_view'))
    #チャンネルを作成するためのフォーム（channelTitle）に入力された情報を取得し、channel_name変数に代入
    channel_name = request.form.get('channelTitle')
    #models.pyのChannelクラスから取得
    channel = Channel.query.filter_by(channel_name=channel_name).first()
    #channelがチャンネル一覧（登録済み）になければ
    if channel == None:
        #channnel_description（チャンネルの説明）フォームに入力された情報を取得し、channel_description変数に代入
        description = request.form.get('channelDescription')
        #Channlクラスにuserid,channel_name,channel_descriptionが登録される
        new_channel = Channel(name = name,description=description)
        db.session.add(new_channel)
        db.session.commit()
        #チャンネル一覧ページに遷移する
        return redirect(url_for('channels_view'))









  
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  