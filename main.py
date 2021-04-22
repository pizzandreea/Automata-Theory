# project 1 DFA word validation

with open("input.txt", "r") as f:
    lines = f.read().split("\n")

of = open("output.txt", 'w')


def check(word):

    index = 0
    currentState = q0

    Course = list()
    Course.append(currentState)

    while index < len(word):
        if (currentState, word[index]) not in transitions:
            of.write("NU\n")
            return
        else:
            currentState = transitions[currentState, word[index]]
            index += 1
            Course.append(currentState)

    if currentState in F:
        of.write("DA\n")
        of.write("Traseu: ")
        for state in Course:
            of.write(state + " ")
        of.write("\n")

    else:
        of.write("NU\n")


# NoQ - no states
# Q - states
# sigma - alphabet
# NoF - no final states
# F - final states
# q0 - initial state
# NoTransitions - no of transitions
# transitions
# Nowords - no of words

Q = set()
sigma = set()
F = set()
transitions = dict()

now = 0  # current line in input file

# line 0 - No of states and transitions

lines[0] = lines[0].split()
NoQ = int(lines[0][0])
NoTransitions = int(lines[0][1])

# moving to the next line in the file
now += 1

# all states
for i in range(NoQ):
    Q.add(i)

# lines 1-NoTransitions (All transitions)

for i in range(1, NoTransitions + 1):
    transition = lines[i].split()
    key = (transition[0], transition[2])
    transitions[key] = transition[1]
    now += 1
    # in the dictionary we will have the transitions like this: transition(state1, letter) = state2


q0 = lines[now]

now += 1

finalstates = lines[now].split()
NoF = int(finalstates[0])

for i in range(NoF):
    F.add(finalstates[i + 1])

now += 1

Nowords = int(lines[now])

now += 1

for i in range(Nowords):
    word = lines[now]
    now += 1
    check(word)
