from database import SessionLocal
from models import User
from utils.hash import Hash

db = SessionLocal()

def seed():
    user = User(username='test_user', password=Hash.get_password_hash('1234'))

    db.add(user)
    db.commit()

if __name__ == '__main__':
    print(f'Seeding data...')
    seed()
