from product import db


class Product(db.Model):
    """
        Product Schema 

        String: id - Primary Key
        String: name
        String: sku
        String: description
        Boolean: active
    """
    id = db.Column(db.String(40), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    sku = db.Column(db.String(200), unique=True, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def __init__(self, id, name, sku, description, active):
        self.id = id
        self.name = name
        self.sku = sku
        self.description = description
        self.active = active
