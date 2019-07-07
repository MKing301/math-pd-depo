from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import os

Base = declarative_base()


class User(Base):
    '''A user of the catalog app program. Users will have
       the following attributes:
       Attibute(s):
       id - unique id number for each user
       first_name - user's first name
       last_name - user's last name
       username = user's username
       email - user's email address
       password - user's password
       inserted - user inserted date
    '''
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    inserted = Column(DateTime, nullable=False)


engine = create_engine(os.environ.get('LOCAL_DB_URI_MATH'))

Base.metadata.create_all(engine)
