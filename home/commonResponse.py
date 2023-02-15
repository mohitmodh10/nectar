def generateCommonResponse(status:int,message:str,data):
    jsonData = {
        "status":status,
        "message": message,
        "data":data
    }
    return jsonData
