from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(['QAAccount.pyx','QAOrder.pyx'],        # Cython code file with primes() function  # Python code file with primes_python_compiled() function
                          annotate=True),        # enables generation of the html annotation file
)