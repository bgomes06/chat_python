import banco
import threading

if __name__ == '__main__':
    user = input('Nickname: ')
    f = threading.Thread(target=banco.mostrar_mensagem)
    f.start()
    while f.isAlive:
        mens = input()
        banco.cadastrar(user, mens)
