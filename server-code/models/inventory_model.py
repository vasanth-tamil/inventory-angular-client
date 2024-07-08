from models.model import Model

class Inventory(Model):
    def __init__(self, _id=None, item_name=None, category=None, quantity=0, unit_price=0, supplier=None, date_added=None, last_update=None, reorderd_level=0, location=None):
        self.id = _id
        self.item_name = item_name
        self.category = category
        self.quantity = quantity
        self.unit_price = unit_price
        self.supplier = supplier
        self.date_added = date_added
        self.last_update = last_update
        self.reorderd_level = reorderd_level
        self.location = location

        super().__init__()

    def create(self):
        self.cursor.execute(
            "INSERT INTO inventory (item_name, category, quantity, unit_price, supplier, date_added, last_update, warning_limit, location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (self.item_name, self.category, self.quantity, self.unit_price, self.supplier, self.date_added, self.last_update, self.warning_limit, self.location,)
        )
        self.commit()

    def update(self, id):
        self.cursor.execute(
            "UPDATE inventory SET item_name = %s, category = %s, quantity = %s, unit_price = %s, supplier = %s, last_update = %s, warning_limit = %s, location = %s WHERE ID = %s",
            (self.item_name, self.category, self.quantity, self.unit_price, self.supplier, self.last_update, self.warning_limit, self.location, id,)
        )
        self.commit()

    def set_limit(id, limit):
        model = Model()
        model.cursor.execute(
            "UPDATE inventory SET warning_limit = %s WHERE ID = %s",
            (limit, id,)
        )
        model.commit()

    @staticmethod
    def get_by_id(id):
        model = Model()
        model.cursor.execute("SELECT * FROM inventory WHERE ID = %s", (id,))
        inventory = model.cursor.fetchone()
        return inventory

    @staticmethod
    def get_all():
        model = Model()
        model.cursor.execute("SELECT * FROM inventory")
        inventory = model.cursor.fetchall()
        return inventory

    
    @staticmethod
    def delete(id: int):
        model = Model()
        model.cursor.execute("DELETE FROM inventory WHERE ID = %s", (id,))
        model.commit()