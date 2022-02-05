# sqlalchemy-challenge
## Background
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area.

## Step 1 - Climate Analysis and Exploration

* Use SQLAlchemy `create_engine` to connect to your sqlite database.
<img src="/Images/1_create_engine.png" alt="Create Engine"/>
<img src="/Images/2_inspector.png" alt="Inspector"/>

* Use SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.
<img src="/Images/3_automap_base.png" alt="Automap Base"/>

* Link Python to the database by creating an SQLAlchemy session.

### Precipitation Analysis
* Start by finding the most recent date in the data set.
<img src="/Images/4_most_recent.png" alt="Most Recent"/>
* Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data.
* Select only the `date` and `prcp` values.
* Load the query results into a Pandas DataFrame and set the index to the date column.
* Sort the DataFrame values by `date`.
* Plot the results using the DataFrame `plot` method.
* Use Pandas to print the summary statistics for the precipitation data.
<img src="/Images/5_twelve_months.png" alt="12 Months"/>
<img src="/Images/6_precipitation_chart.png" alt="Precipitation"/>
<img src="/Images/7_prcp_fig.png" alt="Precipitation Chart"/>
<img src="/Images/Precipitation.png" alt="Precipitation Plot"/>


### Station Analysis

* Design a query to calculate the total number of stations in the dataset.
<img src="/Images/8_exploratory_station_analysis.png" alt="Station Analysis"/>

* Design a query to find the most active stations (i.e. which stations have the most rows?).

  * List the stations and observation counts in descending order.

  * Which station id has the highest number of observations?

  * Using the most active station id, calculate the lowest, highest, and average temperature.
<img src="/Images/9_most_active.png" alt="Most Active"/>
  

* Design a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filter by the station with the highest number of observations.

  * Query the last 12 months of temperature observation data for this station.

  * Plot the results as a histogram with `bins=12`.
<img src="/Images/10_temp_hist.png" alt="Temperature Histogram"/>

* Close out your session.


- - -

## Step 2 - Climate App

Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

* Use Flask to create your routes.
### Routes

* `/`

  * Home page.

  * List all routes that are available.
<img src="/Images/11_flask_app_part_1.png" alt="Flask App Part 1"/>
<img src="/Images/14_app_homepage.png"/>

* `/api/v1.0/precipitation`

  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.
<img src="/Images/15_app_precipitation.png"/>

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.
<img src="/Images/12_flask_app_part_2.png" alt="Flask App Part 2"/>
<img src="/Images/16_app_stations.png" alt="Flask App Stations"/>

* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the most active station for the last year of data.

  * Return a JSON list of temperature observations (TOBS) for the previous year.
<img src="/Images/17_app_tob.png" alt="Flask App Temperature Observations"/>

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
<img src="/Images/13_flask_app_part_3.png" alt="Flask App Part 3"/>
  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
<img src="/Images/18_app_start.png" alt="Flask App Start Route"/>

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

<img src="/Images/19_app_start_end.png" alt="Flask App Start and End Route"/>