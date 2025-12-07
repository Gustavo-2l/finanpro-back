from sqlalchemy.orm import Session
from models.goal_models import Goal
from schemas.goal_schema import GoalCreate


def create_goal(db: Session, user_id: int, goal: GoalCreate):
    new_goal = Goal(
        user_id=user_id,
        title=goal.title,
        description=goal.description,
        value=goal.value,
        deadline=goal.deadline
    )

    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)

    return new_goal


def get_user_goals(db: Session, user_id: int):
    return db.query(Goal).filter(Goal.user_id == user_id).all()
