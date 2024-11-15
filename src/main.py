from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import models
from . import schemas
from .database import get_db, engine, Base
from typing import List

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/vehicle", response_model=List[schemas.Vehicle])
def get_vehicles(db: Session = Depends(get_db)):
    return db.query(models.Vehicle).all()

@app.post("/vehicle", response_model=schemas.Vehicle, status_code=status.HTTP_201_CREATED)
def create_vehicle(vehicle: schemas.VehicleCreate, db: Session = Depends(get_db)):
    try:
        db_vehicle = models.Vehicle(**vehicle.model_dump())
        db.add(db_vehicle)
        db.commit()
        db.refresh(db_vehicle)
        return db_vehicle
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Vehicle with this VIN already exists"
        )
    except ValueError as e:
        raise HTTPException(
            status_code=422,
            detail=str(e)
        )

@app.get("/vehicle/{vin}", response_model=schemas.Vehicle)
def get_vehicle(vin: str, db: Session = Depends(get_db)):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.vin == vin.upper()).first()
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@app.put("/vehicle/{vin}", response_model=schemas.Vehicle)
def update_vehicle(vin: str, vehicle: schemas.VehicleBase, db: Session = Depends(get_db)):
    db_vehicle = db.query(models.Vehicle).filter(models.Vehicle.vin == vin.upper()).first()
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    try:
        for key, value in vehicle.model_dump().items():
            setattr(db_vehicle, key, value)
        db.commit()
        db.refresh(db_vehicle)
        return db_vehicle
    except ValueError as e:
        db.rollback()
        raise HTTPException(
            status_code=422,
            detail=str(e)
        )

@app.delete("/vehicle/{vin}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vehicle(vin: str, db: Session = Depends(get_db)):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.vin == vin.upper()).first()
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    db.delete(vehicle)
    db.commit()
    return None