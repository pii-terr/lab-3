import random
import base64
import hashlib
import time
import math


def pihash(val_1):
    start_time = time.time()
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
    print("---Su Hash y tiempo es----")
    print(hex_mul)
    print("--- %s Segundos ---" % (time.time() - start_time))


def entropia(c):
    val_1=str(c)
    print(val_1)
    val_1_no=("".join(list(dict.fromkeys(val_1))))
    print(val_1_no)
    largo=len(val_1)
    largo=int(largo)
    base=len(val_1)
    base=int(base)
    base_log=math.log2(base)
    base_log=float(base_log)
    entropia=largo*base_log
    print("--- La entropia de su arreglo es")
    print(entropia)


val_1 = ""
print("Que accion desea hacer")
print(" 1: Analizar una entrada manual")
print(" 2: Analizar un documento")
print(" 3: Analizar un archivo de texto")
print(" 4: Analizar entropia de una entrada manual")
print(" 5: Analizar la entropia de documento")
print(" 6: Analizar entropia de archivo de texto")
entrada=input()
entrada=int(entrada)
if entrada == 2:
    print("Escriba nombre del documento con su extension")
    documento = input()
    f = open(str(documento), "r")
    val_1 = f
    pihash(val_1)
elif entrada == 1:
    print("Escriba su entrada")
    val_1 = input()
    pihash(val_1)
elif entrada == 3:
    print("Cuantas lineas de texto desea hashear")
    rango= input()
    print("Escriba nombre del documento con su extension")
    documento = input()
    
    f = open(documento, "r")
    i=0
    for x in f:
        val_1=print(x)
        val_1=x
        pihash(str(val_1))
        i=i+1
        if i==int(rango):
            break

elif entrada==4:
    print("Escriba su entrada")
    val_1 = input()
    entropia(val_1)
elif entrada == 5:
    print("Escriba nombre del documento con su extension")
    documento = input()
    f = open(str(documento), "r")
    val_1 = f
    entropia(val_1)
elif entrada == 6:
    print("Cuantas lineas de texto desea hashear")
    rango= input()
    print("Escriba nombre del documento con su extension")
    documento = input()
    
    f = open(documento, "r")
    i=0
    for x in f:
        val_1=print(x)
        
        i=i+1
        val_1=x
        entropia(val_1)
        if i==int(rango):
            break












    



