from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    gender = CharField()
    age = IntegerField()
    class Meta:
        database = db # This model uses the "people.db" database.

class User(Model):
    nickname = CharField()
    name = CharField()
    password = CharField()
    email = CharField()
    birthplace = CharField()
    interest = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Anniversary (Model):
    date = DateField()
    name = CharField()
    description = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.create_tables([Person, User, Anniversary])
