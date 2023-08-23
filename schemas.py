from pydantic import BaseModel
from datetime import date


class SatelliteInfoBase(BaseModel):
    last_updated: date
    altitude: float


class SatelliteInfoCreate(SatelliteInfoBase):
    pass


class SatelliteInfo(SatelliteInfoBase):

    class Config:
        orm_mode = True
