# Datasets

| Dataset     | Train | Val   | Size  |
| ----------- | ----- | ----- | ----- |
| citypersons | 2975  | 500   | 11.6G |
| deepdrive   | 70000 | 20000 | 542M  |
| kitti       | 5984  | 1497  | 6.2G  |
| roadsigns   | 693   | 184   | 228M  |

**Labels**

We have the following distinct labels.

- car
- person
- van
- rider
- truck
- tram
- personsitting
- bus
- train
- motorcycle
- bicycle
- trafficlight
- trafficsign
- stopsign
- speedlimitsign
- crosswalk

When converting the downloaded annatations into the format we need, you can choose wich labels you want to end up with

## unified1.json

**Changes:** person and personsitting get unified. stopsign, speedlimitsign, crosswalk and trafficsign get unified.

| ID  | Name          | Citypersons | Deepdrive | Kitti | Roadsigns |
| --- | ------------- | ----------- | --------- | ----- | --------- |
| 0   | Car           | 0           | 700703    | 23075 | 0         |
| 1   | Person        | 17975       | 92159     | 3728  | 0         |
| 2   | Van           | 0           | 0         | 2349  | 0         |
| 3   | Rider         | 1680        | 4560      | 1301  | 0         |
| 4   | Truck         | 0           | 27892     | 901   | 0         |
| 5   | Tram          | 0           | 0         | 418   | 0         |
| 6   | Bus           | 0           | 11977     | 0     | 0         |
| 7   | Train         | 0           | 128       | 0     | 0         |
| 8   | Motorcycle    | 0           | 3023      | 0     | 0         |
| 9   | Bicycle       | 0           | 7124      | 0     | 0         |
| 10  | Traffic light | 0           | 187871    | 0     | 120       |
| 11  | Traffic sign  | 0           | 238270    | 0     | 867       |


## unified2.json

| ID  | Name            |
| --- | --------------- |
| 0   | Car             |
| 1   | Pedestrian      |
| 2   | Van             |
| 3   | Rider           |
| 4   | Truck           |
| 5   | misc            |
| 6   | Tram            |
| 7   | Person sitting  |
| 8   | bus             |
| 9   | train           |
| 10  | motorcycle      |
| 11  | bicycle         |
| 12  | traffic light   |
| 13  | traffic sign    |
| 14  | stop sign       |
| 15  | speedlimit sign |
| 16  | crosswalk       |