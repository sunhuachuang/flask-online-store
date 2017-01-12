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
