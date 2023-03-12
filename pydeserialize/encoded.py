from urllib.parse import quote
from base64 import b64encode
import binascii

class Encode():
    
    @staticmethod
    def shell(payload):
        print(payload)
    
    @staticmethod
    def urlencode(payload):
        print(quote(payload))
    
    @staticmethod
    def base64(payload):
        print(b64encode(payload))
    
    @staticmethod
    def hexadecimal(payload):
        print(binascii.hexlify(payload))