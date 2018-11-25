from pymongo import MongoClient, DESCENDING
import time

try:
    client = MongoClient()
    db = client['chat']
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

def cadastrar(nome, mensagem):
    date = {
        'nome': nome,
        'mensagem': mensagem,
        'hora': time.strftime("%d-%m-%Y %H:%M:%S")
    }
    db.chat.insert(date)

def mostrar_mensagem():
    ultimo = [x for x in db.chat.find().sort('id', DESCENDING)]
    while True:
        date = [x for x in db.chat.find().sort('id', DESCENDING)]
        if date != ultimo:
            ultimo = date
            print('[{}] {} : {} \n'.format(date[0]['hora'], date[0]['nome'],date[0]['mensagem']))
        time.sleep(2)
