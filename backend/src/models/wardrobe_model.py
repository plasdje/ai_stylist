import mongoengine as me

class Wardrobe(me.Document):
    user_id = me.ObjectIdField(required=True)
    items = me.ListField(me.ReferenceField('Item'), default=list)

    meta = {
        'collection': 'wardrobes'
    }
