from fastapi import HTTPException, Depends, APIRouter, status
from sqlalchemy.orm import Session
from db.schemas import HouseBase, HouseDisplay
from db.database import get_db
from db.houses import create_houses, get_houses, get_house_by_id, update_house_by_id, delete_house_by_id, get_saved_houses_by_user
from typing import Optional, List
from fastapi import APIRouter, Depends, Query
from db.models import House, User
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/houses',
    tags=['houses']
)

@router.post('/',response_model=HouseDisplay)
def create_house(request: HouseBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  return create_houses(db, request, current_user)

@router.get('/', response_model=List[HouseBase])
def read_houses(
    db: Session = Depends(get_db),
    city: Optional[str] = None,
    sort_by: Optional[str] = Query(None, regex="^(price|size)$"), 
    sort_order: Optional[str] = Query("asc", regex="^(asc|desc)$")  
):
    return get_houses(db, city, sort_by, sort_order)

@router.get('/myhouses')
def read_user_houses(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user_houses = db.query(House).filter(House.user_id == current_user.id).all()
    if not user_houses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No houses found for the current user.")
    return user_houses

@router.get('/{id}', response_model=HouseDisplay)
def read_house(id:int, db: Session = Depends(get_db)):
  return get_house_by_id(db,id)

@router.post('/{id}/update')
def update_house(id: int, request:HouseBase, db: Session = Depends(get_db)):
  return update_house_by_id(db,id,request)

@router.get('/delete/{id}')
def delete_house(id: int, db: Session = Depends(get_db)):
  return delete_house_by_id(db,id)



@router.get('/mysavedhouses', response_model=List[HouseDisplay])
async def read_saved_houses(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    saved_houses = get_saved_houses_by_user(db, current_user.id)
    return saved_houses