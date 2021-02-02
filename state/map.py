"""
A simpler example of a finite state machine.
"""

from enum import Enum, auto


class State(Enum):
    ON_HOOK = auto()
    OFF_HOOK = auto()
    CONNECTING = auto()
    CONNECTED = auto()
    ON_HOLD = auto()


class Trigger(Enum):
    CALL_DIALED = auto()
    CALL_CONNECTED = auto()
    PLACED_ON_HOLD = auto()
    TAKEN_OFF_HOLD = auto()
    LEFT_MESSAGE = auto()
    HUNG_UP = auto()


if __name__ == '__main__':
    rules = {
        State.OFF_HOOK: (
            (Trigger.CALL_DIALED, State.CONNECTING),
        ),
        State.CONNECTING: (
            (Trigger.CALL_CONNECTED, State.CONNECTED),
            (Trigger.HUNG_UP, State.ON_HOOK),
        ),
        State.CONNECTED: (
            (Trigger.PLACED_ON_HOLD, State.ON_HOLD),
            (Trigger.LEFT_MESSAGE, State.ON_HOOK),
            (Trigger.HUNG_UP, State.ON_HOOK),
        ),
        State.ON_HOLD: (
            (Trigger.TAKEN_OFF_HOLD, State.CONNECTED),
            (Trigger.HUNG_UP, State.ON_HOOK),
        ),
    }

    state = State.OFF_HOOK
    exit_state = State.ON_HOOK
    while state != exit_state:
        print(f'The phone is currently {state}.')

        for i in range(len(rules[state])):
            t = rules[state][i][0]
            print(f'{i}: {t}.')

        idx = int(input('Select an option: '))
        s = rules[state][idx][1]
        state = s
