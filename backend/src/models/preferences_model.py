import mongoengine as me

class Preferences(me.Document):
    user = me.ReferenceField("User", required=True)
    brands = me.ListField(me.StringField(), default=list)
    aesthetics = me.ListField(me.StringField(), default=list)
    celebrities = me.ListField(me.StringField(), default=list)
    colors = me.ListField(me.StringField(), default=list)

    meta = {
        'collection': 'preferences'
    }
