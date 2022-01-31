from events_app.models import *
from events_app import db
from datetime import datetime

u1 = Guest(name='Alex', email='email@gmail.com', phone='555-555-5555')
e1 = Event(title='Fun Event', description='this is a fun event :)', date_and_time=datetime.now())

u1.events_attending.append(e1)
db.add