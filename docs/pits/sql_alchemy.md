关于sqlAlchemy这个包的填坑。

#### relations 关联表的设置问题。
关联表ontToMany之间使用的是
```
#products.py表 一对多
product_images = db.relationship('ProductImage', back_populates='product', lazy='dynamic')

#product_image表 多对一
product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
product = db.relationship("Product", back_populates="product_images")

```
使用的是 对象的名字来代表该表。 如ProductImage, Product, 这样使用的时候，必须确保改对象也在当前文件中， 如果是不同的文件，就需要将另一个文件导入。  
因此， 在最外层的__init__.py中统一导入了所有的对象。

