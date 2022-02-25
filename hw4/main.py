# "Взять функцию подсчета чисел Фибоначчи и сравнить время исполнения кода (вызова функции от большого числа n 10 раз через 10 потоков\процессов) при использовании threading и multiprocessing
#
# Необходимо сравнить время выполнения при синхронном запуске, использовании потоков и процессов.
#
# Артефакт - текстовый файл с результатами запуска различными методами."
def run_easy():
    pass

# "Переписать функцию integrate для того, чтобы ее выполнение можно было распараллелить. Иcпользовать `concurrent.futures`: `ThreadPoolExecutor` и `ProcessPoolExecutor`.  Добавить логирование (когда какая задача запускается), сравнить время выполнения для `integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs)` при разном числе `n_jobs` (от 1 до `cpu_num*2`)
#
# Артефакт - файл логов, файл сравнения общего времени исполнения"
def run_medium():
    pass


# "Практика работы с процессами. Использование multiprocessing.Queue и multiprocessing.Pipe. Реализовать следующую схему приложения:
# У вас есть главный процесс и 2 дочерних (A и B). Из главного процесса вы можете через stdin отправлять сообщения (строки) в процесс A, которые будут складироваться в очередь. К каждому из сообщений процесс A будет применять .lower() и отправлять в процесс B (одно сообщение раз в 5 секунд). Процесс B должен отправлять закодированную сроку через rot13 и отправлять в главный процесс откуда печатать в stdout.
#
# Артефакт - текстовый файл взаимодействия вас и программы (необходимо выводить время сообщений)"
def run_hard():
    pass


if __name__ == '__main__':
    run_easy()
    run_medium()
    run_hard()
