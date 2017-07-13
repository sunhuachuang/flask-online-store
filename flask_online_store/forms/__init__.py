from flask_wtf import FlaskForm
from flask import request


class BaseForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        if request.form and ('obj' in kwargs):
            obj = kwargs['obj']
            for field, value in request.form.items():
                if hasattr(obj, field):
                    setattr(obj, field, value)
        FlaskForm.__init__(self, *args, **kwargs)
