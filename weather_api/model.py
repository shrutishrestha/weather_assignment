from pydantic import BaseModel
from typing import List, Optional

class Coord(BaseModel):
    lon: float
    lat: float

class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str

class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: Optional[int] = None
    grnd_level: Optional[int] = None

class Wind(BaseModel):
    speed: float
    deg: int

class Clouds(BaseModel):
    all: int

class Sys(BaseModel):
    type: int
    id: int
    country: str
    sunrise: int
    sunset: int

class WeatherResponse(BaseModel):
    coord: Coord
    weather: List[Weather]
    base: str
    main: Main
    visibility: Optional[int] = None
    wind: Wind
    clouds: Clouds
    dt: int
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int
