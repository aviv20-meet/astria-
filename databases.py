from model import Base, User, Lawyer, Laws, Rights


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# replace lecture.db with your own database file
def make_session():
	engine = create_engine('sqlite:///database.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session

def add_user(name, email, password):
	session = make_session()
	new_user = User(
		name = name, 
		email = email, 
		password = password)
	session.add(new_user)
	session.commit()

def add_lawyer(name, profession, specialty):
	session = make_session()
	new_user = User(
		name = name, 
		profession = profession, 
		specielty = specielty, 
		education = education, 
		experience = experience, 
		location =location)
	session.add(new_user)
	session.commit()

def get_all_laws():
	session = make_session()
	laws = session.query(Laws).all()
	return laws

def get_all_rights():
	session = make_session()
	rights = session.query(Rights).all()
	return rights
	
def get_all_lawyers():
	session = make_session()
	lawyers = session.query(Lawyer).all()

	return lawyers