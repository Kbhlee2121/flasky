import pytest
from app import create_app, db
from app.models.dog import Dog

#app
@pytest.fixture
def app():
    app = create_app({'TESTING': True})

    # withn the context of the app we just created
    with app.app_context():
        # for all these different models, create all these datatables and place them in test database
        db.create_all()
        # way for us to get multiple responses back and to pause and then continue
        yield app

    # after test has run, want to start from scratch again so it doesn't affect next test
    with app.app_context():
        db.drop_all()


#client
@pytest.fixture
# referring to app fixture
def client(app):
    # using flask method test_client to start test and refers to app fixture
    return app.test_client()

#data
@pytest.fixture
def one_dog(app):
    dog = Dog(
        name="joy",
        breed="husky",
        age="10"
    )

    db.session.add(dog)
    db.session.commit()

"""
import pytest
from app import create_app
# ************************
# app - simulate flask run
# ************************
@pytest.fixture
# name this app because it is the simulation of the app (the flask server)
def app():
    # right now its not important what you put in the dictionary
    # since we only have been checking to see if the dictionary actually exists
    # and is not empty
    # but you can set up more complicated logic in __init__.py if needed
    app = create_app({"Testing": True})
    
    # SETTING UP
    # the next steps are going to be in the context of the simulated test app
    with app.app_context():
        # create all the tables for the test db
        # this takes care of the steps we manually do
        # when we do flask db init, migrate and update in terminal
        db.create_all()
        # pause this function for now until after tests are run
        yield app # this line divides set up and clean up!
        
    # CLEANING UP (or tearing down)
    # after tests are finished running
    with app.app_context():
        # drop all the db tables and clear all data
        # so that you can have a fresh db every time
        db.drop_all()
        
# **************************    
# client - simulate requests
# **************************
@pytest.fixture
# the parameter app is referring to the app fixture right above it
# pytest knows to inject the app in when running this func
def client(app):
    # test_client is a feature of Flask
    # to setup a mock client for you
    return app.test_client()
# ****************************
# data to be populated into db
# ****************************
"""