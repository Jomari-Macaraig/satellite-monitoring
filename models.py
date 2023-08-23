from sqlalchemy import Column, Float, Date

from database import Base


class SatelliteInfo(Base):
    __tablename__ = "satellite_info"

    last_updated = Column(Date)
    altitude = Column(Float)
