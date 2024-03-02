import random

from matplotlib import pyplot as plt

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
        else:
            if porta_premio == porta_giocatore:
                return True
            else:
                return False


def MonteCarlo(n):
    ripetizioni = 1000000
    vittorie = 0

    print("\n-----------------------------------------------------------------------------------------------")
    print("Eseguendo la simulazione con ", ripetizioni, " ripetizioni e probabilità di cambiare pari a ", n)
    for i in range(ripetizioni):
        scelta_premio = random_choice()
        scelta_giocatore = random_choice()
        if switch(scelta_premio, scelta_giocatore, n):
            vittorie += 1

    rateo = vittorie / ripetizioni
    print("\nRateo di vittoria:", rateo)
    print("-----------------------------------------------------------------------------------------------")
    return rateo

def MCripetuto():
    with open("montecarlo_log.txt", "w") as f:
    # Itera su tutti i valori da 0 a 1 con passo 0.1
        for n in range(0, 1001):
            n = n / 1000  # Converti l'indice in un valore compreso tra 0 e 1
            rateo = MonteCarlo(n)  # Esegui la simulazione con il valore corrente di n
            f.write(f"n={n:.6f}: Rateo di vittoria={rateo:.6f}\n")

def plottaMC():
    # Leggi il file e ottieni le probabilità di switch e i ratei di vittoria
    switch_probabilities = []
    win_rates = []

    with open('montecarlo_log.txt', 'r') as file:
        for line in file:
            switch_prob, win_rate = line.strip().split(': ')
            switch_probabilities.append(float(switch_prob.split('=')[1]))
            win_rates.append(float(win_rate.split('=')[1]))

    # Crea il plot
    plt.plot(switch_probabilities, win_rates, marker='o', linestyle='-')

    # Etichette degli assi e titolo
    plt.xlabel('Probabilità di switch', fontsize = 18)
    plt.ylabel('Rateo di vittoria', fontsize = 18)
    plt.title('Rateo di vittoria in base alla probabilità di switch', fontsize = 18)

    # Mostra il plot
    plt.grid(True)
    plt.show()

#MCripetuto()
plottaMC()