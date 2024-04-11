import threading
import time 
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

print("----------------------------------")
print("Dos hilos")

globalArrayNum = []
def contadorDos(inicio, fin):
    logging.info(f'Función con rango: {inicio} - {fin}')
    for i in range(inicio, fin+1, 1):
        globalArrayNum.append(i)
        time.sleep(0.01)
    return 0

t0 = time.time()
listaHilos = []
t = threading.Thread(target = contadorDos, args = (1,50))
listaHilos.append(t)
t.start() 

t = threading.Thread(target = contadorDos, args = (51,100))
listaHilos.append(t)
t.start()

for t in listaHilos:
    t.join() #unir hilos al principal
tf = time.time() 
print(f'Tiempo de ejecución: {tf} ')
print(globalArrayNum)

print("----------------------------------")
print("Pool de hilos")

def printHW():
    logging.info(f'Función HW')
    print("Hola mundo")

globalArrayNum = []
with ThreadPoolExecutor(max_workers= 2) as executor:
    inicio = 1
    hilos = 5
    fin = 200
    #subrango = 200//5
    subrango = fin // hilos
    for i in range (inicio, subrango, 50):
        executor.submit(contadorDos,inicio,fin)
        i+49

        
        
"""    executor.submit(contadorDos,1,50)
    executor.submit(contadorDos,51,100)
    executor.submit(contadorDos,101,150)
    executor.submit(contadorDos,151,200)
    executor.submit(printHW)"""

tf = time.time() - t0
print(globalArrayNum)
print(f'Tiempo de ejecución: {tf} ')
globalArrayNum.sort()
