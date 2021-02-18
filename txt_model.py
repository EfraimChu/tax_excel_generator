from peewee import *

database = MySQLDatabase('tax', **{'sql_mode': 'PIPES_AS_CONCAT', 'password': 'root123', 'charset': 'utf8',
                                   'use_unicode': True, 'user': 'root'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class TaxData(BaseModel):
    code_num = BigIntegerField(null=True)
    general_tax = CharField(null=True)
    id = IntegerField(null=True)
    remark = CharField(null=True)
    service_abb_name = CharField(null=True)
    service_name = CharField(null=True)
    small_tax = CharField(null=True)
    small_tax_code = CharField(null=True)
    tax_explan = CharField(null=True)
    tax_id = IntegerField(null=True)
    tax_key = CharField(null=True)

    class Meta:
        table_name = 'tax_data'
        primary_key = False
