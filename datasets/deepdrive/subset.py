import argparse

weather = ["clear", "overcast", "snowy", "rainy", "foggy", "partly_cloudy", "undefined"]
scene = ["residential", "highway", "city street", "parking lot", "gas stations", "tunnel"]
tod = ["dawn/dusk", "daytime", "night"]


def filter_dataset(weather, scene, time_of_day):
    # convert underscore to space for ; e.g. partly_cloudy -> partly cloudy


def main():
    parser = argparse.ArgumentParser(description="Create Subset of Deepdrive based on (multiple) tags")
    parser.add_argument('-w', '--weather', nargs='+', help="Weather conditions to filter by (e.g.: clear foggy party_cloudy)")
    parser.add_argument('-s', '--scene', nargs='+', help="Scenes to filter by (e.g.: residential highway)")
    parser.add_argument('-t', '--time_of_day', nargs='+', help="Time of day to filter by (e.g.: daytime)")

    args = parser.parse_args()

    filter = filter_dataset(args.weather, args.scene, args.time_of_day)

if __name__ == "__main__":
    main()