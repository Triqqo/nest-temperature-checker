import csv
import os
from pathlib import Path, PosixPath


def list_data_files() -> list[PosixPath]:
    data_dir = f"{os.path.dirname(__file__)}/data"
    data_files = list(Path(data_dir).glob("*.csv"))

    return data_files


def get_temperature_data(data: list[PosixPath]) -> list[dict]:
    temperature_data: list[dict] = []

    for file in data:
        with open(str(file)) as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row[1].strip() == 'Temperaturebucket': temperature_data.append({
                    'Time': row[0].strip(),
                    'EventDescription': row[1].strip(),
                    'MaxValue': float(row[2].strip())
                })

    return temperature_data


def get_temperature_exceeding_threshold(temperature_data: list[dict], threshold: float = 26.5) -> list[dict]:
    temperature_exceeded: list[dict] = []

    temp_entry: dict
    for temp_entry in temperature_data:
        temperature = temp_entry.get('MaxValue')
        if temp_entry.get('MaxValue') > threshold:
            print(f"Temperature exceeded threshold on {temp_entry.get('Time')}, measured: {temperature}")
            temperature_exceeded.append(temp_entry)

    return temperature_exceeded


def write_result_csv(data: list[dict], filename: str):
    with open(filename, 'w') as csvfile:
        result_writer = csv.writer(csvfile)

        for entry in data:
            result_writer.writerow(entry.values())


def main():
    data_files = list_data_files()

    temperature_data = get_temperature_data(data_files)
    
    temperature_exceeded = get_temperature_exceeding_threshold(temperature_data=temperature_data, threshold=26.5)

    fifteen_minute_blocks_exceeded = len(temperature_exceeded)
    hours_exceeded = fifteen_minute_blocks_exceeded / 4

    print(f"\nTemperature exceeded threshold in 15 minute measurements: {fifteen_minute_blocks_exceeded} times")
    print(f"Temperature exceeded threshold in hours (amount of measurements divided by 4): {hours_exceeded} hours")

    write_result_csv(data=temperature_exceeded, filename='result.csv')


if __name__ == '__main__':
    main()