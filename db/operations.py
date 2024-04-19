from datetime import datetime
from sqlalchemy.exc import OperationalError
from data.example_data import PEOPLE_NOTES
from apps.config import db
from api.models import Note, Person

def get_data_from_table(model):
    try:
        data = db.session.query(model).all()
        db.session.close()
        return data
    except OperationalError:
        return []

def create_database(db):
    db.create_all()
    for data in PEOPLE_NOTES:
        new_person = Person(lname=data.get("lname"), fname=data.get("fname"))
        for content, timestamp in data.get("notes", []):
            new_person.notes.append(
                Note(
                    content=content,
                    timestamp=datetime.strptime(
                        timestamp, "%Y-%m-%d %H:%M:%S"
                    ),
                )
            )
        db.session.add(new_person)
    db.session.commit()
    print("Created new database")

def update_database(db, existing_people, existing_notes):
    db.drop_all()
    db.create_all()
    for person in existing_people:
        db.session.merge(person)
    for note in existing_notes:
        db.session.merge(note)
    db.session.commit()
    print("Updated existing database")
