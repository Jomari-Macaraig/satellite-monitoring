from datetime import date
from sqlalchemy.orm import Session

import models, schemas


def get_satellite_info(db: Session):
    return db.query(models.SatelliteInfo).all()


def create_satellite_info(db: Session, raw_satellite_info: schemas.SatelliteInfoCreate):
    satellite_info = models.SatelliteInfo(
        last_updated=raw_satellite_info.last_updated,
        altitude=raw_satellite_info.altitude
    )
    db.add(satellite_info)
    db.commit()
    db.refresh(satellite_info)
    return satellite_info
