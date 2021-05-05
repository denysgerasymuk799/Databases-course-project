from init_config import db


class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Customer %r>' % self.customer_name
