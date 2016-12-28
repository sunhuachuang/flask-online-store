from .. import BaseForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class CategoryForm(BaseForm):
    name = StringField('name',
        validators=[
            DataRequired()
        ])

    description = TextAreaField('description',
        validators=[
            DataRequired()
        ])
