from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from db.schemas import UserBase, UserDisplay
from db.database import get_db
from db.users import create_user, get_user_by_id, update_user_by_id, delete_user_by_id

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.post('/', response_model=UserDisplay)
def user_signup(request: UserBase, db: Session = Depends(get_db)):
  return create_user(db, request)


@router.get('/{id}', response_model=UserDisplay)
def read_house(id:int, db: Session = Depends(get_db)):
  return get_user_by_id(db,id)


@router.post('/{id}/update')
def update_house(id: int, request:UserBase, db: Session = Depends(get_db)):
  return update_user_by_id(db,id,request)


@router.get('/delete/{id}')
def delete_user(id: int, db: Session = Depends(get_db)):
  return delete_user_by_id(db,id)


