import socket
import threading
import sys

# Função para enviar mensagens
def enviar_mensagens(sock):
    try:
        while True:
            msg = input()
            if msg.strip().lower() == '/sair':
                sock.close()
                print("Conexão encerrada.")
                break
            sock.sendall(msg.encode('utf-8'))
    except (BrokenPipeError, OSError):
        print("Falha ao enviar. Conexão encerrada.")
        sock.close()

# Função para receber mensagens
def receber_mensagens(sock):
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                print("Conexão encerrada pelo outro usuário.")
                sock.close()
                break
            print(f"\nRecebido: {data.decode('utf-8')}")
    except (ConnectionResetError, OSError):
        print("Conexão perdida.")
        sock.close()

# Função principal
def main():
    modo = input("Digite 's' para servidor ou 'c' para cliente: ").strip().lower()

    if modo == 's':
        host = '0.0.0.0'
        porta = int(input("Porta para escutar conexões: "))
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind((host, porta))
        servidor.listen(1)
        print(f"Aguardando conexão na porta {porta}...")
        conn, addr = servidor.accept()
        print(f"Conectado por {addr}")

        thread_envio = threading.Thread(target=enviar_mensagens, args=(conn,))
        thread_recebimento = threading.Thread(target=receber_mensagens, args=(conn,))

    elif modo == 'c':
        ip = input("IP do servidor: ").strip()
        porta = int(input("Porta do servidor: "))
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((ip, porta))
        print(f"Conectado ao servidor {ip}:{porta}")

        thread_envio = threading.Thread(target=enviar_mensagens, args=(cliente,))
        thread_recebimento = threading.Thread(target=receber_mensagens, args=(cliente,))

    else:
        print("Modo inválido. Use 's' para servidor ou 'c' para cliente.")
        return

    thread_envio.start()
    thread_recebimento.start()

    thread_envio.join()
    thread_recebimento.join()

if __name__ == '__main__':
    main()