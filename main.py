from fastapi import FastAPI, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from models import Base, User, Relation_Routes_Stations, Stations
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:password@localhost/2024SparcsHackathon"  # MySQL 연결 문자열 수정

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 라우트 정의
@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.post("/login")
def login(login_id: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.login_id == login_id).first()
    if not user or not user.password == password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"message": "Login successful"}

@app.get("/selectRoute")
def select_route(route_id: int, db: Session = Depends(get_db)):
    join_query = db.query(
        Relation_Routes_Stations.station_id,
        Stations.name,
        Stations.latitude,
        Stations.longitude
    ).join(Stations, Relation_Routes_Stations.station_id == Stations.id).filter(Relation_Routes_Stations.route_id == route_id).all()
    return join_query
