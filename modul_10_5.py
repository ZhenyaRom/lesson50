from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='UTF-8') as file:
        while True:
            s = file.readline()
            if not s:
                break
            all_data.append(s)


# time_start = datetime.now()
# filenames = [f'./file {number}.txt' for number in range(1, 5)]
# for f in filenames:
#     read_info(f)
# time_finish = datetime.now()
# time_rez = time_finish - time_start
# print(time_rez)


if __name__ == '__main__':
    time_start = datetime.now()
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    time_finish = datetime.now()
    time_rez = time_finish - time_start
    print(time_rez)
