from asyncio import Queue
import random
import multiprocessing

import warnings

from matplotlib import pyplot as plt
warnings.filterwarnings("ignore")

def random_choice():
    #Restituisce una scelta casuale tra 0, 1 e 2
    return random.randint(0, 2)

def switch(porta_premio, porta_giocatore, n):
    if n == 0:
        if porta_premio != porta_giocatore:
            return False
        else:
            return True
    else:
        #se n = 1 rnd sarà sempre < 1 e quindi si cambierà ogni volta
        rnd = random.random()
        if rnd < n: 
            if porta_premio == porta_giocatore:
                return False
            else:
                return True

def monty_hall_simulation(num_simulations, switch_percentage, result_queue):
    vittorie = 0
    for i in range(num_simulations):
        scelta_premio = random_choice()
        scelta_giocatore = random_choice()
        if switch(scelta_premio, scelta_giocatore, switch_percentage):
            vittorie += 1
    print(vittorie)
    result_queue.put(switch_percentage, vittorie)  # Metti i risultati nella coda dei risultati
    

def parallel_monty_hall(num_simulations, switch_percentage, num_processes):
    result_queue = multiprocessing.Queue()  # Coda per i risultati
    processes = []
    for i in range(0,1001):
        process = multiprocessing.Process(
            target=monty_hall_simulation, 
            args=(num_simulations, i/1000, result_queue)
            )
        processes.append(process)
        process.start()


    for process in processes:
        process.join()  # Aspetta che tutti i processi terminino

    all_results = []
    while not result_queue.empty():
        all_results.append(result_queue.get())
    print(all_results)
    return all_results


def plottaMC():
    # Leggi il file e ottieni le probabilità di switch e i ratei di vittoria
    switch_probabilities = []
    win_rates = []

    with open('montecarlo_log2.txt', 'r') as file:
        for line in file:
            switch_prob, win_rate = line.strip().split(': ')
            switch_probabilities.append(float(switch_prob.split('=')[1]))
            win_rates.append(float(win_rate.split('=')[1]))

    # Crea il plot
    plt.plot(switch_probabilities, win_rates, marker='o', linestyle='-')

    # Etichette degli assi e titolo
    plt.xlabel('Probabilità di switch')
    plt.ylabel('Rateo di vittoria')
    plt.title('Rateo di vittoria in base alla probabilità di switch')

    # Mostra il plot
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    num_simulations = 1000000
    switch_percentage = 0.5
    num_processes = 10  # Numero di processi paralleli

    simulation_results = parallel_monty_hall(num_simulations, switch_percentage, num_processes)

    with open("montecarlo_log2.txt", "w") as f:
        for valore, risultato in simulation_results:
            f.write(f"n={valore:.6f}: Rateo di vittoria={risultato:.6f}\n")

    plottaMC()