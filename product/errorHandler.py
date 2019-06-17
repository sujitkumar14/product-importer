
import json

class ErrorResponse:

     """
        Error Response Class to handle all the Success of the Server
    """


    constants = {

        'NO_FILE_FOUND': {'msg': 'No file found', 'code': 200},
        'PRODUCT_NOT_EXIST': {'msg': 'product not exist', 'code': 200},
        'UPLOAD_SUCCESSFULL': {'msg': 'file uploading successfull', 'code': 200}
    }

    def sendResponse(self, type):

        """
            Send Response for an Request 

            Parameter:
            Dict: type
        
        """
        response = {

            'success': False,
            'code': self.constants[type].code
            'msg': self.constants[type].msg
        }

        return json.dumps(response)