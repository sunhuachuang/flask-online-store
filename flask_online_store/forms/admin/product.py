from .. import BaseForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class ProductForm(BaseForm):
    name = StringField('name',
        validators=[
            DataRequired()
        ])

    description = TextAreaField('description',
        validators=[
            DataRequired()
        ])
