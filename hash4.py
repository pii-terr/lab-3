import random
import base64
import hashlib
import hashlib
import time
import math


val_1 = ""
print("Que accion desea hacer")
print(" 1: Analizar una entrada manual")
print(" 2: Analizar un documento")
print(" 3: Analizar un archivo de texto")
print(" 4: Analizar entropia de una entrada manual")
print(" 5: Analizar una entrada manual")
print(" 6: Analizar entropia de archivo de texto")
entrada=input()
entrada=int(entrada)
if entrada == 2:
    print("Escriba nombre del documento con su extension")
    documento = input()
    f = open(str(documento), "r")
    val_1 = f
elif entrada == 1:
    print("Escriba su entrada")
    val_1 = input()









start_time_pi = time.time()
#val_1 = input()
val_1 = str(val_1)
largo = len(val_1)

ass=""
hexx=""
binn=""



for  i in range(largo):
    a=val_1[i]
    val_1_as = ord(val_1[i])
    ass = ass+str(val_1_as)
    val_1_hex=hex(val_1_as)
    hexx = hexx+str(val_1_hex[2:])
    val_1_bin=bin(val_1_as)
    val_1_bin=val_1_bin[2:]
    binn=binn+str(val_1_bin)




in_ass = ass[::-1]
in_hexx = hexx[::-1]
in_binn = binn[::-1]


mul_ass=int(ass)*int(in_ass)
mul_ass=int(mul_ass)*int(mul_ass)*int(mul_ass)*int(mul_ass)*int(mul_ass)
hex_mul=hex(mul_ass)
hex_mul=hex_mul[2:]

#print(hex_mul)
while(len(hex_mul)<55):
    hex_mul=hex_mul+str(hex_mul[::-1])

hex_mul=hex_mul[0:55]
print(hex_mul)
print("--- %s Segundos ---" % (time.time() - start_time_pi))
start_time_sha1 = time.time()
hash_object_sha1 = hashlib.sha1(val_1.encode('utf-8'))
print(hash_object_sha1.hexdigest())
print("--- %s Segundos sha1---" % round((time.time() - start_time_sha1),10))
start_time_sha256 = time.time()
hash_object_sha256 = hashlib.sha256(val_1.encode('utf-8'))
print(hash_object_sha256.hexdigest())
print("--- %s Segundos sha256---" % round((time.time() - start_time_sha256),10))
start_time_md5 = time.time()
hash_object_md5 = hashlib.md5(val_1.encode('utf-8'))
print(hash_object_md5.hexdigest())
print("--- %s Segundos md5---" % round((time.time() - start_time_md5),10))

    



