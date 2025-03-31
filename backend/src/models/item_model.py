import mongoengine as me

class Item(me.Document):
    
    user = me.ReferenceField("User", required=True)
    type = me.StringField(required=True)
    category = me.StringField(required=True)
    brand = me.StringField(required=True)
    color = me.ListField(me.StringField(), default=list)
    material = me.StringField()
    season = me.ListField(me.StringField(), default=list)
    style_tags = me.ListField(me.StringField(), default=list)
    image_url = me.StringField()
    
    meta = {
        'collection': 'items'
    }
