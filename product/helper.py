import csv
from product.model import Product as ProductModel
import uuid
import asyncio
import random


class Product:

    async def addProduct(self, **kwargs):
        """
            Async function to add product in the database

            parameters:
            **kwargs - names arguments
            name, sku, description

            returns:
            confirmation of adding
        """
        name = kwargs['name']
        sku = kwargs['sku']
        id = str(uuid.uuid4())
        description = kwargs['description']
        active = kwargs['active']
        if kwargs['active'] == None:
            active = random.choice([True, False])

        product = ProductModel()
        productData = product.getProductBySku(sku)
        if productData == None:
            return product.insertProduct(
                id=id, description=description, sku=sku, name=name, active=active)
        else:
            return product.updateProduct(sku, name=name, description=description)

    def uploadFile(self, filepath):
        """
            Upload file in the event loop 

            parameters:
            string: filepath - absolute path of a file

            returns:
            void
        """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        with open(filepath, 'rt') as f:
            data = csv.reader(f)
            next(data, None)
            rows = []
            for row in data:
                name = row[0]
                sku = row[1]
                description = row[2]
                # append the async in rows to run in event loop
                rows.append(asyncio.ensure_future(self.addProduct(
                    name=name, sku=sku, description=description)))

            # run until completed
            loop.run_forever()
