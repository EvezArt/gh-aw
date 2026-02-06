from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models import *
from schemas import *
import jwt
from datetime import datetime
from simulations import run_simulation

app = FastAPI()

SECRET_KEY = "your-secret-key"

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/aftermath/seed")
def seed_aftermath(data: AftermathCreate, db: Session = Depends(get_db)):
    aftermath = Aftermath(**data.dict(), created_at=datetime.utcnow(), alignment_score=0.0)
    db.add(aftermath)
    db.commit()
    return {"id": aftermath.id}

@app.post("/aftermath/scan")
def scan_aftermaths(db: Session = Depends(get_db)):
    # Stub: fetch RSS, compute similarity
    aftermaths = db.query(Aftermath).all()
    for a in aftermaths:
        a.alignment_score += 0.1  # Stub update
    db.commit()
    return {"scanned": len(aftermaths)}

@app.post("/metrics/ingest")
def ingest_metrics(data: MetricIngest, db: Session = Depends(get_db)):
    metric = Metric(**data.dict(), ts=datetime.utcnow())
    db.add(metric)
    db.commit()
    return {"id": metric.id}

@app.get("/metrics/current")
def get_current_metrics(db: Session = Depends(get_db)):
    # Stub latest
    return {"digital": {"cr": 0.05}, "service": {"cr": 0.1}, "tool": {"cr": 0.02}}

@app.post("/cells/slice")
def slice_cells(data: CellSlice, db: Session = Depends(get_db)):
    # Stub slicing logic
    slices = {
        "tax": data.amount * data.tax_pct,
        "reserve": data.amount * data.reserve_pct,
        "ops": data.amount * data.ops_pct,
        "draw": data.amount * data.draw_pct
    }
    # Update cells/tx
    return slices

@app.get("/cells/balances")
def get_balances(db: Session = Depends(get_db)):
    cells = db.query(Cell).all()
    return [{"name": c.name, "balance": c.balance} for c in cells]

@app.post("/router/webhook")
def router_webhook(data: EventWebhook, db: Session = Depends(get_db)):
    # Threshold logic
    action = "SCALE"
    if data.payload.get("refund", 0) > 0.08:
        action = "HARDEN"
    # Add more thresholds
    event = Event(ts=datetime.utcnow(), source=data.source, payload=data.payload, router_action=action)
    db.add(event)
    db.commit()
    return {"action": action}

@app.post("/nav/test-offline")
def test_offline(db: Session = Depends(get_db)):
    # Stub 24h sim
    log = NavLog(ts=datetime.utcnow(), path_used="/dashboard", latency_ms=100, offline_mode=True, breach_attempts=0)
    db.add(log)
    db.commit()
    return {"tested": True}

@app.post("/sims/run")
def run_sim(data: SimRun, db: Session = Depends(get_db)):
    polygon, win_prob = run_simulation(data.scenario_name, data.params)
    sim = Sim(scenario_name=data.scenario_name, params=data.params, result_polygon=polygon, win_probability=win_prob)
    db.add(sim)
    db.commit()
    return {"polygon": polygon, "win_probability": win_prob}

@app.get("/dossier/daily")
def get_daily_dossier():
    # Stub
    return {"timeline": "Archived future events here"}