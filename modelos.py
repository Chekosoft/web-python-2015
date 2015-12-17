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

    @property
    def is_anonymous(self):
        return False

    @property
    def is_active(self):
        return self.baneado

    @property
    def is_authenticated(self):
        return self.username != ''

    def get_id(self):
        return unicode(self.id)

class Pedido(BaseModel):
    fechaPedido = peewee.DateTimeField(default=datetime.now())
    cliente = peewee.ForeignKeyField(Cliente, related_name='pedidos')

class Inventario(BaseModel):
    nombreProducto = peewee.CharField()
    description = peewee.CharField()
    precio = peewee.FloatField()

class ItemPedido(BaseModel):
    idPedido = peewee.ForeignKeyField(Pedido)
    idProducto = peewee.ForeignKeyField(Inventario)
    cantidad = peewee.IntegerField()


if __name__ == '__main__':
    db.create_tables([Cliente, Pedido, Inventario, ItemPedido])
