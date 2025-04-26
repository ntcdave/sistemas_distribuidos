import threading #Biblioteca que permite manipular threads
import time      #Biblioteca para simular tarefas
import queue
import random
#-------------------------------------------------------------------------------
#Fila
fila_de_tarefas = queue.Queue()
#-------------------------------------------------------------------------------
#Função que simula a tarefa de cada thread
def trabalhador(nome):
    #Loop contínuo enquanto a fila não estiver vazia
    while True:
        try:
            #Tenta pegar tarefas da fila. Se a fila estiver vaziz por mais
            #de 10s, ocorrerá uma exceção.
            tarefa = fila_de_tarefas(timeout = 10)
        except queue.Empty:
            #Quando a fila esvaziar por mais de 10s, a thread será finalida
            print(f'\n\n{nome} nenhuma tarefa na fila! Encerrando o programa!\n\n')
            break
        
        #Simulando o "processamento" da tarefa
        print(f'\nA tarefa {nome} esta processando!')
        time.sleep(random.uniform(1,5))
        print(f'\nA tarefa {nome} concluida!')

        #Informando que a fila que a tarefa foi concluida
        fila_de_tarefas.task.done()
#-------------------------------------------------------------------------------
#Funções que será manipulada pelas threads
def tarefa(nome):
    print(f'\nIniciando a tarefa: {nome}')
    time.sleep(0.5); #Simula uma tarefa que demana 10s de execução
    print(f'Finalizando a tarefa: {nome}')
#-------------------------------------------------------------------------------
#Criando threads e preenchendo a fila com 10 tarefas iniciais ==
for i in range(1,11):
    fila_de_tarefas.put(f"Tarefa 1")

#Lista de Trabalhadores ========================================

print("\n\nTodas as threads foram finalizadas")
