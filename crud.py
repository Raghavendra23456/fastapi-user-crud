from sqlalchemy.orm import Session 
import models,schemas

def create_user(db:Session,users:list[schemas.UserCreate]):


    hero=[]
    for user in users:
        db_user=models.User(name=user.name,age=user.age)
        hero.append(db_user)
    db.add_all(hero)
    db.commit()

    return hero
    

def read_user(db:Session,user_id:int):
    return db.query(models.User).filter(models.User.id==user_id).first()

def update_user(db:Session,user_id:int,user:schemas.UserCreate):
    db_user=db.query(models.User).filter(models.User.id==user_id).first()

    if not db_user:
        return None
    db_user.name=user.name
    db_user.age=user.age

    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db:Session,user_id:int):
    db_user=db.query(models.User).filter(models.User.id==user_id).first()

    if not db_user:
        return None
    
    db.delete(db_user)
    db.commit()
    return db_user