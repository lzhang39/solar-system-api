import pytest
from app import create_app
from app import db

from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_saved_planets(app):
    # Arrange
    mercury = Planet(name="Mercury",
                     description="The hot planet",
                     order_from_sun=1)
    venus = Planet(name="Venus",
                   description="Goddess of beauty",
                   order_from_sun=2)

    db.session.add_all([mercury, venus])
    db.session.commit()
