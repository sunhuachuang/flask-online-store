from wtforms import BooleanField, DecimalField, IntegerField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired

from .. import BaseForm
from ...models import Category

class ProductForm(BaseForm):
    name = StringField('name',
        validators=[
            DataRequired()
        ])
    price = DecimalField('price',
        validators=[
            DataRequired()
        ])
    number = IntegerField('price',
        validators=[
            DataRequired()
        ])
    detail = TextAreaField('detail',
        validators=[
            DataRequired()
        ])
    tips = TextAreaField('tips',
        validators=[
            DataRequired()
        ])
    is_pub = BooleanField('is_pub')
    is_hot = BooleanField('is_hot')
    is_new = BooleanField('is_new')
    category_id = SelectField('category_id',
        choices=[(c.id, c.name) for c in Category.query.order_by('name')],
        validators=[
            DataRequired()
        ])
