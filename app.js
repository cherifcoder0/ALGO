function isPrime(nbr) {
    if (nbr >= 2) {
        for (i = 2; i<=Math.sqrt(nbr) ; i++) {//si un nombre a un diviseur supérieur à sa racine carrée, il aura forcément un diviseur inférieur correspondant (les diviseurs vont par paires).
                                             // Donc inutile de tester jusqu’à nbr - 1, on s’arrête à √nbr.
            if (nbr % i == 0) {
                return false
            }
        }
        return true
    }
}

function getPrimeList(inf, sup) {
    list = []
    for (let i=inf; i<=sup; i++) {
        if (isPrime(i)) {
            list.push(i)
            
        }
    }
    return list
}

console.log(getPrimeList(1,21));
