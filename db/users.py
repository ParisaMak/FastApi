from sqlalchemy.orm import Session
from db.schemas import UserBase
from db.models import User
from db.hash import Hash

def create_user( db: Session,request: UserBase):
    new_user = User(username=request.username,
                     email=request.email,
                     password_hash=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



def get_user_by_id(db: Session, id: int ):
    user = db.query(User).filter(User.id == id).first()
    return user

def get_user_by_username(db: Session, username: str):
    user = db.query(User).filter(User.username == username).first()
    return user

def update_user_by_id(db: Session, id: int ,request:UserBase):
    house = db.query(User).filter(User.id == id)
    house.update({
        User.username :request.username,
        User.email: request.email,
        User.password_hash :Hash.bcrypt(request.password)
    })
    db.commit()
    return 'ok'

def delete_user_by_id(db: Session, id: int ):
    user = db.query(User).filter(User.id == id).first() 
    db.delete(user)
    db.commit()
    return 'ok'