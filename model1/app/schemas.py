
from pydantic import BaseModel

class HouseFeatures(BaseModel):
    OverallQual: int
    GrLivArea: float
    TotalBsmtSF: float
    GarageCars: int
    FirstFlrSF: float
    GarageArea: float
    BsmtFinSF1: float
    YearBuilt: int
    FullBath: int
    TotRmsAbvGrd: int
    YearRemodAdd: int
    Fireplaces: int
    MasVnrArea: float
    LotArea: float
    OverallCond: int
