# Google Nest temperature threshold checker

This script checks Google Nest sensor data for whether temperature has exceeded a certain threshold. This is useful for housing in the Netherlands (and possibly also other places), which legally should not exceed 26.5 degrees Celcius for over 300 hours in a year.

This has been tested with data from the Google Nest Protect smoke detector, but might also work with data from the thermostat or other sources.

## Usage

1. Clone this repo
2. Go to Google Takeout (https://takeout.google.com/) and request all your Nest data. You will get a link to download a zip of your data within a few days.
3. Get the `.csv` files containing sensor data from your downloaded zip and put them in this repo's `data` directory. They should be called something like `{year}-{month}-sensors.csv`. For best results, put exactly one year's worth of files there.
4. Run `python aggregate.py`
5. A summary will be printed to stdout, and all measurements exceeding the default threshold of `26.5` degrees will be written to `result.csv`.

Optionally you could modify the `get_temperature_exceeding_threshold` function call to pass in any other threshold.