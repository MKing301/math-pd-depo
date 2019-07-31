from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_bcrypt import Bcrypt
from database_setup import Base, Course
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

course1 = Course(grade="6 - 8",
             course="Geometry")
session.add(course1)
session.commit()

course2 = Course(grade="6 - 8",
             course="Trigonometry")
session.add(course2)
session.commit()

course3 = Course(grade="K - 5",
             course="Elementary Math")
session.add(course3)
session.commit()

course4 = Course(grade="K - 5",
             course="Basic Math")
session.add(course4)
session.commit()

course5 = Course(grade="High School",
             course="Algera")
session.add(course5)
session.commit()

course6 = Course(grade="High School",
             course="Pre-Algera")
session.add(course6)
session.commit()

course7 = Course(grade="Undergraduate",
             course="Calculus")
session.add(course7)
session.commit()

course8 = Course(grade="Post-Graduate",
             course="Differential Equations")
session.add(course8)
session.commit()

course9 = Course(grade="Undergraduate",
             course="Calculus 2")
session.add(course9)
session.commit()

print("Courses created!")