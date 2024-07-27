from models import db, connect_db, User, Feedback
from app import app

# Create all tables
with app.app_context():
    db.drop_all()
    db.create_all()

    # If table isn't empty, empty it
    User.query.delete()
    Feedback.query.delete()

    # Add users
    user1 = User.register(
        username="john_doe",
        password="password123",
        first_name="John",
        last_name="Doe",
        email="john@example.com"
    )

    user2 = User.register(
        username="jane_smith",
        password="password123",
        first_name="Jane",
        last_name="Smith",
        email="jane@example.com"
    )

    db.session.add(user1)
    db.session.add(user2)

    # Add feedback
    feedback1 = Feedback(
        title="Great Service",
        content="I really enjoyed the service provided!",
        username="john_doe"
    )

    feedback2 = Feedback(
        title="Needs Improvement",
        content="The service could be faster.",
        username="jane_smith"
    )

    db.session.add(feedback1)
    db.session.add(feedback2)

    # Commit the transactions
    db.session.commit()
