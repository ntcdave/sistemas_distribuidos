import os
import multiprocessing
import math

 #função que verifica se um número é primo
def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
# função que determina (calcula)os números primos em um intervalo, organizando-os em uma fila.
def primos_range(start, end, queue):
    primos = [n for n in range(start, end) if primo(n)]
    queue.put(primos)

#função para dividir range de análise com base no número de processos
def dividir_range(total, num_processos):
    step = total // num_processos
    ranges = []
    for i in range(num_processos):
        start = i * step
        end = start + step if i < num_processos - 1 else total
        ranges.append((start, end))
    return ranges

#Função principal que cria os processos e organiza a fila de números primos
# para o usuário digitar o numero de processos, para dividir os processos.
def main():
    total = int(input("Digite o número máximo para encontrar primos: "))
    num_processos = int(input("Digite o número de processos a serem usados: "))
    
    ranges = dividir_range(total, num_processos)
    queue = multiprocessing.Queue()
    processos = []

    for start, end in ranges:
        p = multiprocessing.Process(target=primos_range, args=(start, end, queue))
        processos.append(p)
        p.start()
    for p in processos:
        p.join()

    primos = []
    while not queue.empty():
        primos.extend(queue.get())
    primos = sorted(set(primos))  # Remove duplicatas e ordena a lista
    print(f"Total de números primos encontrados: {len(primos)}")
    print(f"Números primos encontrados até {total}: {primos}")


if __name__ == "__main__":
    main()