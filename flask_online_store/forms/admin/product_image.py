from wtforms import FileField, FieldList, FormField
from wtforms.validators import DataRequired

from .. import BaseForm
from ...models import Product
from ...utils.wtforms_validators import ImageFileRequired

class ProductImageForm(BaseForm):
    image = FileField('Image File',
        validators=[
            DataRequired(),
            ImageFileRequired()
        ])


class MultiProductImageForm(BaseForm):
    images = FieldList(FileField('Image File',
        validators=[
            DataRequired(),
            ImageFileRequired()
        ]), min_entries=1)
