# wtforms flalk 结合的坑
#### 如果是一个select 表单， 内容是 sqlalchemy 的对象
```python
# productForm中的category设置方法
category_id = SelectField('category',
    choices=[(str(c.id), c.name) for c in Category.query.order_by('name')],
    validators=[
        DataRequired()
    ])
```
尤其注意的是， choices的value值必须设置为str类型, 因为form表单传送过来的是string, python是强类型的语言，所以用string对应。

#### fieldList的使用
``` python
# product_image中的设置
class MultiProductImageForm(BaseForm):
    images = FieldList(FileField('Image File',
        validators=[
            DataRequired(),
            ImageFileRequired()
        ]), min_entries=1)
```
`min_entries`这个参数必须是kw, 而且只能在初始时期绑定， 后期调用__init__方法绑定的话， 参数传递会有问题， 有机会重写一下， 或者重写它的 __new__方法。
总体来说这个包不够自动化，需要填的坑很多，慎用。
