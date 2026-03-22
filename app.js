function isPrime(nbr) {
    if (nbr >= 2) {
        for (i = 2; i < nbr; i++) {
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
