from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_bcrypt import Bcrypt
from database_setup import Base, User
import os
import datetime
import pytz 

engine = create_engine(os.environ.get('LOCAL_DB_URI_MATH'))
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Set up encrpytion
bcrypt = Bcrypt()

# Create test user
Test_User = User(first_name="first name",
                 last_name="last name",
                 username="username",
                 email="email",
                 password=bcrypt.generate_password_hash("password").decode('utf-8'),
                 user_role="user role",
                 inserted = datetime.datetime.now(pytz.timezone('US/Eastern')))
session.add(Test_User)
session.commit()

print("Test user created!")
