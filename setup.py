from setuptools import setup

setup(
    name='pyx509',
    version='0.1.0',
    url='http://github.com/tracer0tong/pyx509',
    license='GNU GPLv2',
    author='Copyright (C) 2009-2010  CZ.NIC, z.s.p.o. (http://www.nic.cz), erny, tracer0tong',
    author_email='erevilla@tangrambpm.es, tracer.tong@yandex.ru',
    packages=['pyx509','pyx509.pkcs7','pyx509.pkcs7.asn1_models'],
    scripts=['bin/pkcs7_parse.py', 'bin/x509_parse.py'],
    description='Py3k x509 protocol files parser'
)
