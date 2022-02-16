from hw1.src.tretikoffhw1.tretikoffhw1 import set_picture
def format_row(lst):
    return ' & '.join(lst) + ' \\\\\n'


def preamble(lst):
    return '|'.join(map(lambda _: 'L', lst))


def generate(lst, sep='\\hline\n'):
    return '\\newcolumntype{L}{>{\\centering\\arraybackslash}m{3cm}}\n' \
           '\\begin{tabular}\n' \
           '{ |' + preamble(lst) + '| }\n' + \
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
    ['With the lights out', 'it\'s less dangerous', 'I wanna heal, I wanna feel what I thought was never real\
    I wanna let go of the pain Ive felt so long\
    (Erase all the pain til its gone)\
    I wanna heal, I wanna feel like Im close to something real\
    I wanna find something Ive wanted all along\
    Somewhere I belong']
]

if __name__ == '__main__':
    with open("artifacts/table.tex", "w") as file:
        file.write(generate(test2))
        file.close()
