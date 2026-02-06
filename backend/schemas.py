from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class AftermathCreate(BaseModel):
    text: str
    motifs: List[str]
    personas: List[str]

class MetricIngest(BaseModel):
    mode: str
    cr: float
    aov: float
    ltv: float
    refund: float
    ttv: float
    velocity: float
    dependence: float

class CellSlice(BaseModel):
    amount: float
    tax_pct: float = 0.3
    reserve_pct: float = 0.2
    ops_pct: float = 0.4
    draw_pct: float = 0.1

class EventWebhook(BaseModel):
    source: str
    payload: dict

class SimRun(BaseModel):
    scenario_name: str
    params: dict