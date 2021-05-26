
class Stack(list):

    def __init__(self):
        super().__init__(self)

    def __repr__(self):
        return "$" if self.is_empty() else "".join(self)[::-1]

    def push_left(self, item):
        for s in item[::-1]:
            if s != "$":
                self.append(s)
            else:
                return

    def pop_left(self):
        return self.pop()

    def is_empty(self):
        return len(self) == 0


"""Getting input from console."""


def get_input_data():
    data = input().split("|")
    for i in range(len(data)):
        data[i] = list(data[i].split(","))
    return data


def get_input_transitions():

    # dictionary of transitions, consists of tuples

    transitions = dict()
    while True:
        try:
            function = input()
            if function == "\n" or function == "":
                break
            else:
                pass
            function = function.split("->")
            transitions[tuple(function[0].split(","))] = tuple(function[1].split(","))
        except Exception as e:
            break
    return transitions


def log_fail():
    print("fail|0")


def log_pair(state, stack):
    print("%s#%s|" % (state, stack), end="")


# q0 - initial state
# s0 - initial symbol
# F - final states
# Q - states
# sigma - alphabet

inputData = get_input_data()
Q = input().split(",")                 # Q
sigma = input().split(",")                    # Alphabet symbols (sigma) UNION epsilon
STACK_ALPHABET = input().split(",")             # Finite stack alphabet
F = input().split(",")                           # F is a subset of Q
initialState = input()                           # PDA in this state before making any transitions
initialSymbol = input()                          # Stack consists of one instance of this symbol
transitions = get_input_transitions()           # Transition functions (delta)


for data in inputData:
    stack = Stack()
    failed = False

    # start from initial states
    q0 = initialState
    s0 = initialSymbol
    log_pair(q0, s0)

    for symbol in data:

        # epsilon
        while transitions.get((q0, "$", s0)) is not None:
            (q0, s0) = transitions.get((q0, "$", s0))
            stack.push_left(s0)
            log_pair(q0, stack)
            if not stack.is_empty():
                s0 = stack.pop_left()
            else:
                failed = True
                break

        # stack not empty, check if transition exists
        if not failed and transitions.get((q0, symbol, s0)) is not None:
            (q0, s0) = transitions.get((q0, symbol, s0))
            stack.push_left(s0)
            log_pair(q0, stack)
            if not stack.is_empty():
                s0 = stack.pop_left()
            else:
                failed = True
        else:
            failed = True

        # stack empty
        if failed:
            log_fail()
            break
       

    # epsilon
    if not failed:
        while transitions.get((q0, "$", s0)) is not None and q0 not in F:
            (q0, s0) = transitions.get((q0, "$", s0))
            stack.push_left(s0)
            log_pair(q0, stack)
            if not stack.is_empty():
                s0 = stack.pop_left()
            else:
                break
        print(1 if q0 in F else 0, end="\n")
    else:
        pass