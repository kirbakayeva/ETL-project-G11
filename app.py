import numpy as np
import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
pg_user = 'postgres'
pg_password = 'mobo0056'
db_name = 'Candidates'


connection_string = f"{pg_user}:{pg_password}@localhost:5432/{db_name}"
engine = create_engine(f'postgresql://{connection_string}')

# engine = create_engine("sqlite:///Solved/titanic.sqlite")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save reference to the table

# Passenger = Base.classes.passenger
Candidates = Base.classes.Candidates
Polls = Base.classes.Polls
States = Base.classes.States
Candidate_Spending = Base.classes.Candidate_Spending

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################


def double(inp):
    if inp is not None:
        return inp*2
    else:
        return None

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/passengers"
    )

@app.route('/api/v1.0/names')
def names():
    # Query all passengers
    session = Session(engine)
    results = session.query(Passenger.name).all()

    # close the session to end communication with the server
    session.close()

    all_names = list(np.ravel(results))
    # alternative with list comprehension
    # all_names = [result[0] for result in results]

    return jsonify(all_names)


@app.route('/api/v1.0/passengers')
def passengers():

    ############### Database Block ###################
    # Start session
    session = Session(engine)

    # Query the database
    results = session.query(Passenger).all()

    # close session
    session.close()
    ###################################################

    ################### Processing ####################
    all_passengers = []
    for passenger in results:
        passenger_dict = {}
        passenger_dict['name'] = {'first':passenger.name.split(' ')[1],'last':passenger.name.split(' ')[0]}
        passenger_dict['age'] = passenger.age
        passenger_dict['doubleAge'] = double(passenger.age)
        passenger_dict['sex'] = passenger.sex
        all_passengers.append(passenger_dict)
    ####################################################

    return jsonify(all_passengers)

if __name__ == '__main__':
    app.run(debug=True)