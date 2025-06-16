from dataclasses import dataclass, field
from typing import List, Dict, Any, Iterator, Optional
import json


@dataclass
class City:
    name: str
    lat: float
    lon: float
    district: str
    population: int
    subject: str

