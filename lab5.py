# your name
# your NetID
# your SBU ID number
# CSE 101
# Lab 5

def fizz_buzz(max_fizz_buzz, fizz, buzz):
    result = []
    n = 0
    while max_fizz_buzz > 0:

        n = n + 1

        if n % fizz == 0 and n % buzz == 0:
            result.append('fizzbuzz')
            max_fizz_buzz = max_fizz_buzz - 1
        elif n % fizz == 0 and n % buzz != 0:
            result.append('fizz')
        elif n % fizz != 0 and n % buzz == 0:
            result.append('buzz')
        else:
            result.append(n)

    return result


def mass_purchase(city, budget):
    result = []
    total = 0
    for i in range(0,len(city)):
        for j in range(0, len(city[i])):
            if total + city[i][j] <= budget:
                total = total + city[i][j]
                result.append([i,j])

    return result

