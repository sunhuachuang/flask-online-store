import os
from flask_uploads import UploadSet, IMAGES

product_images_upload = UploadSet('productimages', IMAGES)

def delete_file(store, filename):
    os.remove(store.path(filename))
