import pytest
from app import create_app
from app import db


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


# @pytest.fixture
# def two_saved_planets(app):
#     # Arrange
#     ocean_book = Planet(name="Ocean Book",
#                         description="watr 4evr")
#     mountain_book = Planet(name="Mountain Book",
#                            description="i luv 2 climb rocks")

#     db.session.add_all([ocean_book, mountain_book])
#     # Alternatively, we could do
#     # db.session.add(ocean_book)
#     # db.session.add(mountain_book)
#     db.session.commit()
