# your name
# your NetID
# your SBU ID number
# CSE 101
# Homework 3


# Part I
def frog(mood, actions):
    current_mood = mood;

    # empty lists
    if not actions:
        return 0

    for action in actions:
        if action == 'play':
            current_mood = current_mood + 2
        elif action == 'eat' and current_mood >= mood * 0.5:
            current_mood = current_mood
        elif action == 'eat' and current_mood < mood * 0.5:
            current_mood = current_mood - 3
        elif action == 'read' and current_mood >= mood * 0.75:
            current_mood = current_mood - 4
        elif action == 'read' and current_mood < mood * 0.75:
            current_mood = current_mood - 5
        elif action == 'work':
            current_mood = current_mood - 6
        else:
            current_mood = current_mood - 1

        if current_mood <= 0:
            return 0

    return current_mood


# Part II
def pacman(line):
    # empty line
    if not line:
        return ['<']

    pos = 0

    final_stats = line[:]

    while line[pos] not in 'GHOSTghost':

        final_stats[pos] = '_'
        pos = pos + 1
        if pos >= len(line):
            break

    if pos == 0:
        return ['<'] + line
    elif pos == len(line):
        return final_stats + ['<']
    else:
        final_stats[pos - 1] = '<'
        return final_stats


# Part III
def brackets(expr):
    L = [];
    for character in expr:
        if character in '{[(':
            L.append(character)
        elif character in '}])' and not L:
            return 'error'
        elif character == '}' and L[-1] == '{':
            L.pop()
        elif character == ']' and L[-1] == '[':
            L.pop()
        elif character == ')' and L[-1] == '(':
            L.pop()
        else:
            return L

    return L


# Part IV
def hail_length(n):
    length = 1
    while n != 1:
        length = length + 1

        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = n * 3 + 1

    return length


def siblings(length, maximum):
    L = []

    for i in range(1, maximum):
        if hail_length(i) == length:
            L.append(i)

    return sorted(L)


# Part V
def vampire_hunt(humans, vampires, hunters):
    while humans != 0 and vampires !=0:
        vampires = max(0, vampires - hunters)

        if humans - vampires <= 0:
            vampires = vampires + humans
            humans = 0
        else:
            humans = humans - vampires
            vampires = vampires * 2

    return [humans,vampires]
