from models import Dog
from sqlalchemy import create_engine

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    dogs=session.query(Dog).all()
    return dogs

def find_by_name(session, name):
    query=session.query(Dog).filter(Dog.name.like(f"%{name}%"))
    return query.first()
                                      
def find_by_id(session, id):
    query=session.query(Dog).filter(Dog.id.like(f"%{id}%"))
    return query.first()

def find_by_name_and_breed(session, name, breed):
    query=session.query(Dog).filter(
        Dog.name.like(f"%{name}%")
    ).filter(
        Dog.breed.like(f"%{breed}%"))
    return query.first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()