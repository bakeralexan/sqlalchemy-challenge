# sqlalchemy-challenge
## Background
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area.

## Step 1 - Climate Analysis and Exploration

* Use SQLAlchemy `create_engine` to connect to your sqlite database.
<img scr="/Images/1_create_engine.png">
<img scr="/Images/2_inspector.png">

* Use SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.
<img scr="/Images/3_automap_base.png">

* Link Python to the database by creating an SQLAlchemy session.

### Precipitation Analysis
* Start by finding the most recent date in the data set.
<img scr="/Images/4_most_recent.png">
* Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data.
<img scr="/Images/5_twelve_months.png">
* Select only the `date` and `prcp` values.

* Load the query results into a Pandas DataFrame and set the index to the date column.
<img scr="/Images/6_precipitation_chart.png">
<img scr="/Images/7_prcp_fig.png">
* Sort the DataFrame values by `date`.

* Plot the results using the DataFrame `plot` method.
<img scr="/Images/Precipitation.png">
* Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Design a query to calculate the total number of stations in the dataset.
<img scr="/Images/8_exploratory_station_analysis.png">

* Design a query to find the most active stations (i.e. which stations have the most rows?).

  * List the stations and observation counts in descending order.

  * Which station id has the highest number of observations?

  * Using the most active station id, calculate the lowest, highest, and average temperature.
<img scr="/Images/9_most_active.png">
  

* Design a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filter by the station with the highest number of observations.

  * Query the last 12 months of temperature observation data for this station.

  * Plot the results as a histogram with `bins=12`.
<img scr="/Images/10_temp_hist.png">

* Close out your session.


- - -

## Step 2 - Climate App

Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

* Use Flask to create your routes.
### Routes

* `/`

  * Home page.

  * List all routes that are available.
<img scr="/Images/11_flask_app_part_1.png">
<img scr="/Images/14_app_homepage.png">

* `/api/v1.0/precipitation`

  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.
<img scr="/Images/15_app_precipitation.png">

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.
<img scr="/Images/12_flask_app_part_2.png">
<img scr="/Images/16_app_stations.png">

* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the most active station for the last year of data.

  * Return a JSON list of temperature observations (TOBS) for the previous year.
<img scr="/Images/17_app_tob.png">

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
<img scr="/Images/13_flask_app_part_3.png">
  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
<img scr="/Images/18_app_start.png">

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

<img scr="/Images/19_app_start_end.png">