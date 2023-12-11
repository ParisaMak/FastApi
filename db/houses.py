from sqlalchemy.orm import Session
from db.schemas import HouseBase
from db.models import House, User, SavedHouse
from sqlalchemy import desc, asc
from typing import Optional


def create_houses(db: Session,request: HouseBase, current_user: User):
    new_house= House( 
        price = request.price,
        user_id=current_user.id,
        bedrooms = request.bedrooms,
        bathrooms = request.bathrooms,
        size= request.size,
        houseNumber = request.houseNumber,
        numberAddition = request.numberAddition,
        streetName = request.streetName,
        Zip = request.Zip,
        city = request.city,
        constructionYear = request.constructionYear,
        hasGarage = request.hasGarage,
        description = request.description,
        category = request.category)
    db.add(new_house)
    db.commit()
    db.refresh(new_house)
    return  new_house


def create_saved_houses(db: Session,request: HouseBase, current_user: User):
    new_house= House( 
        price = request.price,
        user_id=current_user.id,
        bedrooms = request.bedrooms,
        bathrooms = request.bathrooms,
        size= request.size,
        houseNumber = request.houseNumber,
        numberAddition = request.numberAddition,
        streetName = request.streetName,
        Zip = request.Zip,
        city = request.city,
        constructionYear = request.constructionYear,
        hasGarage = request.hasGarage,
        description = request.description,
        category = request.category)
    db.add(new_house)
    db.commit()
    db.refresh(new_house)
    return  new_house


def get_houses(db: Session, city:Optional[str], sort_by:Optional[str], sort_order: Optional[str]):
    query = db.query(House)
    
    if city:
        query = query.filter(House.city == city)

    if sort_by:
        order = desc if sort_order =='desc' else asc
        if sort_by == 'price':
            query = query.order_by(order(House.price))
        elif sort_by == 'size':
            query = query.order_by(order(House.size))
    return query.all()


def get_house_by_id(db: Session, id: int ):
    house = db.query(House).filter(House.id == id).first()
    return house

def get_saved_houses_by_user(db: Session, user_id: int):
    saved_houses = db.query(House).join(SavedHouse, House.id == SavedHouse.house_id).filter(SavedHouse.user_id == user_id).all()
    return saved_houses

def update_house_by_id(db: Session, id: int ,request:HouseBase):
    house = db.query(House).filter(House.id == id)
    house.update({
        House.price :request.price,
        House.bedrooms : request.bedrooms,
        House.bathrooms :request.bathrooms,
        House.size :request.size,
        House.houseNumber : request.houseNumber,
        House.numberAddition : request.numberAddition,
        House.streetName : request.streetName,
        House.Zip : request.Zip,
        House.city : request.city,
        House.constructionYear : request.constructionYear,
        House.hasGarage : request.hasGarage,
        House.description : request.description
    })
    db.commit()
    return 'ok'

def delete_house_by_id(db: Session, id: int ):
    house = db.query(House).filter(House.id == id).first() 
    db.delete(house)
    db.commit()
    return 'ok'