import requests


result = requests.get(url='https://saopaulo.publicbikesystem.net/ube/gbfs/v1/en/station_status')
print(result)

print(result.json()['data']['stations'][104]['num_bikes_available'])