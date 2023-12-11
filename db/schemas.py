from typing import List
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from db.models import HouseCategory

class UserBase(BaseModel):
    username: str
    email: str
    password:str
 
class HouseBase(BaseModel):
    price: float
    bedrooms: int
    bathrooms: int
    size: float
    houseNumber: int
    numberAddition: Optional[str] = None
    streetName: str
    Zip: str
    city: str
    constructionYear: int
    hasGarage: bool
    description: Optional[str] = None
    category: HouseCategory

class User(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

        
class SavedHouseBase(BaseModel):
    user_id: int
    house_id: int
    saved_date: datetime

    class Config:
        orm_mode = True

class HouseDisplay(BaseModel):
    price: float
    bedrooms: int
    bathrooms: int
    size: float
    houseNumber: int
    numberAddition: Optional[str] = None
    streetName: str
    Zip: str
    city: str
    constructionYear: int
    hasGarage: bool
    description: Optional[str] = None
    user: User
    saved_by_users: List[SavedHouseBase] = []
    class Config:
        orm_mode = True

class UserDisplay(BaseModel):
    username: str
    email: str
    saved_houses: List[SavedHouseBase] = []
    class Config:
        orm_mode = True
       