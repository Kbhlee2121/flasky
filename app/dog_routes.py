from flask import Blueprint, jsonify

dog_bp = Blueprint("dog", __name__, url_prefix="/dogs")

class Dog:
    def __init__(self, id, name, breed, tricks=None):
        self.id = id
        self.name = name
        self.breed = breed
        if not tricks:
            tricks = []
        self.tricks = tricks

    # this is just a dictionary, using flask it will return as JSON
    def to_json(self):
        if not self.tricks:
            tricks = "NO tricks"
        else:
            tricks = self.tricks

        return {
            "id": self.id,
            "name": self.name,
            "breed": self.breed,
            "tricks": self.tricks
        }

dogs = [
    Dog(1, "mac", "greyhound"),
    Dog(2, "sparky", "schnauzer"),
    Dog(3, "teddy", "golden retriever")
]

@dog_bp.route("", methods = ["GET"])
def handle_dogs():
    dogs_response = []
    for dog in dogs:
        dogs_response.append(
            #vars(dog)
            # "id": dog.id,
            # "name": dog.name,
            # "breed":dog.breed,
            # "tricks":dog.tricks
            dog.to_json()
        )

    # return jsonify(dogs_response)
    return jsonify(dogs_response)

@dog_bp.route("/<dog_id>", methods =["GET"])
def handle_dog(dog_id):
    dog_id = int(dog_id)
    for dog in dogs:
        if dog.id == dog_id:
            # return {
            #     "id": dog.id,
            #     "name": dog.name,
            #     "breed":dog.breed,
            #     "tricks":dog.tricks
            # }
            return dog.to_json()
