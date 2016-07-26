from os import getenv
import pymssql 
from time import sleep

print ("hola")
sleep(2)

server = 'EXP-AXPOS10'
user = 'PythonNeto'
password = '1234qwerASDF'
base = 'StoragePython'

conn = pymssql.connect(server, user, password, base)
cursor = conn.cursor()
"""cursor.executemany("INSERT INTO Clientes VALUES (%s, %s, %d, %s)",[('Ernesto', 'Solis', '12','Masculino')])
conn.commit()"""

print ("Termino")
cursor.execute('SELECT * FROM Clientes')

for row in cursor:
    print('row = %r' % (row,))
conn.close()
sleep(10)