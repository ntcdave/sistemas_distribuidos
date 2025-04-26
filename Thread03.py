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
            tarefa = fila_de_tarefas(timeout = 10)
        except queue.Empty
            #quando a fila esvaziar por mais de 10s, a thread será finalizada.
            print(f'\n\n{nome} nenhuma tarefa na fila! Encerrando programa!\n\n')
            break
        

        #Simula o "processamento" da tarefa
        print(f'\nA tarefa {nome} está processando!')
        time.sleep(random.uniform(1,5))
        