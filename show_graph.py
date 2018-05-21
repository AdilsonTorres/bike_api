import matplotlib.pyplot as plt
import sys
import glob
import datetime
import time
import os
# import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter, MaxNLocator

ROOT_PATH = sys.path[0]

# TODO: Receive as parameter or create all stations graphs.
station = 101 - 1
stations = [
    101,
    105,
]


def format_fn(tick_val, tick_pos):
    return time.strftime("%d/%b \n %H:%M", time.localtime(tick_val * 10000))


def create_graph(data_time, available_bikes, available_docks, station):
    # available =
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


def mount_data_graph(station, log_files):
    data_time = []
    available_bikes = []
    available_docks = []

    for file in log_files:
        contents = ''
        with open(file) as f:
            contents = f.readlines()

        available_bikes.append(int(contents[2 + station * 3 - 2 + 1].split(' ')[1]))
        available_docks.append(int(contents[2 + station * 3 - 2 + 2].split(' ')[1]))

        year = int(file.split('/logs/')[1].split('-')[0][0:4])
        month = int(file.split('/logs/')[1].split('-')[0][4:6])
        day = int(file.split('/logs/')[1].split('-')[0][6:8])
        hour = int(file.split('-')[1].split('.log')[0][0:2])
        minutes = int(file.split('-')[1].split('.log')[0][2:4])

        time = datetime.datetime(year, month, day, hour, minutes)
        data_time.append(time.timestamp() / 10000)
        # i += 1

    create_history(data_time, available_bikes, available_docks)


def main(argv):
    log_path = ROOT_PATH + '/logs/*.log'
    log_files = glob.glob(log_path)
    log_files.sort()

    if len(stations) > 1:




if __name__ == "__main__":
    main(sys.argv)
