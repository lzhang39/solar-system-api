from app import db
from flask import Blueprint
from flask import request
from flask import jsonify
from .models.planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["POST"], strict_slashes=False)
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        order_from_sun=request_body["order_from_sun"])

    db.session.add(new_planet)
    db.session.commit()

    return {
        "success": True,
        "message": f"Planet {new_planet.name} has been created"
    }, 201


@planets_bp.route("", methods=["GET"], strict_slashes=False)
def planet_index():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "order_from_sun": planet.order_from_sun
        })

    return jsonify(planets_response), 200


@planets_bp.route("/<planet_id>", methods=["GET"], strict_slashes=False)
def get_one_planet(planet_id):
    # if not isinstance(planet_id, int):
    #     return {
    #         "success": False,
    #         "message": f"ID {planet_id} must be an integer"
    #     }, 400

    planet = Planet.query.get(planet_id)

    if planet:
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "order_from_sun": planet.order_from_sun
        }, 200

    return {
        "success": False,
        "message": f"Planet with ID {planet_id} was not found"
    }, 404
