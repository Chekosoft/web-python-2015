#encoding: utf-8

import peewee
from modelos import Cliente, Pedido, ItemPedido, db
from datetime import datetime

##Ejemplos de manejo de peewee.

"""Insertar filas en una tabla"""

#Se puede:
cliente = Cliente.create(username = u'Cheko', password = u'12345678')
#O también se puede:
otro_cliente = Cliente(username = 'Juanito', password = u'123456789')
otro_cliente.save()

"""Seleccionar filas"""

#Una fila:
cliente_analisis = Cliente.get(Cliente.username == u'Cheko')

#Una colección de filas
inscritos = Cliente.select().where(Cliente.fechaInscripcion <= datetime.now())
#Si select está vacío, entonces se seleccionan todos los campos de la tabla.

#Además, puedo seguir aplicando operaciones a esta colección
inscritos = inscritos.limit(15)

#Iterar sobre una colección de filas:
for inscrito in inscritos:
    print "idCliente: {}, nombreCliente: {}, baneado: {}".format(
        inscrito.username, inscrito.password, inscrito.baneado
    )


"""Modificar filas""":
#Una fila
cliente_analisis.username = u'Choko'
cliente_analisis.baneado = True
cliente_analisis.save()

##Multiples filas se modifican con lo siguiente:
"""
clientes_a_modificar = Cliente.update(Cliente.baneado = False)
.where(Cliente.baneado == True)
clientes_a_modificar.execute()
"""

"""Borrar filas""":
#Borrar una fila
print otro_cliente.delete_instance() #Puede ser también una colección de filas

#Devuelve cuantos campos fueron borrados.

#Para varias filas: Se hace una selección con delete-where y luego se ejecuta
#el método execute sobre la colección
#Ejemplo:

"""
clientes_baneados = Cliente.delete().where(Cliente.baneado == True)
clientes_baneados.execute()
"""

"""JOINS"""
clientes_pedidos = (Cliente
                    .select(Cliente, Pedido)
                    .join(Pedido)
                    .join(ItemPedido)
                    .where(ItemPedido.cantidad >= 10)
                    )

for cliente in clientes_pedidos:
    print "Cliente: {}".format(Cliente.name)

#Devuelve los campos del Cliente y del Pedido cuyos pedidos tengan mas de 10 elementos.
#Lo mismo se aplica para relaciones muchos a muchos.


""" Conexiones explicitas """
db.connect() #Inicia una conexión explicita, se debe cerrar.
db.close() #Cierra una conexión

""" Transacciones """

db.connect()
try:
    with db.atomic() as transaction:
        User.create(username=u'Choko', password=u'1234567')
        transaction.commit() #Commit realiza los correspondientes cambios
except peewee.IntegrityError:
    print "El usuario Choko ya existe" #Al haber una excepción, se hace rollback.
db.close()

#Mas información en: http://peewee.readthedocs.org/en/latest/peewee/example.html
