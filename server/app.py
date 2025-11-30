from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --------------------
# MODELS
# --------------------
class Plant(db.Model):
    __tablename__ = "plants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_in_stock = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "price": self.price,
            "is_in_stock": self.is_in_stock,
        }


# ROUTES


# GET all plants
@app.route('/plants', methods=['GET'])
def get_plants():
    plants = Plant.query.all()
    return jsonify([plant.to_dict() for plant in plants]), 200


# GET one plant
@app.route('/plants/<int:id>', methods=['GET'])
def get_plant(id):
    plant = Plant.query.get_or_404(id)
    return jsonify(plant.to_dict()), 200


# POST new plant
@app.route('/plants', methods=['POST'])
def post_plant():
    data = request.get_json()
    new_plant = Plant(
        name=data['name'],
        image=data['image'],
        price=data['price'],
        is_in_stock=data.get('is_in_stock', True)
    )
    db.session.add(new_plant)
    db.session.commit()
    return jsonify(new_plant.to_dict()), 201


# PATCH update plant
@app.route('/plants/<int:id>', methods=['PATCH'])
def patch_plant(id):
    plant = Plant.query.get_or_404(id)
    data = request.get_json()

    if "name" in data:
        plant.name = data["name"]
    if "image" in data:
        plant.image = data["image"]
    if "price" in data:
        plant.price = data["price"]
    if "is_in_stock" in data:
        plant.is_in_stock = data["is_in_stock"]

    db.session.commit()
    return jsonify(plant.to_dict()), 200


# DELETE plant
@app.route('/plants/<int:id>', methods=['DELETE'])
def delete_plant(id):
    plant = Plant.query.get_or_404(id)
    db.session.delete(plant)
    db.session.commit()
    return '', 204


if __name__ == '__main__':
    app.run(port=5555, debug=True)




































