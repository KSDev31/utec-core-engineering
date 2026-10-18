#!/usr/bin/env python3
def uppercase(str):
    resultado = ""
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            resultado += chr(ord(i) - 32)
        else 
            resultado += i
    print("{}".format(resultado))