def success_response(message="success", data=None):
    return{
        "success": True,
        "message": message,
        "data": data
    }

def error_response(message="error", data= None):
    return{
        "success": False,
        "message": message,
        "data": data
    }