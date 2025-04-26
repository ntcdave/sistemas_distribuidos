import threading 
import time
import queue
import random


fila_de_tarefas = queue.Queue()

#função que simula a tarefa de cada thread
def trabalhador(nome):
    #Loop continuo enquanto fila não estiver vazia
    while True:
        try:
            #Tentar pegar tarefa da fila. Se a fila estiver vazia por mais de 10 segundos, ocorrerá uma exceção.
            tarefa = fila_de_tarefas.get(timeout = 10)
        except queue.Empty:
            #quando a fila esvaziar por mais de 10s, a thread será finalizada.
            print(f'\n\n{nome} nenhuma tarefa na fila! Encerrando programa!\n\n')
            break
        

        #Simula o "processamento" da tarefa
        print(f'\nA tarefa {nome} está processando!')
        time.sleep(random.uniform(1,5))
        print(f'\nA tarefa {nome} finalizou!')


        #Informando que a fila que a tarefa foi finalizada
        fila_de_tarefas.task_done()

#Preechendo a fila com 10 tarefas inciais
#de "Tarefa 1" a "Tarefa 10"
for i in range(1, 11):
    fila_de_tarefas.put(f'Tarefa {i}')


#Lista para armazenar as threads (trabalhadores)
threads = []

#Criando 03 threads (trabalhadores) e inciando com um nome diferente
#Inciando atendimento de tarefs
for i in range(3):
    #Cada thread executa a função "trabalhador" com um nome diferente
    t = threading.Thread(target=trabalhador, args=(f'Thread {i+1}',))
    #Inicia a thread
    t.start()
    threads.append(t) #Armazenando e gerenciamento na lista a thread em execução

#Gerenciando quando todas as tarefas da fila foram marcadas como concluídas
fila_de_tarefas.join()

#Finalizando quando a fila estiver tolalmente vazia(sem demanda)
print('\n\nTodas as tarefas foram processadas com sucesso!\n\n')