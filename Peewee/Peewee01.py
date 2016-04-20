from peewee import SqliteDatabase, CharField, ForeignKeyField, Model


db = SqliteDatabase(':memory:')


class Person(Model):
    name = CharField()

    class Meta:
        database = db


class Address(Model):
    address = CharField()
    person = ForeignKeyField(Person)

    class Meta:
        database = db


Person.create_table()
Address.create_table()

p = Person(name='person')
p.save()
a = Address(address='address', person=p)
a.save()

person = Person.select().where(Person.name == 'person').get()
print(person.id, person.name)

address = Address.select().where(Address.person == person).get()
print(address.id, address.address)
