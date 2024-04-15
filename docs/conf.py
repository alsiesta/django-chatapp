# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django
# Adjust the Python path to include the Django project directory (one level up)
sys.path.insert(0, os.path.abspath('..'))

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_chatapp.settings'  

# Initialize Django
django.setup()

# extensions = [
#     'sphinx.ext.autodoc',
#     # 'sphinx.ext.napoleon',  # Optional, for Google/NumPy style docstrings
#     # 'sphinx.ext.viewcode'   # Optional, adds links to source code
# ]

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Django Chat App'
copyright = '2024, Alexander Schönfeld'
author = 'Alexander Schönfeld'
release = 'April'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions =  [ 'sphinx.ext.autodoc' ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']




# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
