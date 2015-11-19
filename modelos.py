#encoding: utf-8

import peewee
from datetime import datetime


db = peewee.SqliteDatabase('basedatos.sqlite')

class BaseModel(peewee.Model):
    class Meta:
        database = db

class Cliente(BaseModel):
    username = peewee.CharField(unique=True)
    password = peewee.CharField()
    fechaInscripcion = peewee.DateTimeField(default=datetime.now())
    baneado = peewee.BooleanField(default=False)

class Pedido(BaseModel):
    fechaPedido = peewee.DateTimeField(default=datetime.now())
    cliente = peewee.ForeignKeyField(Cliente, related_name='pedidos')

class Item(BaseModel):
    nombreProducto = peewee.StringField()
    description = peewee.StringField()
    precio = peewee.FloatField()

class ItemPedido(BaseModel):
    idPedido = peewee.ForeignKeyField(Pedido)
    idProducto = peewee.ForeignKeyField(Inventario)
    cantidad = peewee.IntegerField()


if __name__ == '__main__':
    db.create_tables([Cliente, Pedido, Inventario, ItemPedido])
