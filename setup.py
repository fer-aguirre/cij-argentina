from setuptools import setup, find_packages

setup(
    name='Datos del Centro de Información Judicial (CIJ) de Argentina',
    version='0.1.0',
    author='Fer Aguirre',
    description='Repositorio para convertir archivos PDF del CIJ de Argentina en datos estructurados para hacerlos públicos y descargables por medio de Datasette',
    python_requires='>=3',
    license='MIT License',
    packages=find_packages(),
)