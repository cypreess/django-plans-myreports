#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='django-plans-myreports',
    version='0.1',
    description='Accountant reports from django-plans',
    author='Krzysztof Dorosz',
    author_email='cypreess@gmail.com',
    license='MIT',

    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ],
    include_package_data=True,
    zip_safe=False,
    package_data={
        'plans_reports': [
            'templates/plans_reports/*.html',
            ],
        }
    )
