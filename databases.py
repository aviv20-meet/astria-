from model import Base, Student


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# replace lecture.db with your own database file
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(name, email, password):
	new_user = User(name = name, email = email, password = password)
	session.add(new_user)
	session.commit()

def add_lawyer(name, profession, specialty)


