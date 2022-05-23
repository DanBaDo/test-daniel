ENDPOINTS = {
    'INSPECTORS': "https://6244305b3da3ac772b0c7854.mockapi.io/fakeSolar/3rdParty/inspectors",
    'INSPECTIONS': "https://6244305b3da3ac772b0c7854.mockapi.io/fakeSolar/3rdParty/inspections"
}

SG_IDS  = ["SolarGrade"]

RESP_STATUS = {
    'OK': 'Ok',
    'ERROR': 'Error'
}

class Response:
    def __init__(self, status, data, error=False):
        self.status = status
        self.data = data
        if error: self.error = error