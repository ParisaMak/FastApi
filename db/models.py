from db.database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime ,Float, Enum
from datetime import datetime
from sqlalchemy.orm import relationship
import enum

class HouseCategory(enum.Enum):
    HOUSE = "house"
    APARTMENT = "apartment"
    STUDIO = "studio"
    LOFT = "loft"

class House(Base):
    __tablename__ = "houses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="houses")
    saved_by_users = relationship("SavedHouse")
    price = Column(Float, index=True)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    size= Column(Float )  
    houseNumber = Column(Integer)
    numberAddition = Column(String)
    streetName = Column(String, index=True)
    Zip = Column(String, index=True)
    city = Column(String ,index=True)
    constructionYear = Column(Integer)
    hasGarage = Column(Boolean)
    description = Column(String)
    creation_date = Column(DateTime ,default=datetime.utcnow)
    category = Column(Enum(HouseCategory))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    houses = relationship("House", back_populates="user")
    saved_houses = relationship("SavedHouse", back_populates="user")


class SavedHouse(Base):
    __tablename__ =  'saved_houses'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    house_id = Column(Integer, ForeignKey('houses.id'), primary_key=True)
    saved_date = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="saved_houses")
    house = relationship("House")