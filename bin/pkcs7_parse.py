#!/usr/bin/env python
import sys
from pyx509.pkcs7_models import PKCS7


def print_signature_info(derData):
    """
    Print certificates of signature
    """
    PKCS7.from_der(derData).display()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: pkcs7_parse.py pkcs7_enveloped.der")
        sys.exit(1)
    der_file = sys.argv[1]
    print_signature_info(open(der_file, 'rb').read())
