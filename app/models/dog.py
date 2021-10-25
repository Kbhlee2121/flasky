from app import db 

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    breed = db.Column(db.String)
    # tricks can be many to many or one to zero/many


    # this is just a dictionary, using flask it will return as JSON
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "breed": self.breed,
        }