import mongoengine as me

class Credentials(me.Document):
    
    email = me.StringField(required=True)
    password_hash = me.StringField(required=True)

    meta = {
        'collection': 'users'
    }
