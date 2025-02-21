from setuptools import setup, find_packages

setup(
    name='ia_prompt',       # Nom du module
    version='0.1',           # Version
    packages=find_packages(), # Recherche automatique des packages
    install_requires=[       # Dépendances (optionnel)
        'numpy', 
        'torch', 
        'trimesh'
    ],
    description='Module pour le déploiement de l’IA de modélisation 3D',
    author='noalau',
    license='MIT'
)
