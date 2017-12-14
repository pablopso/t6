#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
import os
import gnupg
import json

DIRETORIO='/home/teste/gpghome'
SERVER='http://127.0.0.1:5000'


def criptografar(arquivo, destinatarios): #retorna o caminho do arquivo criptografado

    print("criptografando...")
    gpg = gnupg.GPG(gnupghome=DIRETORIO)

############################# teste
#    destinatarios=['teste@teste.com']
##

    with open(arquivo, 'rb') as f:
        status = gpg.encrypt_file(f, recipients=destinatarios,output=(arquivo+'.gpg'))
    print("o arquivo foi criptografado")
    return (arquivo+'.gpg')

def descriptografar(arquivo):
    senha=raw_input("digite sua senha descriptografar: ")
    print("descriptografando...")
    saida=arquivo[:-4]

    gpg = gnupg.GPG(gnupghome=DIRETORIO)
    with open(arquivo, 'rb') as f:
        status = gpg.decrypt_file(f, passphrase=senha, output=saida)
    print("o arquivo foi descriptografado")

def uploud(arquivo):
    print(arquivo)
    print("Fazendo uploud...")
    url=SERVER
    arq=open(arquivo,'rb')
    f={'file':arq}
    try:
        r=requests.post(url,files=f)
        print(r.text)
        print("uploud concluido.")
    except:
        print("nao eh possivel fazer uploud do arquivo...")
    finally:
	arq.close()

def download(arquivo): #retorna o caminho do arquivo baixado
    print("baixando arquivo...")

    url = str(SERVER+'/uploads/'+arquivo)
    arq_request = requests.get(url)
    arq_request.raise_for_status()
    f = open(arquivo, 'wb')
    for chunk in arq_request.iter_content(8192):
        f.write(chunk)
    f.close()
    print("download concluido.")
    return arquivo


def listar():
    url = str(SERVER+'/uploads/lista.json')
    response = requests.get(url)
    response.raise_for_status()
    dados = json.loads(response.text)
    response.close()
    for i in dados:
        print(i)



def enviar(lista):
    print(lista)
    if lista:
        arquivo=lista.pop()
    destinatarios=lista
    if destinatarios:
        uploud(criptografar(arquivo,destinatarios))
        os.remove(arquivo+'.gpg')
    else:
        print("e necessario que o arquivo e os destinatarios sejam informados")



def receber(arquivo):
    if arquivo:
        descriptografar(download(arquivo.pop()))
    else:
        print("o nome do arquivo deve ser passado como parametro...")

def shell():
    while 1:
        entrada=str(raw_input())
        argumentos=entrada.split()
        argumentos.reverse()
        comando=argumentos.pop()
        if comando=='listar':
            listar()
        elif comando=='receber':
            receber(argumentos)
        elif comando=='enviar':
            enviar(argumentos)
        elif comando=='sair':
            exit(1)
        else:
            print(comando,'nao e um comando valido')
        argumentos[:]=[]

shell()
