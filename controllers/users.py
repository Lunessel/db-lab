# blueprints/user.py
from flask import Blueprint, jsonify, request

from schemas.trips import UserWithTripDTO, TripDTO
from services.users import UsersService
from schemas.users import UserDTO, CreateUserDTO


# Define the blueprint: 'user', set its url prefix: /user
user_blueprint = Blueprint('users', __name__, url_prefix='/users')


@user_blueprint.get("/")
def get_all_users():
    users = UsersService.get_all_users()
    response = [UserWithTripDTO.model_validate(user).model_dump() for user in users]
    return jsonify(response)


@user_blueprint.get("/<int:id>")
def get_user(id: int):
    user = UsersService.get_user_by_id(id=id)
    response = UserWithTripDTO.model_validate(user).model_dump()
    return jsonify(response)

@user_blueprint.post("/")
def create_user():
    body = CreateUserDTO.model_validate(request.get_json())
    user = UsersService.create_user(
        name=body.name,
        phone_number=body.phone_number,
        email=body.email,
        rating=body.rating
    )
    response = UserDTO.model_validate(user).model_dump()
    return jsonify(response)

@user_blueprint.put("/<int:id>")
def update_user(id: int):
    body = CreateUserDTO.model_validate(request.get_json())
    user = UsersService.update_user(
        id=id,
        name=body.name,
        phone_number=body.phone_number,
        email=body.email,
        rating=body.rating
    )
    response = UserDTO.model_validate(user).model_dump()
    return jsonify(response)

@user_blueprint.delete("/<int:id>")
def delete_user(id: int):
    UsersService.delete_user(id=id)
    return jsonify({"detail": "User deleted successfully"})
