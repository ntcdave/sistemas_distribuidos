import threading
import queue
import time
import random

#Lista para armazenar as threads (trabalhadores)
threads = []  
#Criando uma fila com definição de prioridade
fila_de_tarefas = queue.PriorityQueue()
#--------------------------------------------------
#Função que simula a tarefa de cada thread
def trabalhador(nome):
    #Loop continuo enquanto fila não estiver vazia
    while True:
        try:
            #tentar pegar tarefa da fila. Se a fila estiver vazia por mais de 30 segundos, ocorrerá uma exceção.
            prioridade, tarefa = fila_de_tarefas.get(timeout=30)
        except queue.Empty:
            #quando a fila esvaziar por mais de 30s, a thread será finalizada.
            print(f'\n\n{nome} nenhuma tarefa na fila! Encerrando programa!\n\n')
            break
        #Simulando o "processamento" da tarefa
        print(f'\n\n{nome} está processando a tarefa {tarefa} com prioridade {prioridade}!')
        time.sleep(random.uniform(1, 5))
        print(f'\n{nome} concluí: {tarefa}')

        #Informando à fila que a tarefa foi concluída
        fila_de_tarefas.task_done()

#Preenchendo a fila com 10 tarefas iniciais(A - J) e informando
# as diferentes prioridades (1 = alta prioridade e 5 = baixa prioridade)
tarefas_com_prioridades = [
    (1, 'Tarefa A'),
    (2, 'Tarefa B'),
    (3, 'Tarefa C'),
    (4, 'Tarefa D'),
    (5, 'Tarefa E'),
    (1, 'Tarefa F'),
    (2, 'Tarefa G'),
    (3, 'Tarefa H'),
    (4, 'Tarefa I'),
    (5, 'Tarefa J')
]

for item in tarefas_com_prioridades:
    fila_de_tarefas.put(item)


#Criando 03 threads (trabalhadores) e inciando cada uma com atendimento de tarefas
for i in range(3):
    #Cada thread executa a função "trabalhador" com um nome diferente
    t = threading.Thread(target=trabalhador, args=(f'Thread {i + 1}',))
    #Inicia a thread
    t.start()
    threads.append(t)  # Armazenando e gerenciamento na lista a thread em execução
#Gerenciando quando todas as tarefas da fila foram marcadas como concluídas
fila_de_tarefas.join()
#Finalizando quando a fila estiver tolalmente vazia(sem demanda)
print('\n\nTodas as tarefas foram processadas com sucesso!\n\n')
#--------------------------------------------------""