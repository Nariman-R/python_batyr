from peewee import *

from app.dependencies import get_db


class Item(Model):
    title = CharField(verbose_name='title')
    price = DecimalField(verbose_name='price')
    category = CharField(verbose_name='category')
    image_url = CharField(verbose_name='image')
    description = CharField(verbose_name='description')
    
    class Meta:
        database = get_db()

class Payment(Model):
    item = ForeignKeyField(Item, verbose_name='item', backref='items')
    date = DateTimeField(verbose_name='date')
    status = CharField(verbose_name='status', default='new')
    is_issued = BooleanField(verbose_name="Error or not", default=False)

    class Meta:
        database = get_db()

if __name__ == '__main__':
    get_db().create_tables([Item, Payment])

    product1 = Item(title='Mars', price=3.2, category='Chocolate bar', image_url='', description='')
    product1.save()
