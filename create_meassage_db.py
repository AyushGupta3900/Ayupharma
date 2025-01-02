from ayupharma import app, db
from ayupharma.models import Message

with app.app_context():
    db.create_all()
    # db.drop_all()