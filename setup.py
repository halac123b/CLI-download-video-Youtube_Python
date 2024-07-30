# Check setuptools, nếu k có dùng distutils có sẵn
try:
    from setuptools import setup, Command

    setuptools_available = True
except ImportError:
    from distutils.core import setup, Command

    setuptools_available = False
