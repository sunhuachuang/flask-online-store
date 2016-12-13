from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    username = StringField('username',
                           validators=[
                               DataRequired(message=u'用户名不能为空')
                           ],
                           render_kw={
                               'placeholder': u'用户名'
                           })

    email = StringField('email',
                        validators=[
                            DataRequired(message=u'邮箱不能为空'),
                            Email(message=u'请输入有效的邮箱地址')
                        ],
                        render_kw={
                            'placeholder': u'Email'
                        })

    password = PasswordField('password',
                             validators=[
                                 DataRequired(message=u'密码不能为空'),
                                 EqualTo('password_confirm', message='Passwords must match'),
                                 Length(6,20)
                             ],
                             render_kw={
                                 'placeholder': u'Password'
                             })

    password_confirm = PasswordField('repeat password',
                             render_kw={
                                 'placeholder': u'Password Again'
                             })

    validate_code = StringField('validate code',
                                validators=[
                                    DataRequired(message=u'验证码不能为空')
                                ],
                                render_kw={
                                    'placeholder':u'请输入验证码'
                                })
