from app import create_app, db
from app.models import User  # pastikan import User model

app = create_app()

with app.app_context():
    db.drop_all()
    
    db.create_all()
    
    print("Database telah diinisialisasi!")