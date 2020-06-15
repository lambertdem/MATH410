In the current folder you will find .rmd files that were used to obtain the extreme value analysis results for datasets of temperature
in July, and rain precipitations for cities in Canada (Québec, Montreal, Toronto and Vancouver).

The current folder also contains the following subfolders:
	Data_Processing:
		-Python (.py) Files used to merge the .csv files obtained from the 
		 Environment Canada website.
	Datasets:
		-The resulting merged .csv files for each city.

To reproduce the exact merging of the files, one needs to take the following steps:

1) Copy-Paste the following URL in a web browser (it should automatically download the yearly data for a given location.

	https://climate.weather.gc.ca/climate\_data/bulk\_data\_e.html?format=csv&stationID={StationID}&Year={Year}&Month=1&Day=1&timeframe={TimeFrame}&submit=Download+data

	where {StationID}, {Year} and {TimeFrame} should be replaced with the desired values.

	QUÉBEC
	{StationID} = 26892 for {Year} in [1992,2020], 5251 for {Year} in [1943,2017], 51457 for {Year} in [2013,2020]

	MONTREAL
	{StationID} =  5415 for {Year} in [1941,2013], 51157 for {Year} in [2013,2020]

	TORONTO
	{StationID} = 51459 for {Year} in [2013,2020], 5097 for {Year} in [1937,2013]

	VANCOUVER
	{StationID} =   889 for {Year} in [1937,2013], 51442 for {Year} in [2013,2020]

	{TimeFrame} = 2 is the prefered time frame as it leads to a download od daily data


2) Once the .csv files have been downloaded, add the .py scripts to the same folder and run them to obtain a single
	   unified .csv

3) Run the desired R scripts, making sure that the path to the merged .csv files is accurate.

