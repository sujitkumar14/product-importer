
from product.model import Product as ProductModel
import json
import csv
from product.helper import Product as ProductHelper
from os.path import realpath
from werkzeug import secure_filename
from threading import Thread
from product.errorHandler import ErrorResponse
from product.successHandler import SuccessResponse


class Product:

    @staticmethod
    def uploadFile(f):
        """
            function saves the data of in the database

            parameters:
            string:filename - name of the file

            returns:
            string:success response
        """
        if not f:
            return ErrorResponse.sendResponse(ErrorResponse.constants['NO_FILE_FOUND'])
        else:
            # saving and creating absolute path
            filepath = realpath(secure_filename(f.filename))
            f.save(filepath)
            productHelper = ProductHelper()
            # start a seperate thread for upload the file
            Thread(target=productHelper.uploadFile,
                   args=(str(filepath),)).start()
            return SuccessResponse.sendResponse(SuccessResponse.constants['UPLOAD_SUCCESSFULL'], {})

    @staticmethod
    def getProduct(id):
        """
             Returns the product details for an id

             parameters:
             string:id - id of the product

             returns:
             string:success response
         """
        product = ProductModel()
        productData = product.getProduct(id)
        if productData != None:
            return SuccessResponse.sendResponse(SuccessResponse.constants['PRODUCT_DATA'], {"id": productData.id, "name": productData.name, "sku": productData.sku, "description": productData.description})
        else:
            return ErrorResponse.sendResponse(ErrorResponse.constants['PRODUCT_NOT_EXIST'])

    @staticmethod
    def deleteProduct(id):
        """
            Delete the product for an id

            parameters:
            string:id - id of the product

            returns:
            string:success response
        """
        product = ProductModel()
        product.deleteProduct(id)
        return SuccessResponse.sendResponse(SuccessResponse.constants['PRODUCT_DATA_DELETED'], {})

    @staticmethod
    def deleteAllProduct():
        ''' Delete all the product. '''
        product = ProductModel()
        product.deleteAllProducts()
        return SuccessResponse.sendResponse(SuccessResponse.constants['PRODUCT_DATA_DELETED'], {})

    @staticmethod
    def getAllProducts():
        ''' Returns all the product. '''
        product = ProductModel()
        productData = product.getAllProducts()
        products = []
        if productData != None:
            for p in productData:
                productTemp = {}
                productTemp["id"] = p.id
                productTemp["name"] = p.name
                productTemp["sku"] = p.sku
                productTemp["description"] = p.description
                products.append(productTemp)
        return SuccessResponse.sendResponse(SuccessResponse.constants['PRODUCT_DATA'], products)

    @staticmethod
    def getProductCount():
        ''' Returns the Number of Product in database. '''
        product = ProductModel()
        count = product.productCount()
        return SuccessResponse.sendResponse(SuccessResponse.constants['PRODUCT_DATA'], count)
