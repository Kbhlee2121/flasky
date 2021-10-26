from flask import Blueprint, jsonify

cat_bp = Blueprint("cat", __name__, url_prefix="/cats")

class Cat:
    def __init__(self, id, name, color, personality):
        self.id = id
        self.name = name
        self.color = color
        self.personality = personality
        

cats = [
    Cat(1, "Muna", "black", "mischevious"),
    Cat(2, "Matthew", "spotted", "cuddly"),
    Cat(3, "George", "Gray","Sassy")
]

# get all cats
@cat_bp.route("", methods = ["GET"])
def get_all_cats():
    cats_response = [vars(cat) for cat in cats]
    return jsonify(cats_response)

# get one cat
@cat_bp.route("/<cat_id>", methods = ["GET"])
def get_one_cats(cat_id):
    # Using try and except for the edge case of if a non integar is entered
    try:
        cat_id = int(cat_id)
    except:
        return "Bad data", 400

    for cat in cats:
        if cat_id == cat.id:
            return vars(cat)
    return "Not found", 404