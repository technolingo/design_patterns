from enum import Enum, auto


class State(Enum):
    LOCKED = auto()
    UNLOCKED = auto()
    FAILED = auto()


if __name__ == '__main__':
    code = '1234'
    state = State.LOCKED
    entry = ''

    while True:
        if state == State.LOCKED:
            entry += input()
            if entry == code:
                state = State.UNLOCKED
            elif not code.startswith(entry):
                state = State.FAILED
        elif state == State.FAILED:
            print('Failed to unlock')
            entry = ''
            state = State.LOCKED
        elif state == State.UNLOCKED:
            print('Successfully unlocked')
            break
