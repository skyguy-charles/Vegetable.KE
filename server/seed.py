from app import app, db, Plant

with app.app_context():
    # Drop all tables and recreate them
    db.drop_all()
    db.create_all()

    # Add sample plants
    plants = [
        Plant(name="Aloe Vera", image="https://example.com/aloe.png", price=10.5, is_in_stock=True),
        Plant(name="Snake Plant", image="https://example.com/snake.png", price=15.0, is_in_stock=True),
        Plant(name="Peace Lily", image="https://example.com/peace.png", price=20.0, is_in_stock=False),
    ]

    db.session.add_all(plants)
    db.session.commit()

    print("🌱 Database seeded with sample plants!")




















