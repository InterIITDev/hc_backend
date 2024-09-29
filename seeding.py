from sqlalchemy.orm import Session
from models.Models import Role  # Make sure to import your Role model

def seed_roles(db: Session):
    roles = [
        {"id":100, "name": "Admin", "description": "Administrator role"},
        {"id":1, "name": "User", "description": "Regular user role"},
        {"id":101, "name": "Moderator", "description": "Moderator role"},
        # Add more roles as needed
    ]

    for role in roles:
        existing_role = db.query(Role).filter(Role.name == role["name"]).first()
        if not existing_role:
            new_role = Role(id=role["id"], name=role["name"], description=role["description"])
            db.add(new_role)

    db.commit()
