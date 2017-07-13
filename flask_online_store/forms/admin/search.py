from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    key_words = StringField('keyWords',
                            validators=[
                                DataRequired(message=u'不能为空')
                            ],
                            render_kw={
                                'class': 'search-query',
                                'placeholder': u'搜索'
                            })
