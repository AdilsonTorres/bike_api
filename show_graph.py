import matplotlib.pyplot as plt
import sys
import glob
import datetime
import time
import os
# import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter, MaxNLocator

ROOT_PATH = sys.path[0]

stations = [
    101,
    105,
    232,
]


def format_fn(tick_val, tick_pos):
    return time.strftime("%d/%b \n %H:%M", time.localtime(tick_val * 10000))


def create_graph(data_time, available_bikes, available_docks, station):
    fig_size = plt.rcParams["figure.figsize"]
    print("Current size:", fig_size)
    fig_size[0] = 12
    fig_size[1] = 9

    plt.rcParams["figure.figsize"] = fig_size
    p1 = plt.bar(x=data_time, height=available_bikes)
    p2 = plt.bar(x=data_time, height=available_docks, bottom=available_bikes)
    # plt.gcf().autofmt_xdate()
    # myFmt = mdates.DateFormatter('%H:%M')
    # plt.gca().xaxis_date('America/Sao_Paulo')
    plt.gca().xaxis.set_major_formatter(FuncFormatter(format_fn))
    # plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

    plt.legend((p1[0], p2[0]), ("Available Bikes", "Available Docks"))
    plt.title("Frequency of bikes at station {}".format(station))

    graph_path = os.path.dirname(ROOT_PATH + '/graphs/')
    if not os.path.exists(graph_path):
        print("create log directory.")
        os.makedirs(graph_path)
    plt.savefig(graph_path + "/" + "station_{}.png".format(station))
    plt.close()


def mount_data_graph(station, log_files):
    data_time = []
    available_bikes = []
    available_docks = []

    k = 0
    j = len(log_files)

    for i in range(k, j):
        contents = ''
        file = log_files[i]
        with open(file) as f:
            contents = f.readlines()

        bikes = int(contents[station * 3 - 2 + 1].split(' ')[1])
        available_bikes.append(bikes)
        docks = int(contents[station * 3 - 2 + 2].split(' ')[1])
        available_docks.append(docks)

        year = int(file.split('/logs/')[1].split('-')[0][0:4])
        month = int(file.split('/logs/')[1].split('-')[0][4:6])
        day = int(file.split('/logs/')[1].split('-')[0][6:8])
        hour = int(file.split('-')[1].split('.log')[0][0:2])
        minutes = int(file.split('-')[1].split('.log')[0][2:4])

        time = datetime.datetime(year, month, day, hour, minutes)
        data_time.append(time.timestamp() / 10000)

    create_graph(data_time, available_bikes, available_docks, station)


def main(argv):
    log_path = ROOT_PATH + '/logs/*.log'
    log_files = glob.glob(log_path)
    log_files.sort()

    for station in stations:
        mount_data_graph(station, log_files)


if __name__ == "__main__":
    main(sys.argv)
