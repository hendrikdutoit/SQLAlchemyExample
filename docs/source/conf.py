import os
import sys
from pprint import pprint

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
#
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
#
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

project = 'SQLAlchemyExample'
copyright = '2023, Hendrik du Toit'
author = 'Hendrik du Toit'
release = '0.1'
version = '0.1.40'

# add_module_names = False
sys.path.insert(0, os.path.abspath(r'../../src'))
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../..'))
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']
templates_path = ['_templates']
html_theme = 'bizstyle'
epub_show_urls = 'footnote'

# autosummary_generate = True
# autosummary_imported_members = False
# exclude_patterns = []
# extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.autosummary']
# html_static_path = ['_static']
# html_context = {
#     'display_github': True,  # Integrate GitHub
#     'github_user': 'hendrikdutoit',  # Username
#     'github_repo': 'SQLAlchemyExample',  # Repo name
#     'github_version': 'master',  # Version
#     # "conf_py_path": "/source/",  # Path in the checkout to the docs root
# }
# language = 'en'
# master_doc = 'source/index'

pprint(sys.path)
