# set up dependencies
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# set up database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Set up Flask
app = Flask(__name__)

# Set up Flask Routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
        f"<br/>"
        f"Replace start and end dates in the url with specific dates. Please input date in this format YYYY-MM-DD <br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipitation"""
    # Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    # Convert list of tuples into normal list
    all_precipitation = list(np.ravel(results))

    # Return the JSON representation of your dictionary.
    return jsonify(all_precipitation)


@app.route("/api/v1.0/stations")
def all_stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations"""
    # Query all stations
    results = session.query(Station.id, Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()

    session.close()
    stations_list = list(np.ravel(results))

    # Return the JSON representation of your dictionary.
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def temperature():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of temperature observations (TOBS) for the previous year."""
    # Query the dates and temperature observations of the most active station for the last year of data.
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281', Measurement.date <='2017-08-23', Measurement.date >='2016-08-23').all()


    session.close()
    most_active = list(np.ravel(results))
    # Return the JSON representation of your dictionary.
    return jsonify(most_active)

@app.route("/api/v1.0/<start>")
def start_date(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # start = '2015-08-23'
    """Return a JSON list of temperature observations (TOBS) for the previous year."""
    # Query the dates and temperature observations of the most active station for the last year of data.
    results = session.query(Measurement.station, func.count(Measurement.station)).filter(Measurement.date >=start).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    session.close()
    date_start = list(np.ravel(results))
    return jsonify(date_start)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # start = '2016-08-23'
    # end = '2017-08-23'
    """Return a JSON list of temperature observations (TOBS) for the previous year."""
    # Query the dates and temperature observations of the most active station for the last year of data.    
    results = session.query(Measurement.station, func.count(Measurement.station)).filter(Measurement.date <= end, Measurement.date >=start).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()


    session.close()

    date_start_end = list(np.ravel(results))

    # Return the JSON representation of your dictionary.
    return jsonify(date_start_end)

if __name__ == '__main__':
    app.run(debug=True)
