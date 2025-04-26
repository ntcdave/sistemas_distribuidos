import threading #Biblioteca que permite manipular threads
import time      #Biblioteca para simular tarefas

#Função que será manipulada pelas threads =====================
def tarefa(nome):
    print(f'\nIniciando a tarefa: {nome}')
    time.sleep(10); #Simula uma tarefa que demana 10s de execução
    print(f'Finalizando a tarefa: {nome}')
    
    
#Criando threads ==============================================
thread_1 = threading.Thread(target=tarefa,args = ("Thread 1",))
thread_2 = threading.Thread(target=tarefa,args = ("Thread 2",))
thread_3 = threading.Thread(target=tarefa,args = ("Thread 3",))
    
#Iniciado as threads ==========================================
thread_1.start();
thread_2.start();
thread_3.start();

print("\n\nTodas as threads foram finalizadas")
