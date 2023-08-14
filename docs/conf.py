import os
import sys

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
release = '0.1.40'
version = '0.1.40'

add_module_names = False
sys.path.insert(0, os.path.abspath(r'./src'))
# sys.path.insert(0, os.path.abspath('.'))
# sys.path.insert(0, os.path.abspath('../'))
print('Hello world!"')
print(sys.path)
autosummary_generate = True
autosummary_imported_members = False
exclude_patterns = []
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.autosummary']
html_theme = 'bizstyle'
html_static_path = ['_static']
html_context = {
    'display_github': True,  # Integrate GitHub
    'github_user': 'hendrikdutoit',  # Username
    'github_repo': 'SQLAlchemyExample',  # Repo name
    'github_version': 'master',  # Version
    # "conf_py_path": "/source/",  # Path in the checkout to the docs root
}
language = 'en'
# master_doc = 'source/index'
templates_path = ['templates']
