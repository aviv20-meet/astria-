from model import Base, User, Lawyer, Law, Right


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///astria.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()




# replace lecture.db with your own database file
def make_session():
	engine = create_engine('sqlite:///database.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session

def add_user(name, email, password):
	make_session()
	new_user = User(
		name = name, 
		email = email, 
		password = password)
	session.add(new_user)
	session.commit()

def add_law(title, content):
	make_session()
	new_law = Law(
		law_title=title,
		contents=content)
	session.add(new_law)
	session.commit()

def add_right(title, content):
	make_session()
	new_right = Right(
		right_title=title,
		contents=content)
	session.add(new_right)
	session.commit()

def add_lawyer(name, profession, specialty):
	make_session()
	new_lawyer = Lawyer(
		name = name, 
		specialty= specialty, 
		profession = profession,
		education = "", 
		experience = "", 
		location ="")
	session.add(new_lawyer)
	session.commit()

def get_all_laws():
	make_session()
	laws = session.query(Law).all()
	return laws

def get_all_rights():
	make_session()
	rights = session.query(Right).all()
	return rights
	
def get_all_lawyers():
	make_session()
	lawyers = session.query(Lawyer).all()

	return lawyers

add_lawyer("john doe"," " , "mediator")
add_right("hii", "hello")
get_all_rights()