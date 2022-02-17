import tretikoffhw1
from pdflatex import PDFLaTeX

def format_row(lst):
    return ' & '.join(lst) + r' \\ ' + '\n'


def preamble(lst):
    return '|'.join(map(lambda _: 'L', lst))


def generate_table(lst, sep=r'\hline' + '\n'):
    return '\n'.join([
        r'\newcolumntype{L}{>{\centering\arraybackslash}m{3cm}}',
           r'\begin{tabular}',
           '{ |' + preamble(lst) + '| }',
           sep + sep.join(map(format_row, lst)) + sep,
           r'\end{tabular}'
    ])


def generate_picture(path):
    return '\n' + r'\includegraphics[scale=0.5]{' + path + '}\n'


def generate(lst, picturepath):
    tretikoffhw1.set_picture(picturepath)
    return '\n'.join([
        r'\documentclass{article}',
        r'\usepackage{array}',
        r'\usepackage{graphicx}',
        r'\begin{document}',
        generate_table(lst),
        generate_picture(picturepath),
        r'\end{document}'
    ])


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
    with open('artifacts/table.tex', 'w') as file:
        file.write(generate(test2, 'artifacts/tree.png'))
        file.close()

    with open('artifacts/table.pdf', 'wb') as file:
        file.write(PDFLaTeX.from_texfile('artifacts/table.tex').create_pdf(keep_pdf_file=True, keep_log_file=True)[0])
        file.close()
