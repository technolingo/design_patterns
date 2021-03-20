# Single Responsibility Principle / Separation of Concerns

import os


class Journal:

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, idx):
        del self.entries[idx]

    # def save(self, filepath):
    #     pass

    # def load(self, filepath):
    #     pass

    # def download(self, url):
    #     pass

    def __str__(self):
        return '\n'.join(self.entries)


class JournalPersistenceManager:

    @staticmethod
    def save(journal, filepath):
        with open(filepath, 'w') as f:
            f.write(str(journal))

    @staticmethod
    def load(journal, filepath):
        pass

    @staticmethod
    def download(journal, url):
        pass


j = Journal()
j.add_entry('Mars is the destiny.')
j.add_entry('Time is an unrelenting bitch.')
print(f'Journal Entries:\n{j}')

filepath = os.path.join(os.path.dirname(__file__), 'journal.txt')
JournalPersistenceManager.save(j, filepath)
