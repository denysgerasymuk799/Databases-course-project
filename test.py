from sqlalchemy import *

s1 = select(customer_name).select_from(Customer) \
    .where(customer_id.in_(select([customer_id, num]).select_from(
    select([customer_id, func.count(customer_id).label("num")]).select_from(Ordering).
        where(agronomist_id == "A", order_date.between("F", "T")).group_by(customer_id)).where(num > "N")))

s2 = select(product_name).select_from(Product).where(
    product_id.in_(select(distinct(product_id)).select_from(Ordering).where(
        customer_id == "C", order_date.between("F", "T"))))

s3 = select(agronomist_name).select_from(Agronomist).where(
    agronomist_id.in_(select([agronomist_id, num]).select_from(
        select([agronomist_id, func.count(agronomist_id).label("num")]).select_from(
            Degustation.join(Degustation_Customer)).
            where(customer_id == "C", degustation_date.between("F", "T")).group_by(agronomist_id)).
                      where(num > "N")))

s4 = select(agronomist_name).select_from(Agronomist).where(agronomist_id.in_(
    select(distinct(agronomist_id)).select_from(Trip_Agronomist).where(agronomist_id != "A", trip_id.in_(
        select().select_from(Trip).where(trip_date.between("F", "T"), trip_id.in_(
            select().select_from(Trip_Agronomist).where(agronomist_id == "A")
        ))))))

s5 = select(agronomist_name).select_from(Agronomist).where(
    agronomist_id.in_(select().select_from(Ordering).where(customer_id == "C", order_date.between("F", "T"))),
    agronomist_id.in_(select().select_from(Degustation).where(
        degustation_id.in_(select().select_from(Degustation_Customer).where(customer_id == "C")),
        degustation_date.between("F", "T"))
    ))

s6 = select(customer_name).select_from(Customer).where(customer_id.in_(
    select().select_from(
        select([customer_id, func.count(distinct(product_id)).label("num")]).select_from(Ordering).where(
            order_date.between("F", "T")).group_by(customer_id)).where(num > "N")
))

s7 = select(agronomist_name).select_from(Agronomist).where(agronomist_id.in_(
    select().select_from(
        select([agronomist_id, func.count(product_id).label("num")]).select_from(Harvest).where(
            harvest_date.between("F", "T"))).where(num > "N")
))

s8 = select(distinct(degustation_id)).select_from(Degustation.join(Degustation_Customer)).where(
    Degustation_Customer.customer_id == "C", Degustation.agronomist_id == "A")
