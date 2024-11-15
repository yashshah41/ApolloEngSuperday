from pydantic import BaseModel, Field, validator, ConfigDict
from decimal import Decimal
from typing import Optional

class VehicleBase(BaseModel):
    manufacturer_name: str = Field(..., min_length=1)
    description: Optional[str] = None
    horse_power: int = Field(..., gt=0)
    model_name: str = Field(..., min_length=1)
    model_year: int = Field(..., ge=1900, le=2100)
    purchase_price: Decimal = Field(..., gt=0)
    fuel_type: str = Field(..., min_length=1)
    model_config = ConfigDict(
        protected_namespaces=()
    )

class VehicleCreate(VehicleBase):
    vin: str = Field(..., min_length=17, max_length=17)

    @validator('vin')
    def validate_vin(cls, v):
        return v.upper()

class Vehicle(VehicleBase):
    vin: str

    class Config:
        from_attributes = True

class ErrorResponse(BaseModel):
    detail: str