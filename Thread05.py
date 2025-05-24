#Importação das bibliotecas
import threading
import time
import random
import multiprocessing

#Simular uma tarefa execudada por uma thread, como atender uma requisição
def tarefa(nome_no, id_thread):
    print(f"Thread {id_thread} iniciada no nó {nome_no}")
    tempo_execucao = random.randint(1, 3)  # Tempo de execução aleatório entre 1 e 5 segundos
    time.sleep(tempo_execucao)
    print(f"Thread {id_thread} finalizada no nó {nome_no} após {tempo_execucao} segundos")
#Implementando cada processo que simula um nó em um sistema distribuído
def no_distruibuido(nome_no):
    print(f"Nó {nome_no} iniciado (processo PID= multiprocessing.current_process().pid)")
    threads = []
    for i in range(3):  # Cada nó cria 3 threads
        t = threading.Thread(target=tarefa, args=(nome_no, i+1))
        t.start()
        threads.append(t)
    # Aguardar todas as threads terminarem
    for t in threads:
        t.join()
    print(f"Nó {nome_no} finalizado (processo PID= multiprocessing.current_process().pid)")

if __name__ == "__main__":
    #Simulando 2 nós no sistema distribuído
    nomes_nos = ["Nó A", "Nó B"]
    processos = []
    for nome_no in nomes_nos:
        p = multiprocessing.Process(target=no_distruibuido, args=(nome_no,))
        p.start()
        processos.append(p)
    # Aguardar todos os processos terminarem
    for p in processos:
        p.join()
    print("Todos os nós foram finalizados.")