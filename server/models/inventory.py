from models.db import db
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer)
    unit_price = db.Column(db.Float)
    supplier = db.Column(db.String(100))
    date_added = db.Column(db.Date)
    last_update = db.Column(db.Date)
    warning_limit = db.Column(db.Integer)
    location = db.Column(db.String(100))
    user_id = db.Column(db.Integer())

    def __repr__(self):
        return f'<Inventory {self.item_name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'item_name': self.item_name,
            'category': self.category,
            'quantity': self.quantity,
            'unit_price': self.unit_price,
            'supplier': self.supplier,
            'date_added': self.date_added,
            'last_update': self.last_update,
            'warning_limit': self.warning_limit,
            'location': self.location
        }