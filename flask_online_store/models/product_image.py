from . import addTimeToModel, db, db_delete, db_commit
from ..utils.file_upload import product_images_upload, delete_file


@addTimeToModel
class ProductImage(db.Model):
    __tablename__ = 'product_images'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(80))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    # relations
    product = db.relationship("Product", back_populates="product_images")

    def save(self, filename, product_id):
        self.filename = filename
        self.product_id = product_id

        return self

    def get_image_url(self):
        return product_images_upload.url(self.filename)

    def delete_image(self):
        delete_file(product_images_upload, self.filename)
        db_delete(self)
        db_commit()
