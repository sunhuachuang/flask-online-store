from . import db, addTimeToModel

@addTimeToModel
class ProductImage(db.Model):
    __tablename__ = 'product_images'

    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(80))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    # relations
    product = db.relationship("Product", back_populates="product_images")
