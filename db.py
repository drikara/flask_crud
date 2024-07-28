from flask import Flask
from sqlalchemy import create_engine,MetaData,URL,Table

from dotenv import load_dotenv
import os

load_dotenv()
db_engine_url = URL.create(
    os.getenv('DB_ENGINE')+"+"+os.getenv("DB_CONNECTOR"),
    username = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    host = os.getenv("DB_HOST"),
    database = os.getenv("DB_NAME")
)
engine = create_engine(db_engine_url,echo=True)
meta = MetaData()
students = Table("students",meta,autoload_with=engine)
def n_inscription(nom,prenoms,age):
    req = students.insert().values(nom=nom,prenoms=prenoms,age=age)
    with engine.connect() as conn:
        try:
            conn.execute(req)
            
        except Exception as e:
            return f"Erreur lors de l'inserton:{e}"
        else:
            conn.commit()
            return "Insertion réussie"

def get_students():
    query = students.select()
    with engine.connect() as conn:
        resultat = conn.execute(query)
        return resultat.fetchall()
def delete_student(id):
    query = students.delete().where(students.c.id==id)
    with engine.connect() as conn:
        try:
            conn.execute(query)
        except Exception as e:
            return f"Erreur lors de la suppresion"
        else:
            conn.commit()
            return "Suppresion réussie"
        
def modify_student(id,nom,prenoms,age):
    req = students.update().where(students.c.id==id).values(nom=nom,prenoms=prenoms,age=age)
    with engine.connect() as conn:
        try:
            conn.execute(req)
        except Exception as e:
            return f"Erreur lors de la modification :{e}"
        else:
            conn.commit()
            return "Modification réussie"
