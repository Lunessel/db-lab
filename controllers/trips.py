from flask import Blueprint, jsonify, request

from schemas.users import UserDTO
from services.trips import TripsService
from schemas.trips import TripDTO, CreateTripDTO


# Define the blueprint: 'trip', set its url prefix: /trip
trip_blueprint = Blueprint('trips', __name__, url_prefix='/trips')


@trip_blueprint.get("/")
def get_all_trips():
    trips = TripsService.get_all_trips()
    response = [TripDTO.model_validate(trip).model_dump() for trip in trips]
    return jsonify(response)



@trip_blueprint.get("/<int:id>")
def get_trip(id: int):
    trip = TripsService.get_trip_by_id(id=id)
    if not trip:
        return jsonify({"detail": "Trip not found"}), 404
    response = TripDTO.model_validate(trip).model_dump()
    return jsonify(response)


@trip_blueprint.post("/")
def create_trip():
    body = CreateTripDTO.model_validate(request.get_json())
    trip = TripsService().create_trip(
        start_time=body.start_time,
        end_time=body.end_time,
        price=body.price,
        user_id=body.user_id,
        driver_id=body.driver_id
    )
    response = TripDTO.model_validate(trip).model_dump()
    return jsonify(response)

@trip_blueprint.put("/<int:id>")
def update_trip(id: int):
    body = CreateTripDTO.model_validate(request.get_json())
    trip = TripsService().update_trip(
        id=id,
        start_time=body.start_time,
        end_time=body.end_time,
        price=body.price,
        user_id=body.user_id,
        driver_id=body.driver_id
    )
    response = TripDTO.model_validate(trip).model_dump()
    return jsonify(response)


@trip_blueprint.delete("/<int:id>")
def delete_trip(id: int):
    TripsService.delete_trip(id=id)
    return jsonify({"detail": "trip deleted successfully"})
