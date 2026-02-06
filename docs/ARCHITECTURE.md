# Architecture

## Data Flow
1. Events → Router → Actions → Metrics Update
2. Frontend caches data via PWA/IndexedDB
3. Sims run Monte Carlo on scenarios

## Diagrams
- Backend: FastAPI routers
- Frontend: React components
- Infra: Docker services