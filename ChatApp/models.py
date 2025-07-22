from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

#テーブル.カラム作成
class User (db.Model):#db.ModelはSQLAlchemyが用意している親クラス　違うのを書いてしまうとただのpythonのクラスになる
    __tablename__ = 'users'#テーブル作成
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)#idカラム
    name = db.Column(db.String(255), nullable = False) #SQLAlchemyではVARCHARではなくString
    email = db.Column(db.String(255), nullable = False,unique=True)
    nickname = db.Column(db.String(255), nullable = False , unique=True)
    password = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.DateTime, nullable = True)
    updated_at = db.Column(db.DateTime, nullable = True)

    def __init__(self, name, email, nickname, password, created_at = None, updated_at = None):
        self.name = name
        self.email = email
        self.nickname = nickname
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()