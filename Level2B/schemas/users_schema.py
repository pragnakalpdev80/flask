from flask_marshmallow import Marshmallow
from marshmallow import ValidationError
from models.users import User

ma = Marshmallow()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True  
        exclude = ("password_hash",)  

