import requests
import sys
import os
import time

BASE_URL = 'https://saopaulo.publicbikesystem.net/ube/gbfs/v1/en/'
ROOT_PATH = sys.path[0]


def main(argv):
    status_result = requests.get(url=BASE_URL + 'station_status')

    log_path = os.path.dirname(ROOT_PATH + '/logs/')

    if not os.path.exists(log_path):
        print("create log directory.")
        os.makedirs(log_path)

    num_stations = len(status_result.json()['data']['stations'])

    logfile = open(log_path + "/" + time.strftime("%Y%m%d-%H%M%S") + ".log", 'w')
    logfile.write("Number total fo stations: {}\n".format(num_stations))

    if status_result.status_code == requests.codes.ok:
        for station in range(num_stations):
            logfile.write("Station: {}\n".format(station))
            logfile.write("num_bikes_available: {}\n".format(status_result.json()['data']['stations'][station]['num_bikes_available']))
            logfile.write("num_docks_available: {}\n".format(status_result.json()['data']['stations'][station]['num_docks_available']))

    # close log file
    logfile.close()


if __name__ == "__main__":
    main(sys.argv)
