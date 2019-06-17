
import json


class SuccessResponse:

    """
        Success Response Class to handle all the Success of the Server
    """

    constants = {

        'PRODUCT_DATA': {'msg': 'product data', 'code': 200},
        'PRODUCT_DATA_DELETED': {'msg': 'product data deleted', 'code': 200},
        'UPLOAD_SUCCESSFULL': {'msg': 'file uploading successfull', 'code': 200},
        'PRODUCT_COUNT': {'msg': 'product count', 'code': 200}
    }

    @staticmethod
    def sendResponse(type, data):
        ''' 
            Send Response for an Request 

            Dict: type
            Dict: data
        
        '''
        response = {

            'success':True,
            'data': data,
            'code': type['code'],
            'msg': type['msg']
        }

        return json.dumps(response)
