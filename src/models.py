from sqlalchemy import Column, String, Integer, Numeric
from sqlalchemy.orm import validates
from .database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    vin = Column(String, primary_key=True, index=True)
    manufacturer_name = Column(String, nullable=False)
    description = Column(String)
    horse_power = Column(Integer, nullable=False)
    model_name = Column(String, nullable=False)
    model_year = Column(Integer, nullable=False)
    purchase_price = Column(Numeric(10, 2), nullable=False)
    fuel_type = Column(String, nullable=False)

    @validates('vin')
    def convert_upper(self, key, value):
        if(len(value) != 17):
            raise ValueError("VIN must be 17 characters long")
        return value.upper()

    @validates('model_year')
    def validate_year(self, key, value):
        if not (1900 <= value <= 2100):
            raise ValueError("Model year must be between 1900 and 2100")
        return value

    @validates('horse_power')
    def validate_horsepower(self, key, value):
        if value <= 0:
            raise ValueError("Horse power must be positive")
        return value

    @validates('purchase_price')
    def validate_price(self, key, value):
        if value <= 0:
            raise ValueError("Purchase price must be positive")
        return value

__all__ = ['Vehicle', 'Base'] # exports the vehicle and base classes