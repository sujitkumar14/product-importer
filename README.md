<b>product import is a platform to upload a product csv file in a database</b>

- <b>Requirements</b>

    This project requires python >=3.7.0 and npm >=19.0.0

- <b>Getting Started</b>

    To get started, clone the repo and install the dependencies and start the server.

    ```js
    pip3 install -r requirement.txt
    python3 run.py
    ```

<b> API Documentation </b>

- <b> API URL</b>
    ```js
        http://localhost:5000
    ```


- <b>Success Response</b>

    ```js
        'success': true,
        'message': "",
        'data': {}, 
        'code': 200
    ```

- <b>Error Response</b>

    ```js
        'success': false,
        'message': "",
        'code': 200 || 500
    ```


<b>Endpoints</b>

- <b>Welcome</b>

    Welcome message in response

    <b>Route:</b> / <br>
    <b>Method:</b> GET

- <b>Upload Product</b>

    Upload a csv file on product importer

    <b>Route:</b> /product/upload <br>
    <b>Method:</b> POST

    <b>form-data</b>
    1. file

    <b>headers</b>
    1. Content-Type == application/x-www-form-urlencoded 


- <b>product details</b>
    
    product details of the give pid else displays all the products on the platform

    <b>Route:</b> /product/<pid> <br>
    <b>Method:</b> GET

    
    <b> Response </b>
    ```js
        "data": {
            "id":id,
            "name":name,
            "sku":sku,
            "description": description
            "active": true| false
        }
    ```

- <b>Delete product</b>
    
    Delete a product or all product

    <b>Route:</b> /product/<pid> <br>
    <b>Method:</b> DElETE

    <b>Response</b>
    Success Response on successfull deletion of product

- <b>product count</b>
    
    total number of products in the database

    <b>Route:</b> /product/count<pid> <br>
    <b>Method:</b> GET

    
    <b> Response </b>
    ```js
        "data": count
    ```


