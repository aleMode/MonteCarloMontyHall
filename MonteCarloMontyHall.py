import random

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

def MonteCarlo(n):
    ripetizioni = 1000000000
    vittorie = 0

    print("\n-----------------------------------------------------------------------------------------------")
    print("Eseguendo la simulazione con ", ripetizioni, " ripetizioni e probabilità di cambiare pari a ", n)
    for i in range(ripetizioni):
        if i%1000000 == 0:
            print("iterazione: ", i)
        scelta_premio = random_choice()
        scelta_giocatore = random_choice()
        if switch(scelta_premio, scelta_giocatore, n):
            vittorie += 1

    rateo = vittorie / ripetizioni
    print("\nRateo di vittoria:", rateo)
    print("-----------------------------------------------------------------------------------------------")
    return rateo

with open("montecarlo_log.txt", "w") as f:
# Itera su tutti i valori da 0 a 1 con passo 0.1
    for n in range(0, 11):
        n = n / 10  # Converti l'indice in un valore compreso tra 0 e 1
        rateo = MonteCarlo(n)  # Esegui la simulazione con il valore corrente di n
        f.write(f"n={n:.1f}: Rateo di vittoria={rateo:.6f}\n")

#MonteCarlo()