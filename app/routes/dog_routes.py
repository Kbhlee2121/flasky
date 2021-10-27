from app import db 
from app.models.dog import Dog
from flask import Blueprint, jsonify, make_response, request, abort
import random

dog_bp = Blueprint("dog", __name__, url_prefix="/dogs")

# Helper Functions
def valid_int(number, parameter_type):
    try:
        number = int(number)
    except:
        # abort(make_response({"error": "parameter_type must be an int"}, 400))
        abort(400, {"error": f"{parameter_type} must be an int"})

def get_dog_from_id(dog_id):
    valid_int(dog_id, "dog_id")

    # .get_or_404 is an alternative to using if dog is None
    return Dog.query.get_or_404(dog_id, description ="{dog not found}")

@dog_bp.route("/<dog_id>/add_chip", methods=["PATCH"])
def add_chip_to_dog(dog_id):
    dog = get_dog_from_id(dog_id)
    chip = str(random.randint(1000,9999))
    dog.chip = chip
    db.session.commit()
    
    return (dog.to_dict())


# Create dog and get all dogs
@dog_bp.route("", methods=["GET"])
def read_all_dogs():
    age_query = request.args.get("age")
    older_query = request.args.get("older")
    sort_query = request.args.get("sort")

    # dogs?age=2&sort=asc
    # dogs = Dog.query

    if age_query:
        valid_int(age_query, "age")
        dogs = Dog.query.filter_by(age=age_query)
    # query: dogs?older=2
    elif older_query:
        valid_int(older_query, "older")
        dogs = Dog.query.filter(Dog.age > older_query)
    # dogs?sort=asc
    elif sort_query == "asc":
        dogs = Dog.query.order_by(Dog.age.asc())
    elif sort_query == "desc":
        dogs = Dog.query.order_by(Dog.age.desc())
    else:
        dogs = Dog.query.all()

    dogs_response = []
    for dog in dogs:
        dogs_response.append(
            dog.to_dict()
        )

    # return jsonify(dogs_response)
    return jsonify(dogs_response)

@dog_bp.route("", methods =["POST"])
def create_dog():
    request_body = request.get_json()
    # request method takes the JSON in the HTTP request and gives us a python dict
    if "name" not in request_body or "breed" not in request_body or "age" not in request_body:
        return {"error": "incomplete request body"}, 400

    new_dog = Dog (
        name = request_body["name"],
        breed = request_body["breed"],
        age = request_body["age"]
    )

    db.session.add(new_dog)
    db.session.commit()

    return make_response(f"Dog {new_dog.name} created!", 201)

# Routes
@dog_bp.route("/<dog_id>", methods=["GET"])
def get_dog(dog_id):
    dog = get_dog_from_id(dog_id)
    return dog.to_dict()

@dog_bp.route("/<dog_id>", methods=["PATCH"])
def update_dog(dog_id):
    dog = get_dog_from_id(dog_id)
    request_body = request.get_json()
    if "name" in request_body:
        dog.name = request_body["name"]
    if "breed" in request_body:
        dog.breed = request_body["breed"]
    if "age" in request_body:
        dog.age = request_body["age"]

    db.session.commit()
    return jsonify(dog.to_dict())

@dog_bp.route("/<dog_id>", methods =["DELETE"])
def delete_dog(dog_id):
    dog = get_dog_from_id(dog_id)
    db.session.delete(dog)
    db.session.commit()
    return jsonify(dog.to_dict(), 204)
