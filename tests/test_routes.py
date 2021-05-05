def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


# (doing the opposite of testing one planet with no data, trying to get a pass with 404)
# (before was doing a test with no data in test db/fixture NUMBER 2...)
def test_get_missing_planet(client):
    # Act
    response = client.get("/planets/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404


def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "The hot planet",
        "order_from_sun": 1
    }


def test_get_all_planets(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{"id": 1, "name": "Mercury",
                              "description": "The hot planet",
                              "order_from_sun": 1},
                             {"name": "Venus",
                              "description": "Goddess of beauty",
                              "id": 2,
                              "order_from_sun": 2}]


# def test_create_one_planet(client):
#     # Act
#     response = client.post("/planets")
#     request_body = {"name": "Venus",
#                     "description": "Goddess of beauty",
#                     "order_from_sun": 2}
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 201
#     # assert response_body == {"name": "Venus",
#     #                           "description": "Goddess of beauty",
#     #                           "id": 2,
#     #                           "order_from_sun": 2}


def test_create_one_planet(client):
    response = client.post("/planets", {"name": "Venus",
                                        "description": "Goddess of beauty",
                                        "order_from_sun": 2})
    response_body = response.get_json()

    assert response.status_code == 201
    # assert response_body == {"name": "Venus",
    #                          "description": "Goddess of beauty",
    #                          "id": 2,
    #                          "order_from_sun": 2}
