import os
from sqlalchemy import create_engine, Column,Integer,String, or_,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

#DBファイル制作
base_dir = os.path.dirname(__file__)
#引数に渡したパスからファイルを除いたフォルダ名を返す(__file__)はdb。py
database = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
#base_dirとdata.sqliteを繋げて絶対パスを作る　SQLiteの接続先URLは'sqlite:///'＋絶対パス　これをdatabaseに代入

#データベースエンジンの作成
db_engine = create_engine(database ,echo=True)
#create_engineはエンジンを作る関数　第一引数は９行目で作ったdatabaseの情報が入っている
Base = declarative_base()
#テーブルのクラス作成に必要な関数　SQLAlchemyにクラスとして認識されテーブルが作られない

#テーブル.カラム作成
class User (Base):
    __tablename__ = 'users'#テーブル作成
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)#idカラム
    name = Column(String(255), nullable = False) #SQLAlchemyではVARCHARではなくString
    email = Column(String(255), nullable = False,unique=True)
    nickname = Column(String(255), nullable = False , unique=True)
    password = Column(String(255), nullable = False)
    created_at = Column(DateTime, nullable = False)
    updated_at = Column(DateTime, nullable = False)

#コンストラクタ　インスタンスの初期設定をする関数　例　キャラの名前をつける処理
    def __init__(self, name, email, nickname, password, created_at = None, updated_at = None):
        self.name = name
        self.email = email
        self.nickname = nickname
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
#表示用関数   
    def __str__(self):
        return f'user(名前:{self.name},メールアドレス:{self.email},ニックネーム:{self.nickname},パスワード:{self.password},登録日時:{self.created_at},更新日時:{self.updated_at})'

#セッションの生成
session_maker = sessionmaker(bind=db_engine)
session = session_maker()

Base.query = db_session.query_property()
#テーブル操作    
#Base.metadata.create_all(db_engine)
#user01 = User ('yuu', 'hjohs@gmail','masa', 'utyu')
#session.add_all([user01])
#session.commit()