from werkzeug.security import generate_password_hash, check_password_hash
from  flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,PasswordField
from wtforms.validators import DataRequired, Length, ValidationError, Regexp
from models import User

#サインアップ入力フォーム定義
class Signup(FlaskForm):
    name = StringField("名前：",validators=[DataRequired('ユーザー名は必須です')])
    email = StringField("メールアドレス：", validators=[DataRequired(),Regexp(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", message="正しいメールアドレスの形式で入力してください")])
    nickname = StringField("ニックネーム：", validators=[DataRequired()])
    password = PasswordField("パスワード：", validators=[DataRequired(),Regexp(r"^(?=.*[a-zA-Z0-9_.+-]).{6,}$",message="半角英数字記号を含めて6文字以上で入力してください")])
    submit = SubmitField('サインアップ')
    def validate_nickname(self, nickname):
        user = User.query.filter_by(nickname = nickname.data).first() #入力されたニックネームを引く数へ渡しデータベースと比べる
        if user:
            raise ValidationError('そのニックネーム名はすでに使用されています')#同じニックネームならエラーを返す