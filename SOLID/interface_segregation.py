from abc import ABC, abstractmethod


# class MachineABC(ABC):
#     """
#     Abstract base classes should not container any method that not all of its
#     subclasses are expected to implement or use.
#     """

#     def print(self, doc):
#         raise NotImplementedError

#     def scan(self, doc):
#         raise NotImplementedError

#     def fax(self, doc):
#         raise NotImplementedError


# class MultiFunctionPrinter(MachineABC):

#     def print(self, doc):
#         print('Printing ', doc, '...')

#     def scan(self, doc):
#         print('Scanning ', doc, '...')

#     def fax(self, doc):
#         print('Faxing ', doc, '...')


# class SimplePrinter(MachineABC):
#     """
#     This class has inherited methods that it does not support (scan & fax),
#     which breaks the Interface Segregation Principle.
#     """

#     def print(self, doc):
#         print('Printing ', doc, '...')


class PrinterABC(ABC):

    @abstractmethod
    def print(self, doc):
        raise NotImplementedError


class ScannerABC(ABC):

    @abstractmethod
    def print(self, doc):
        raise NotImplementedError


class FaxMachineABC(ABC):

    @abstractmethod
    def print(self, doc):
        raise NotImplementedError


class MultiFunctionPrinter(PrinterABC, ScannerABC, FaxMachineABC):

    def print(self, doc):
        print('Printing ', doc, '...')

    def scan(self, doc):
        print('Scanning ', doc, '...')

    def fax(self, doc):
        print('Faxing ', doc, '...')


class PhotoCopier(PrinterABC, ScannerABC):

    def print(self, doc):
        print('Printing ', doc, '...')

    def scan(self, doc):
        print('Scanning ', doc, '...')


class SimplePrinter(PrinterABC):

    def print(self, doc):
        print('Printing ', doc, '...')
