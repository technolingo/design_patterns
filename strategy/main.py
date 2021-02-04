"""
The strategy pattern achieves a separation of common and specific functionalities of a feature
implementation via composition. c.f. The template method achieves this through inheritance.
"""


from abc import ABC, abstractmethod
from enum import Enum, auto


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


class ListStrategy(ABC):
    """
    An abstract interface that clarifies how to interact with concrete strategies
    """

    def start(self, buffer): pass

    def end(self, buffer): pass

    @abstractmethod
    def add_list_item(self, buffer, item): pass


class MarkdownListStrategy(ListStrategy):

    def add_list_item(self, buffer, item):
        buffer.append(f' * {item}\n')


class HTMLListStrategy(ListStrategy):

    def start(self, buffer):
        buffer.append('<ul>\n')

    def end(self, buffer):
        buffer.append('</ul>\n')

    def add_list_item(self, buffer, item):
        buffer.append(f'  <li>{item}</li>\n')


class TextProcessor:
    """
    A text processor that produces different output based on the underlying strategy used.
    """

    def __init__(self, list_strategy=HTMLListStrategy()):
        self.list_strategy = list_strategy
        self.buffer = []

    def append_list(self, items):
        self.list_strategy.start(self.buffer)
        for item in items:
            self.list_strategy.add_list_item(
                self.buffer, item
            )
        self.list_strategy.end(self.buffer)

    def set_output_format(self, format):
        if format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HTMLListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return ''.join(self.buffer)


if __name__ == '__main__':
    items = ['foo', 'bar', 'baz']

    processor = TextProcessor()
    processor.set_output_format(OutputFormat.MARKDOWN)
    processor.append_list(items)
    print(processor)

    processor.set_output_format(OutputFormat.HTML)
    processor.clear()
    processor.append_list(items)
    print(processor)
