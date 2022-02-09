
def format_row(lst):
    return ' & '.join(lst) + ' \\\\\n'


def preamble(lst):
    return '|'.join(map(lambda _: 'c', lst))


def generate(lst, sep='\\hline\n'):
    return '\\begin{tabular}{ |' + preamble(lst) + '| }\n' + \
           sep + sep.join(map(format_row, lst)) + sep + \
           '\\end{tabular}\n'


test1 = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]
test2 = [
    ['123', '12', '1'],
    ['1', '12', '123'],
    ['With the lights out', 'it\'s less dangerous', 'Here we are now, entertain us']
]

if __name__ == '__main__':
    with open("../artifacts/table.tex", "w") as file:
        file.write(generate(test2))
        file.close()
