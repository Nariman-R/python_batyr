from peewee import *
from environs import Env

environment = Env()
environment.read_env()

DB_NAME = environment('DB_NAME')
DB_URI =  environment('DB_URI')

db = PostgresqlDatabase(database=DB_NAME, dsn=DB_URI)
db.connect()


class Product(Model):
    name = CharField(verbose_name='наименование')
    type = CharField(verbose_name='категория')
    image_url = CharField(verbose_name='адрес изображения')
    price = DecimalField(verbose_name='стоимость')

    class Meta:
        database = db


if __name__ == '__main__':
    db.create_tables([Product])

    product1 = Product(name='Mars', type='Chocolate bar', image_url='', price=3.2)
    product1.save()
    #
    # user2 = User.create(first_name='Peter', last_name='Folin', age=30, is_ill=True)

    # for user in User.select():
    #     print(user.first_name, user.last_name)