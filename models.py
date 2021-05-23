from init_config import db


class Agronomist(db.Model):
    agronomist_id = db.Column(db.Integer, primary_key=True)
    agronomist_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Agronomist %r>' % self.agronomist_name


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


class Sort_Product(db.Model):
    sort_id = db.Column(db.Integer, db.ForeignKey('sort.sort_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)

    def __repr__(self):
        return '<Sort_Product %r>' % self.product_id


class Degustation(db.Model):
    degustation_id = db.Column(db.Integer, primary_key=True)
    agronomist_id = db.Column(db.Integer, db.ForeignKey('agronomist.agronomist_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    degustation_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Degustation %r>' % self.degustation_id


class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Customer %r>' % self.customer_name


class Degustation_Customer(db.Model):
    degustation_id = db.Column(db.Integer, db.ForeignKey('degustation.degustation_id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)

    def __repr__(self):
        return '<Degustation_Customer %r>' % self.degustation_id


class Harvest(db.Model):
    harvest_id = db.Column(db.Integer, primary_key=True)
    sort_id = db.Column(db.Integer, db.ForeignKey('sort.sort_id'), nullable=False)
    agronomist_id = db.Column(db.Integer, db.ForeignKey('agronomist.agronomist_id'), nullable=False)
    harvest_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Harvest %r>' % self.harvest_id


class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    content = db.Column(db.String(10000), nullable=False)
    review_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Review %r>' % self.review_id


class Ordering(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    agronomist_id = db.Column(db.Integer, db.ForeignKey('agronomist.agronomist_id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    weight = db.Column(db.Numeric(12, 2), nullable=False)
    total_price = db.Column(db.Numeric(12, 2), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Order %r>' % self.order_id


class Order_Return(db.Model):
    return_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'), nullable=False)
    return_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Order_Return %r>' % self.return_id


class Trip(db.Model):
    trip_id = db.Column(db.Integer, primary_key=True)
    trip_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Trip %r>' % self.trip_id


class Trip_Agronomist(db.Model):
    agronomist_id = db.Column(db.Integer, db.ForeignKey('agronomist.agronomist_id'), nullable=False)
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.trip_id'), nullable=False)

    def __repr__(self):
        return '<Trip_Agronomist %r>' % self.trip_id
