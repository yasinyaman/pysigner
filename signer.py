from Crypto.Cipher import AES
import base64
import time
import ast


class Signer:
    """
    >>> sing = Signer("This is a key123","This is an IV456")

    >>> sing.signing("Hello World")
    b'eydtZXNzYWdlJzogJ0hlbGxvIFdvcmxkJywgJ3NpZ24nOiBiJ1x4ZjZceGFjUVx4ZTQ5XHhjMlx4MDNceDFjNVx4ZmVoXHgxYlx4MTBceGQyMVx4OTdceGMxX1x4YjdceGFheFx4ZGNceGU2XHhkMHhceGQ0XHhiYlx4MTBrXHhkYVx4ZmVceDg4XHhhNlx4OTk4XHhlZFx4OWRGd1x4YjdceGFhXHhhN0pmQDFQXHhlMlx4YzUpXHhlN1x4YzRceDgxSSd9'

    >>> sing.unsigning(b'eydtZXNzYWdlJzogJ0hlbGxvIFdvcmxkJywgJ3NpZ24nOiBiJ1x4ZjZceGFjUVx4ZTQ5XHhjMlx4MDNceDFjNVx4ZmVoXHgxYlx4MTBceGQyMVx4OTdceGMxX1x4YjdceGFheFx4ZGNceGU2XHhkMHhceGQ0XHhiYlx4MTBrXHhkYVx4ZmVceDg4XHhhNlx4OTk4XHhlZFx4OWRGd1x4YjdceGFhXHhhN0pmQDFQXHhlMlx4YzUpXHhlN1x4YzRceDgxSSd9'
)
    {'info': True, 'message': 'Hello World', 'signTime': 1395749693.3842516, 'sign': b'\xf6\xacQ\xe49\xc2\x03\x1c5\xfeh\x1b\x10\xd21\x97\xc1_\xb7\xaax\xdc\xe6\xd0x\xd4\xbb\x10k\xda\xfe\x88\xa6\x998\xed\x9dFw\xb7\xaa\xa7Jf@1P\xe2\xc5)\xe7\xc4\x81I'}
    """
    def __init__(self,key, iv):
        self.key = key
        self.iv = iv

    def signing(self, message):
        obj = AES.new(self.key, AES.MODE_CFB, self.iv)
        return base64.b64encode(str({"message": message, "sign": obj.encrypt(str({"message": message, "time": time.time()}))}).encode('utf-8'))

    def unsigning(self,signature):
        jsonData = ast.literal_eval(base64.b64decode(signature).decode('utf-8'))
        obj = AES.new(self.key, AES.MODE_CFB, self.iv)
        sign = ast.literal_eval(obj.decrypt(jsonData['sign']).decode('utf-8'))
        if jsonData['message'] == sign['message']:
            return {"info":True, "sign":jsonData['sign'], "message":jsonData['message'], "sign":jsonData['sign'], "signTime":sign['time']}
        else:
            return {"info":False, "sign":jsonData['sign'], "signTime":sign['time']}