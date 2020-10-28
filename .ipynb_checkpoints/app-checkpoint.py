import numpy as np
import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
<<<<<<< HEAD
from sqlalchemy import func

from flask import Flask, jsonify
import datetime as dt


=======

from flask import Flask, jsonify
>>>>>>> 78d0a33ff9ed1f66bfde9223319076dde879310c


#################################################
# Database Setup
#################################################
pg_user = 'postgres'
<<<<<<< HEAD
pg_password = 'Rouzbeh237*tx'
db_name = 'POTUS_db'
=======
pg_password = 'mobo0056'
db_name = 'Candidates'

>>>>>>> 78d0a33ff9ed1f66bfde9223319076dde879310c

connection_string = f"{pg_user}:{pg_password}@localhost:5432/{db_name}"
engine = create_engine(f'postgresql://{connection_string}')

<<<<<<< HEAD
=======
# engine = create_engine("sqlite:///Solved/titanic.sqlite")
>>>>>>> 78d0a33ff9ed1f66bfde9223319076dde879310c

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save reference to the table
<<<<<<< HEAD
=======

# Passenger = Base.classes.passenger
>>>>>>> 78d0a33ff9ed1f66bfde9223319076dde879310c
Candidates = Base.classes.Candidates
Polls = Base.classes.Polls
States = Base.classes.States
Candidate_Spending = Base.classes.Candidate_Spending

<<<<<<< HEAD

=======
>>>>>>> 78d0a33ff9ed1f66bfde9223319076dde879310c
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

<<<<<<< HEAD

=======
>>>>>>> 78d0a33ff9ed1f66bfde9223319076dde879310c
#################################################
# Flask Routes
#################################################


<<<<<<< HEAD
@app.route("/")
def welcome():
    """List all available API routes."""
    return (
        f"<br>List of all available API routes:<br>"
        f"<br>/api/v1.0/Candidate_table<br>"
        f"<br>/api/v1.0/States_table<br>"
        f"<br>/api/v1.0/Spending_table/Trump<br>"
        f"<br>/api/v1.0/Spending_table/Biden<br>"
        f"<br>/api/v1.0/Polls_table/Trump<br>"
        f"<br>/api/v1.0/Polls_table/Biden<br>"
)

@app.route("/api/v1.0/Candidate_table")
def Candidate_table():

    # Open a communication session with the database
    session = Session(engine)
    
    candidates_query =  session.query(Candidates.committee_id, Candidates.name, Candidates.committee_type).all()
    # close the session to end the communication with the database
    session.close()

    all_candidates = list(np.ravel(candidates_query))
    
    return jsonify(all_candidates)


@app.route("/api/v1.0/States_table")
def States_table():

    # Open a communication session with the database
    session = Session(engine)
    
    states_query = session.query(States.State, States.Abbreviation, States.Population).all()

    # close the session to end the communication with the database
    session.close()

    all_states = list(np.ravel(states_query))
    print(all_states)
    return jsonify(all_states)


@app.route("/api/v1.0/Spending_table/Trump")
def Spending_table_Trump():

    # Open a communication session with the database
    session = Session(engine)
    
    trump_query = session.query(Candidate_Spending.committee_id, Candidate_Spending.disbursement_date, Candidate_Spending.disbursement_amount, Candidate_Spending.recipient_name, Candidate_Spending.recipient_state, Candidate_Spending.disbursement_description, Candidate_Spending.id).filter(Candidate_Spending.committee_id == 'C00580100').all()

    # close the session to end the communication with the database
    session.close()

    trump_spending = list(np.ravel(trump_query))
    print(trump_spending)
    return jsonify(trump_spending)

@app.route("/api/v1.0/Spending_table/Biden")
def Spending_table_Biden():

    # Open a communication session with the database
    session = Session(engine)
    
    biden_query = session.query(Candidate_Spending.committee_id, Candidate_Spending.disbursement_date, Candidate_Spending.disbursement_amount, Candidate_Spending.recipient_name, Candidate_Spending.recipient_state, Candidate_Spending.disbursement_description, Candidate_Spending.id).filter(Candidate_Spending.committee_id == 'C00703975').all()

    # close the session to end the communication with the database
    session.close()

    biden_spending = list(np.ravel(biden_query))
    print(biden_spending)
    return jsonify(biden_spending)

@app.route("/api/v1.0/Polls_table/Trump")
def Polls_table_Trump():

    # Open a communication session with the database
    session = Session(engine)
    
    trump_query = session.query(Polls.state, Polls.pollster_id, Polls.fte_grade, Polls.sample_size, Polls.population, Polls.methodology, Polls.end_date, Polls.nationwide_batch, Polls.answer, Polls.candidate_party, Polls.pct, Polls.committee_id, Polls.id).filter(Polls.committee_id == 'C00580100').all()

    # close the session to end the communication with the database
    session.close()

    trump_polls = list(np.ravel(trump_query))
    return jsonify(trump_polls)

@app.route("/api/v1.0/Polls_table/Biden")
def Polls_table_Biden():

    # Open a communication session with the database
    session = Session(engine)
    
    biden_query = session.query(Polls.state, Polls.pollster_id, Polls.fte_grade, Polls.sample_size, Polls.population, Polls.methodology, Polls.end_date, Polls.nationwide_batch, Polls.answer, Polls.candidate_party, Polls.pct, Polls.committee_id, Polls.id).filter(Polls.committee_id == 'C00703975').all()

    # close the session to end the communication with the database
    session.close()

    biden_polls = list(np.ravel(biden_query))
    return jsonify(biden_polls)

if __name__ == '__main__':
    app.run(debug=True)
=======
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
>>>>>>> 78d0a33ff9ed1f66bfde9223319076dde879310c
