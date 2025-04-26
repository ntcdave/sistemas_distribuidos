import threading #Biblioteca que permite manipular threads
import time      #Biblioteca para simular tarefas
import string
#Funções que será manipulada pelas threads =====================

def tarefa(nome):
    print(f'\nIniciando a tarefa: {nome}')
    print(f'\nTarefas tarefosas da Thread 1')
    time.sleep(0.5); #Simula uma tarefa que demana 10s de execução
    print(f'Finalizando a tarefa: {nome}')

def imprimirLetras(nome):
    print(f'\nIniciando a tarefa: {nome}')
    for letra in string.ascii_uppercase[:5]:
        print(f'Letra:{letra}',end='')
        time.sleep(0.5); #Simula uma tarefa que demana 10s de execução
    print(f'\nFinalizando a tarefa: {nome}')

def imprimirNumeros(nome):
    print(f'\nIniciando a tarefa: {nome}')
    for numero in range(1,6):
        print(f'\nNumero:{numero}')
        time.sleep(0.5); #Simula uma tarefa que demana 10s de execução
    print(f'\nFinalizando a tarefa: {nome}')     
    
#Criando threads ==============================================
thread_1 = threading.Thread(target=tarefa,         args = ("Thread 1",))
thread_2 = threading.Thread(target=imprimirLetras, args = ("Thread 2",))
thread_3 = threading.Thread(target=imprimirNumeros,args = ("Thread 3",))
    
#Iniciado as threads ==========================================
thread_1.start()
thread_2.start()
thread_3.start()

#Esperando as thread finalidas
thread_1.join()
thread_2.join()
thread_3.join()

print("\n\nTodas as threads foram finalizadas")
