from math import sqrt


#### Fonction secondaire


def isprime(p):
    '''
    Verifie si un entier est un nombre premier ou pas

    Arg :
       p : nombre entier

    Return :
       retourne un booléen exprimant la vérité de « p est un nombre premier »

    >>> isprime(9)
    False
    >>> isprime(11)
    True
    '''
    premier = True
    for i in range(2,int(sqrt(p))+1):
        if p%i == 0:
            premier = False
    return premier
   

#### Fonction principale


def main():
    '''
    Permet d'afficher tout les nombres premiers dans l'intervalle 0,N
    
    Arg : 
       N : int
       
    Return : None
    
    >>>main(4)
    '1,2,3'
    '''

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
