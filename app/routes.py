# from flask import Blueprint, jsonify

# hello_world_bp = Blueprint("hello_world", __name__)
# dog_bp = Blueprint("dog", __name__, url_prefix="/dogs")
# cat_bp = Blueprint("cat", __name__, url_prefix="/cats")

# class Cat:
#     def __init__(self, id, name, color, personality):
#         self.id = id
#         self.name = name
#         self.color = color
#         self.personality = personality
        

# cats = [
#     Cat(1, "Muna", "black", "sassy"),
#     Cat(2, "Matthew", "gray", "lazy")
# ]

# class Dog:
#     def __init__(self, id, name, breed, tricks=None):
#         self.id = id
#         self.name = name
#         self.breed = breed
#         if not tricks:
#             tricks = []
#         self.tricks = tricks

#     # this is just a dictionary, using flask it will return as JSON
#     def to_json(self):
#         if not self.tricks:
#             tricks = "NO tricks"
#         else:
#             tricks = self.tricks

#         return {
#             "id": self.id,
#             "name": self.name,
#             "breed": self.breed,
#             "tricks": self.tricks
#         }

# dogs = [
#     Dog(1, "mac", "greyhound"),
#     Dog(2, "sparky", "schnauzer"),
#     Dog(3, "teddy", "golden retriever")
# ]

# # get all cats
# @cat_bp.route("", methods = ["GET"])
# def handle_cats():
#     cats_response = [vars(cat) for cat in cats]
#     return jsonify(cats_response)

# # get one cat
# @cat_bp.route("/<cat_id>", methods = ["GET"])
# def handle_cats(cat_id):
#     # Using try and except for the edge case of if a non integar is entered
#     try:
#         cat_id = int(cat_id)
#     except:
#         return "Bad data", 400
#     for cat in cats:
#         if cat_id == cat.id:
#             return vars(cat)
#     return "Not found", 404



# @hello_world_bp.route("/hello-world", methods = ["GET"])
# def hellow_world():
#     return "hello world!"


# @dog_bp.route("", methods = ["GET"])
# def handle_dogs():
#     dogs_response = []
#     for dog in dogs:
#         dogs_response.append(
#             #vars(dog)
#             # "id": dog.id,
#             # "name": dog.name,
#             # "breed":dog.breed,
#             # "tricks":dog.tricks
#             dog.to_json()
#         )

#     # return jsonify(dogs_response)
#     return jsonify(dogs_response)

# @dog_bp.route("/<dog_id>", methods =["GET"])
# def handle_dog(dog_id):
#     dog_id = int(dog_id)
#     for dog in dogs:
#         if dog.id == dog_id:
#             # return {
#             #     "id": dog.id,
#             #     "name": dog.name,
#             #     "breed":dog.breed,
#             #     "tricks":dog.tricks
#             # }
#             return dog.to_json()
