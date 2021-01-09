class FormattedText:

    def __init__(self, text):
        self.text = text
        self.formatting = []

    class TextRange:

        def __init__(self, start, end, capitalize=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self, position):
            return self.start <= position <= self.end

    def get_range(self, start, end):
        rng = self.TextRange(start, end)
        self.formatting.append(rng)
        return rng

    def __str__(self):
        output = []
        for i, c in enumerate(self.text):
            for r in self.formatting:
                if r.covers(i) and r.capitalize:
                    c = c.upper()
            output.append(c)
        return ''.join(output)


if __name__ == "__main__":
    text = 'These violent delights have violent ends.'
    ft = FormattedText(text)
    ft.get_range(28, 34).capitalize = True
    print(ft)
