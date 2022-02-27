# "Взять функцию подсчета чисел Фибоначчи и сравнить время исполнения кода (вызова функции от большого числа n 10 раз через 10 потоков\процессов)
# при использовании threading и multiprocessing
#
# Необходимо сравнить время выполнения при синхронном запуске, использовании потоков и процессов.
#
# Артефакт - текстовый файл с результатами запуска различными методами."
import math
import codecs
import multiprocessing
import sys
from threading import Thread
from multiprocessing import Process, Queue, Pipe
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from time import time, sleep
from datetime import datetime
from itertools import repeat


def fib(n):
    if n == 0: return 0
    a = 1
    b = 1
    while n > 2:
        a, b = b, a + b
        n -= 1
    return b


def fib_seq(n, n_repeat):
    for i in range(n_repeat):
        fib(n)


def fib_parallel(t_type):
    def run_fib_parallel(n):
        t = t_type(target=fib, args=(n,))
        t.start()
        return t

    def inner(n, n_repeat):
        parallel = map(run_fib_parallel, repeat(n, n_repeat))
        for p in parallel:
            p.join()

    return inner


def benchmark_fib(f, n, n_repeat):
    start = time()
    f(n=n, n_repeat=n_repeat)
    end = time()
    return end - start


def run_easy():
    with open("artifacts/easy/time.txt", "w") as file:
        n = 300_000
        n_repeat = 10
        file.write("sequential: " + str(benchmark_fib(fib_seq, n=n, n_repeat=n_repeat)) + '\n')
        file.write("threads:    " + str(benchmark_fib(fib_parallel(Thread), n=n, n_repeat=n_repeat)) + '\n')
        file.write("processes:  " + str(benchmark_fib(fib_parallel(Process), n=n, n_repeat=n_repeat)) + '\n')
        file.close()


def run_iteration(args):
    (i, f, a, step, logger) = args
    logger.log("Iteration %d started working on thread %s\n" % (i, Thread().name))
    return f(a + i * step) * step


def integrate(f, a, b, *, n_jobs=1, n_iter=1000, executor, logger):
    with executor(max_workers=n_jobs) as executor:
        step = (b - a) / n_iter
        args_range = map(lambda i: (i, f, a, step, logger), range(n_iter))
        values = executor.map(run_iteration, args_range)
        return sum(values)


class Logger:
    def __init__(self, filename):
        self.messageQueue = multiprocessing.Manager().Queue()
        self.filename = filename

    def log(self, message):
        self.messageQueue.put(message)

    def dump(self):
        with open(self.filename, "w") as file:
            while not self.messageQueue.empty():
                file.write(self.messageQueue.get())
            file.close()

# "Переписать функцию integrate для того, чтобы ее выполнение можно было распараллелить.
# Иcпользовать `concurrent.futures`: `ThreadPoolExecutor` и `ProcessPoolExecutor`.
# Добавить логирование (когда какая задача запускается),
# сравнить время выполнения для `integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs)`
# при разном числе `n_jobs` (от 1 до `cpu_num*2`)
#
# Артефакт - файл логов, файл сравнения общего времени исполнения"

def run_medium():
    with open("artifacts/medium/statistics.txt", "w") as file:
        logger = Logger("artifacts/medium/logs.txt")
        def benchmark_integrate(executor, n_jobs):
            start = time()
            integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor=executor, logger=logger)
            end = time()
            file.write("%s executor with %d jobs: %s\n" % (executor.__name__, n_jobs, str(end - start)))

        for n_jobs in range(1, 8):
            benchmark_integrate(ThreadPoolExecutor, n_jobs)
            benchmark_integrate(ProcessPoolExecutor, n_jobs)
            logger.dump()


def process_a(a_recv, b_send):
    queue = Queue()
    while True:
        while a_recv.poll():
            queue.put(a_recv.recv())

        if not queue.empty():
            line = queue.get()
            b_send.send(line.lower())
        b_send.send(a_recv.recv())
        sleep(5)


def process_b(b_recv, main_send):
    while True:
        line = b_recv.recv()
        if line is not None:
            main_send.send(codecs.encode(line, 'rot_13'))


# "Практика работы с процессами.
# Использование multiprocessing.Queue и multiprocessing.Pipe.
# Реализовать следующую схему приложения:
# У вас есть главный процесс и 2 дочерних (A и B).
# Из главного процесса вы можете через stdin отправлять сообщения (строки) в процесс A,
# которые будут складироваться в очередь.
# К каждому из сообщений процесс A будет применять .lower() и отправлять в процесс B (одно сообщение раз в 5 секунд).
# Процесс B должен отправлять закодированную сроку через rot13 и отправлять в главный процесс откуда печатать в stdout.
#
# Артефакт - текстовый файл взаимодействия вас и программы (необходимо выводить время сообщений)"
def run_hard():
    file = open("artifacts/hard/logs.txt", "w")
    (a_recv, a_send) = Pipe()
    (b_recv, b_send) = Pipe()
    (main_recv, main_send) = Pipe()
    a = Process(target=process_a, args=(a_recv, b_send))
    b = Process(target=process_b, args=(b_recv, main_send))
    a.start()
    b.start()
    while True:
        text = sys.stdin.readline()
        if not text:
            break
        file.write(datetime.now().strftime("%H:%M:%S") + " received user input: " + text)
        a_send.send(text)
        text = main_recv.recv()
        file.write(datetime.now().strftime("%H:%M:%S") + " from process b: " + text)
    file.close()


if __name__ == '__main__':
    # run_easy()
    # run_medium()
    run_hard()
