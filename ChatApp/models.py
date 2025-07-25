from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin, LoginManager, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask

db = SQLAlchemy()

#テーブル.カラム作成
class User (db.Model, UserMixin):#db.ModelはSQLAlchemyが用意している親クラス　違うのを書いてしまうとただのpythonのクラスになる
    __tablename__ = 'users'#テーブル作成
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)#idカラム
    name = db.Column(db.String(255), nullable = False) #SQLAlchemyではVARCHARではなくString
    email = db.Column(db.String(255), nullable = False,unique=True)
    nickname = db.Column(db.String(255), nullable = False , unique=True)
    password = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.DateTime, nullable = True)
    updated_at = db.Column(db.DateTime, nullable = True)
    #パスワードをハッシュ化（werkzeug.securityを使用）
    def set_password(self, password):#引数に入力されたパスワードを渡す
        self.password = generate_password_hash(password)#generate_password_hashを使いハッシュ化しpasswordカラムに設定
    #入力されたパスワードとカラムに設定されたパスワードが同じかをチェック
    def check_password(self, password):
        return check_password_hash(self.password,password)
    

    def __init__(self, name, email, nickname, password, created_at = None, updated_at = None):
        self.name = name
        self.email = email
        self.nickname = nickname
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

