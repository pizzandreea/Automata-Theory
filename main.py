
# project 1 DFA

with open("input.txt", "r") as f:
    lines = f.read().split("\n")

of = open("output.txt", 'w')

def check(word):
    index = 0
    # if word[0] != q0:
    #     print("NU", end="\n")
    #     return
        # print("mno")

    currentState = q0
    Course = list()
    Course.append(currentState)

    while index < len(word):
        if(currentState, word[index]) not in transitions:
            of.write("NU\n")
            return
        else:
            currentState = transitions[currentState, word[index]]
            index += 1
            Course.append(currentState)

    if currentState in F:
        of.write("DA\n")
        of.write("Traseu: ")
        # of.writelines(Course)
        for state in Course:
            of.write(state+" ")
        of.write("\n")

    else:
        of.write("NU\n")



# NoQ - no states
# Q - states
# sigma - alphabet
# NoF - no final states
# F - final states
# q0 - initial state
# NoTransitions
# transitions
# Nowords

Q = set()
sigma = set()
F = set()
transitions = dict()

now = 0 #current line in input file

# line 0 -
lines[0] = lines[0].split()
NoQ = int(lines[0][0])

NoTransitions = int(lines[0][1])

now+=1

# all states
for i in range(NoQ):
    Q.add(i)

# lines 1-NoTransitions (All transitions)

for i in range(1, NoTransitions+1):
    transition = lines[i].split()
    key = (transition[0], transition[2])
    transitions[key] = transition[1]
    # in dictionar vom avea tranzitiile de forma transition(state1, letter) = state2
    now += 1

q0 = lines[now]

now += 1

finalstates = lines[now].split()
NoF = int(finalstates[0])

for i in range(NoF):
    F.add(finalstates[i+1])

now += 1

Nowords = int(lines[now])

now += 1

for i in range(Nowords):
    word = lines[now]
    now += 1
    # print(word[0],q0)
    check(word)


