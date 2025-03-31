import mongoengine as me

class Wishlist(me.Document):
    user_id = me.ObjectIdField(required=True)
    items = me.ListField(me.ReferenceField('Item'), default=list)

    meta = {
        'collection': 'wishlist'
    }
