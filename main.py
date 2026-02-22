from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv
from typing import List, Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

students = []
with open("q-fastapi.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        students.append({"studentId": int(row["studentId"]), "class": row["class"]})

@app.get("/api")
def get_students(class_: Optional[List[str]] = Query(None, alias="class")):
    if class_:
        return {"students": [s for s in students if s["class"] in class_]}
    return {"students": students}
