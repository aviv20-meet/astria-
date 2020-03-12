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
	__tablename__='lawyers'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	email = Column(String)
	password = Column(String)




Base = declarative_base()