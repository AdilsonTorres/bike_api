## BIKE API

Project based on https://citybik.es/ to collect data about bikes available in Sao Paulo.


### Scripts
- stations_status: Collect data of all stations in Sao Paulo and store in log folder.
- show_graph: Show historical usage of bikes in a given station.

### Tasks in progress
- Run script stations_status every time (every half-hour perhaps)
- Run show_graph to generate personalized graphs (all time, in a day, week, month, etc.)
- Use AWS as host of this scripts (Lambda and DynamoDB).