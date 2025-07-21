from flask import Flask, render_template, request
from db import User, database, session
from sqlalchemy import*
app = Flask(__name__)
db = sqlalchemy(app)





















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