from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

'''

id
name
specielty
lawyer/mediator
location
experience
education
'''

Base = declarative_base()

class Lawyer(Base):
	__tablename__='lawyers'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	profession = Column(String)#lawyer or mediator
	specielty = Column(String)
	education = Column(String)
	experience = Column(String)
	location = Column(String)


class User(Base):
	__tablename__='user'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	email = Column(String)
	password = Column(String)

class Laws(Base):
	__tablename__ ='laws'
	id = Column(Integer, primary_key=True)
	law_title = Column(String)
	contents = Column(String)

class Rights(Base):
	__tablename__ = 'rights'
	id = Column(Integer, primary_key=True)
	right_title = Column(String)
	contents = Column(String)



