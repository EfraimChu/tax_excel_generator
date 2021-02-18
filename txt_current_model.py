from peewee import *

database = MySQLDatabase('tax', **{'sql_mode': 'PIPES_AS_CONCAT', 'password': 'root123', 'charset': 'utf8',
                                   'use_unicode': True, 'user': 'root'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class TaxCurrentData(BaseModel):
    good = CharField(null=True)
    id = IntegerField(null=True)
    price = CharField(null=True)
    quantity = BigIntegerField(null=True)
    tax_code = CharField(null=True)
    unit = CharField(null=True)

    class Meta:
        table_name = 'tax_current_data'
        primary_key = False
