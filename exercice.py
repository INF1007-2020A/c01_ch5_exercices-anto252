#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from typing import List


def convert_to_absolute() -> float:
    return abs(float(input('Entrer un nombre :')))


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOPQ', 'ack'
    result = []
    for i in range(0, len(prefixes)):
        name = prefixes[i] + suffixes
        result.append(name)
    return result


def prime_integer_summation() -> int:
    primes = []

    i = 2
    while len(primes) < 100:
        is_prime = True

        for divider in range(2, int(math.sqrt(i)) + 1):
            if i % divider == 0:
                is_prime = False
                
        if is_prime:
            primes.append(i)

        i += 1
    
    return sum(primes)


def factorial(number: int) -> int:
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i
    return fact


def use_continue() -> None:
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres premiers entre 0 et 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
