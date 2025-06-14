import socket
import threading

#Função para receber mensagens do servidor
def receber_mensagem(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("Conexão encerrada pelo servidor.")
                break
            print(f"\nRecebido: {data.decode('utf-8')}")
        except (ConnectionResetError, OSError):
            print("Conexão perdida.")
            sock.close()
            break



#Função para enviar mensagens do cliente para o servidor
def enviar_mensagem(sock):
    while True:
        try:
            mensagem = input("Digite sua mensagem (ou '/sair' para sair): ")
            if mensagem.strip().lower() == '/sair':
                sock.close()
                print("Conexão encerrada.")
                break
            sock.sendall(mensagem.encode('utf-8'))
        except (BrokenPipeError, OSError):
            print("Erro ao enviar mensagem. Conexão encerrada.")
            sock.close()
            break

#Função para iniciar o programa no modo servidor
def servidor(host ='localhost', porta =12345):
    #definindo o sockt tcp
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Ligando o socket a um endereço e porta específicos
    server_socket.bind((host, porta))
    server_socket.listen(1)
    print(f"Servidor escutando em {host}:{porta}...")
    conn, addr = server_socket.accept()
    print(f"Conexão estabelecida com {addr}")
    try:
        thread_envio = threading.Thread(target=enviar_mensagem, args=(conn,))
        thread_envio.start()
        while True:
            data = conn.recv(1024)
            if not data:
                print("Conexão encerrada pelo cliente.")
                break
            print(f"\nRecebido: {data.decode('utf-8')}")
    except (ConnectionResetError, OSError):
        print("Conexão perdida.")
    finally:
        conn.close()
        server_socket.close()
        print("Servidor encerrado.")


#Função para iniciar o programa no modo cliente
def cliente(host='localhost', porta=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, porta))
        print(f"Conectado ao servidor {host}:{porta}")
        thread_recebimento = threading.Thread(target=receber_mensagem, args=(client_socket,))
        thread_recebimento.start()
        enviar_mensagem(client_socket)
    except (ConnectionRefusedError, OSError):
        print("Não foi possível conectar ao servidor.")
    finally:
        client_socket.close()
        print("Cliente encerrado.")



#Função principal para escolher entre servidor e cliente
def main():
    modo = input("Digite 's' para servidor ou 'c' para cliente: ").strip().lower()
    if modo == 's':
        host = input("Digite o endereço do servidor (default: localhost): ") or 'localhost'
        porta = int(input("Digite a porta do servidor (default: 12345): ") or 12345)
        servidor(host, porta)
    elif modo == 'c':
        host = input("Digite o endereço do servidor: ")
        porta = int(input("Digite a porta do servidor: "))
        cliente(host, porta)
    else:
        print("Opção inválida. Por favor, escolha 's' ou 'c'.")
if __name__ == "__main__":
    main()