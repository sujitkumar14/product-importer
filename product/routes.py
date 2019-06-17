from product import app
from product.controller import Product
from flask import request, jsonify


@app.route("/")
def welcome():
    return "welcome to the product importer"

@app.route("/product/upload",methods=["POST"])
def uploadProduct():
    f = request.files['file']
    return Product.uploadFile(f)

@app.route("/product/<pid>", methods=['GET'])
def getProduct(pid):
    return Product.getProduct(pid)

@app.route("/product/count",methods=["GET"])
def getProductCount():
    return Product.getProductCount()

@app.route("/product/<pid>",methods=['DELETE'])
def deleteProduct(pid):
    return Product.deleteProduct(pid)

@app.route("/product",methods=['DELETE'])
def deleteAllProduct():
    return Product.deleteAllProduct()

@app.route("/product",methods=['GET'])
def getAllProducts():
    return Product.getAllProducts()