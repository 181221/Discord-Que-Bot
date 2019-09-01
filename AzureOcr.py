from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import TextOperationStatusCodes
import re
import time
import os


class OCR:
    env_vars = {}

    def __init__(self, env_file_path="./.env"):
        self.endpoint = ""
        self.key = ""
        self.position_in_que = ""
        self.estimated_que_time = ""
        self.env_file_path = env_file_path
        self.client = None
        self._set_environment_variables()

    def _set_environment_variables(self):
        if os.path.exists(self.env_file_path):
            with open(self.env_file_path) as f:
                for line in f:
                    key, value = line.split('=')
                    self.env_vars[key] = value
        if self.env_vars['ENDPOINT'] in self.env_vars.values():
            self.endpoint = self.env_vars['ENDPOINT'].strip()

        if self.env_vars['AZURE_COGNITIVE_SERVICE_KEY'] in self.env_vars.values():
            self.key = self.env_vars['AZURE_COGNITIVE_SERVICE_KEY'].strip()

    def get_endpoint(self):
        if self.endpoint is "":
            raise Exception("No endpoint or key found in .env")
        else:
            return self.endpoint

    def get_key(self):
        if self.key is "":
            raise Exception("No endpoint or key found in .env")
        else:
            return self.key

    def get_position_in_que(self):
        return self.position_in_que

    def get_estimated_que_time(self):
        return self.estimated_que_time

    def recognize_text(self, filename):
        self._connect()
        raw = True
        custom_headers = None
        numberOfCharsInOperationId = 36
        image_data = open(filename, "rb")
        rawHttpResponse = self.client.recognize_text_in_stream(image_data, "printed", custom_headers, raw)
        operationLocation = rawHttpResponse.headers["Operation-Location"]
        idLocation = len(operationLocation) - numberOfCharsInOperationId
        operationId = operationLocation[idLocation:]

        while True:
            result = self.client.get_read_operation_result(operationId, {"Content-Type": "application/json"})
            if result.status not in ['NotStarted', 'Running']:
                break
            time.sleep(1)
        if result.status == TextOperationStatusCodes.succeeded:
            rec_result = result.additional_properties['recognitionResult']
            for textResult in rec_result:
                for line in rec_result['lines']:
                    text = line['text']
                    x = re.findall("position in queue:", text, re.IGNORECASE)
                    y = re.findall("estimated time:", text, re.IGNORECASE)
                    if x:
                        self.position_in_que = text
                    if y:
                        self.estimated_que_time = text

    def _connect(self):
        credentials = CognitiveServicesCredentials(self.get_key())
        self.client = ComputerVisionClient(self.get_endpoint(), credentials)