# Check setuptools, nếu k có dùng distutils có sẵn

from setuptools import setup, Command
setuptools_available = True

try:
    # This will create an exe that needs Microsoft Visual C++ 2008
    # Redistributable Package
    import py2exe
except:
    pass