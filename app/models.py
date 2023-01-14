import mongoengine as me


class Company(me.Document):
    # id = me.IntField()
    name = me.StringField(required=True)
    country_iso = me.StringField(null=True)
    city = me.StringField(null=True)
    nace = me.IntField(null=True)
    website = me.StringField(null=True)

    def __repr__(self):
        return self.name
