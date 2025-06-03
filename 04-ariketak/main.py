import os
import time

nombre = os.environ.get('IZENA', 'Ikaslea')
curso = os.environ.get('KURTSOA', 'Docker')

print(f"Kaixo {nombre}!")
print(f"Ongietorri {curso} kurtsora!")