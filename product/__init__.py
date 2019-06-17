from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://product-importer:sd5ym5jrnumpa2ot@fulfil-product-importer-sujitkumar141994-d48a.aivencloud.com:24369/products?sslmode=require'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from product.schema import Product
from product import routes

db.create_all()
db.session.commit()
