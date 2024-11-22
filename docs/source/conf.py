# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

sys.path.insert(0, os.path.abspath('../../src'))  # repertoire du code source
sys.path.insert(0, os.path.abspath('.'))  # ajout du repertoire courant

from dependency import load_django  # noqa: E402


# Initialiser Django si nécessaire (pour sphinx autodoc
# qui va voir les heritages de modele par ex.).
# Desactivé pour readthedoc (variable d'env : SKIP_DJANGO==1)
load_django()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Orange County Lettings'
copyright = '2024, Mothraa'
author = 'Mothraa'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
              "sphinx.ext.viewcode",  # permet de faire le lien avec le code source
              "sphinx.ext.autodoc",  # génération auto de la doc
              # "sphinx.ext.napoleon",  # pour le format docstrings google
              "sphinx_rtd_theme",  # theme "readthedoc"
]

templates_path = ['_templates']
exclude_patterns = ['manage.rst',
                    '**/manage.py',
                    '**/migrations/**',
                    '**/tests/**'
                    ]

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

autodoc_default_options = {
    'members': True,
    'undoc-members': False,
    'inherited-members': False,
}
