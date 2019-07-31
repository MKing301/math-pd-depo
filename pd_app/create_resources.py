from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_bcrypt import Bcrypt
from database_setup import Base, Resource
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

resource1 = Resource(title="Learning Geometry",
             grade="6 - 8",
             course="Geometry",
             location="https://www.google.com/",
             description="A demo description note.")
session.add(resource1)
session.commit()

resource2 = Resource(title="Geometry 101",
             grade="6 - 8",
             course="Geometry",
             location="https://www.google.com/",
             description="A look into Geometry.")
session.add(resource2)
session.commit()

resource3 = Resource(title="Fractions",
             grade="K - 5",
             course="Elementary Math",
             location="https://www.google.com/",
             description="Some fraction problems.")
session.add(resource3)
session.commit()

resource4 = Resource(title="Fractions 101",
             grade="K - 5",
             course="Elementary Math",
             location="https://www.google.com/",
             description="The is some test text.")
session.add(resource4)
session.commit()

resource5 = Resource(title="Basic Algebra",
             grade="High School",
             course="Algera",
             location="https://www.google.com/",
             description="Some Algebra tricks.")
session.add(resource5)
session.commit()

resource6 = Resource(title="Intermediate Algebra",
             grade="High School",
             course="Algera",
             location="https://www.google.com/",
             description="The next level of Algebra tricks.")
session.add(resource6)
session.commit()

resource7 = Resource(title="Calculus",
             grade="Undergraduate",
             course="Calculus",
             location="https://www.google.com/",
             description="The place for derivatives.")
session.add(resource7)
session.commit()

resource8 = Resource(title="The Diff EQ Code",
             grade="Post-Graduate",
             course="Differential Equations",
             location="https://www.google.com/",
             description="The real math.")
session.add(resource8)
session.commit()

resource9 = Resource(title="Calculus 2",
             grade="Undergraduate",
             course="Calculus",
             location="https://www.google.com/",
             description="The place for derivatives.")
session.add(resource9)
session.commit()

print("Resources created!")