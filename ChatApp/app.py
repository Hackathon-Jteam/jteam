from flask import Flask, render_template, request
app = Flask(__name__)
    





















#サインアップページの表示
@app.route('/signup', methods = ['POST'])
def signup ():
    return render_template('signup.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

#サインアップの処理
