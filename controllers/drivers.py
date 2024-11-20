from flask import Blueprint, jsonify, request
from services.drivers import DriversService
from schemas.drivers import DriverDTO, CreateDriverDTO
from schemas.trips import DriverWithTripDTO

# Define the blueprint: 'driver', set its url prefix: /driver
driver_blueprint = Blueprint('drivers', __name__, url_prefix='/drivers')


@driver_blueprint.get("/")
def get_all_drivers():
    drivers = DriversService.get_all_drivers()
    response = [DriverWithTripDTO.model_validate(driver.__dict__).model_dump() for driver in drivers]
    return jsonify(response)


@driver_blueprint.get("/<int:id>")
def get_driver(id: int):
    driver = DriversService.get_driver_by_id(id=id)
    response = DriverWithTripDTO.model_validate(driver.__dict__).model_dump()
    return jsonify(response)


@driver_blueprint.post("/")
def create_driver():
    body = CreateDriverDTO.model_validate(request.get_json())
    driver = DriversService.create_driver(
        name=body.name,
        licence_number=body.licence_number,
        phone_number=body.phone_number,
        rating=body.rating,
        experince_years=body.experince_years,
        status=body.status
    )
    response = DriverDTO.model_validate(driver.__dict__).model_dump()
    return jsonify(response)
@driver_blueprint.put("/<int:id>")
def update_driver(id: int):
    body = CreateDriverDTO.model_validate(request.get_json())
    driver = DriversService.update_driver(
        id=id,
        name=body.name,
        licence_number=body.licence_number,
        phone_number=body.phone_number,
        rating=body.rating,
        experince_years=body.experince_years,
        status=body.status
    )
    response = DriverDTO.model_validate(driver.__dict__).model_dump()
    return jsonify(response)

@driver_blueprint.delete("/<int:id>")
def delete_driver(id: int):
    DriversService.delete_driver(id=id)
    return jsonify({"detail": "driver deleted successfully"})
