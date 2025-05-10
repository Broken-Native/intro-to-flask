# database helper functions
from sqlalchemy import Table
from extensions import db
# CRUD

def create_record(db_table: Table, **kwargs: dict) -> None:
    """a db utility function for creating new records in database"""

    # create an instance of the db table class
    record = db_table(**kwargs)
    # add the table instance/object to the database session
    db.session.add(record)
    # commit record in database session 
    db.session.commit()

def get_record(db_table, record_id, all_record = False):
    if all_record:
        record = db_table.query.all()

    else: 
        record = db_table.query.get(record_id)
        
    return record