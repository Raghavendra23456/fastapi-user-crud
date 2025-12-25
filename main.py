from fastapi import FastAPI,Depends,HTTPException
import models,schemas,crud
from sqlalchemy.orm import Session
from database import get_db,engine

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.post("/users/",response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate,db:Session=Depends(get_db)):
    return crud.create_user(db,user)

@app.get("/users/{user_id}",response_model=schemas.UserResponse)
def read_user(user_id:int,db:Session=Depends(get_db)):
    user=crud.read_user(db,user_id)
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    return user

@app.put("/users/{user_id}",response_model=schemas.UserResponse)

def update_user(user_id:int,user:schemas.UserCreate,db:Session=Depends(get_db)):
    updated_user=crud.update_user(db,user_id,user)

    if not updated_user:
        raise HTTPException(status_code=404,detail="user not found")
    return updated_user

@app.delete("/users/{user_id}")

def delete_user(user_id:int,db:Session=Depends(get_db)):
    deleted_user=crud.delete_user(db,user_id)

    if not deleted_user:
        raise HTTPException(status_code=404,detail="details not found")
    return {"message":"user deleted succesfully"}
              
   


      