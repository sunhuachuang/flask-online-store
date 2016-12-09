from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,Length


class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(message= u'用户名不能为空')],
                           render_kw={'placeholder': u'用户名'})

    password = PasswordField('password',validators=[DataRequired(message= u'密码名不能为空')],
                             render_kw={'placeholder': u'密码'})

    submit_login = SubmitField('登录',render_kw={'class': 'btn'})


#不一定需要
class SearchForm(FlaskForm):
    key_words=StringField('搜索关键词',render_kw={'class': 'search-query', 'placeholder': u'搜索'})
    submit = SubmitField('搜索',render_kw={'class': 'btn'})



class RegisterForm(FlaskForm):
    username = StringField('username',
                           validators=[DataRequired(message=u'用户名不能为空')],
                           render_kw={'placeholder': u'用户名'})

    email = StringField(u'邮箱', validators=[DataRequired(message=u'邮箱不能为空'),
                                           Email(message=u'请输入有效的邮箱地址')],
                                 render_kw={'placeholder': u'Email'})

    password = PasswordField(u'输入密码',
                             validators=[DataRequired(message=u'密码不能为空'),Length(6,20)],
                             render_kw={'placeholder': u'Password'})

    password2 = PasswordField(u'重复密码',
                             render_kw={'placeholder': u'Password Again'})

    validate_code = StringField(u'验证码',
                                validators=[DataRequired(message=u'验证码不能为空')],
                                render_kw={'placeholder':u'请输入验证码'})

    submit_register = SubmitField(u'注册',render_kw={'class': 'btn'})






