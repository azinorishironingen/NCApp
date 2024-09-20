from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    gender = CharField()
    age = IntegerField()
    class Meta:
        database = db # This model uses the "people.db" database.

class Person(Model):
    nickname = CharField()
    name = CharField()
    password = IntegerField()
        password = IntegerField()
        
    class Meta:
        database = db # This model uses the "people.db" database.
db.create_tables([Person])
Person.create(name="かずのり" , gender="男性" , age=11)
Person.create(name="あおい" , gender="女性" , age=13)
Person.create(name="たいき" , gender="男性" , age=4)
Person.create(name="せいいちろう" , gender="男性" , age=2)