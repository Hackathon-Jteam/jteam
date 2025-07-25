from flask import Flask, render_template, request
app = Flask(__name__)
    









#トップページの表示
@app.route('/', methods = ['GET'])
def top ():
    return render_template('top.html')





#サインアップページの表示
@app.route('/signup', methods = ['GET'])
def signup ():
    return render_template('signup.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

#サインアップの処理
