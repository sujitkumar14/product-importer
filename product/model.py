from product.schema import Product as ProductSchema
from product import db
import json

class Product:

    """
        Class Product to interact with database
    """

    def insertProduct(self, **kwargs):
        ''' Insert a new product in database '''
        product = ProductSchema(kwargs['id'], kwargs['name'],
                                kwargs['sku'], kwargs['description'],kwargs['active'])
        db.session.add(product)
        db.session.commit()
        return product

    def getProduct(self, id):
        ''' Returns the product details for an Id. '''
        productData = ProductSchema.query.filter_by(id=id).first()
        return productData

    def deleteProduct(self,id):
        ''' Delete the product for an Id. '''
        ProductSchema.query.filter_by(id=id).delete()
        db.session.commit()
    
    def deleteAllProducts(self):
        ''' Delete all the products. '''
        ProductSchema.query.filter_by().delete()
        db.session.commit()

    def getAllProducts(self):
        ''' Returns all the product. '''
        productData = ProductSchema.query.filter_by()
        return productData

    def getProductByActive(self,active):
        ''' Returns the Product Details for a active.'''
        productData = ProductSchema.query.filter_by(active=active)
        return productData
    
    def getProductByName(self,name):
        ''' Returns the Product Details for a name. '''
        productData = ProductSchema.query.filter_by(name=name)
        return productData

    def getProductBySku(self,sku):
        ''' Returns the product Details for an SKU. '''
        productData = ProductSchema.query.filter_by(sku=sku).first()
        return productData
    
    def updateProduct(self,sku,**kwargs):
        ''' Update the product Details for an SKU. '''
        productData = ProductSchema.query.filter_by(sku=sku).first()
        productData.name = kwargs['name']
        productData.description = kwargs['description']
        db.session.commit()
        return productData
    
    def productCount(self):
        ''' Returns the Total Number of products. '''
        count = ProductSchema.query.filter_by().count()
        return str(count)