from init_config import db


class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Customer %r>' % self.customer_name


class Agronomist(db.Model):
    agronomist_id = db.Column(db.Integer, primary_key=True)
    agronomist_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Customer %r>' % self.customer_name


class Sort(db.Model):
    sort_id = db.Column(db.Integer, primary_key=True)
    sort_name = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return '<Sort %r>' % self.sort_name


class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False, unique=True)
    price = db.Column(db.Numeric(12, 2), nullable=False)

    def __repr__(self):
        return '<Product %r>' % self.product_name
