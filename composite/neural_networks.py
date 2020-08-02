from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):

    def connect_to(self, other):
        if self == other:
            return

        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):

    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __repr__(self):
        return f'{self.__class__.__name__} "{self.name}" with ' \
            f'{len(self.inputs)} inputs and {len(self.outputs)} outputs'

    def __iter__(self):
        yield self


class NeuralLayer(list, Connectable):

    def __init__(self, name, count):
        super().__init__()
        self.name = name
        for i in range(count):
            self.append(Neuron(f'{name}-{i}'))

    def __repr__(self):
        return f'{self.__class__.__name__} "{self.name}" with {len(self)} neurons'

    def __next__(self):
        print('asdf')


if __name__ == "__main__":
    neuron1 = Neuron('n1')
    neuron2 = Neuron('n2')
    layer1 = NeuralLayer('l1', 3)
    layer2 = NeuralLayer('l2', 4)

    neuron1.connect_to(neuron2)
    neuron2.connect_to(layer1)
    layer1.connect_to(layer2)

    print(neuron1)
    print(neuron2)
    print(layer1)
    print(layer2)
