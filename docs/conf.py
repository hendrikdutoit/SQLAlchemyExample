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
release = '0.1.27'
version = '0.1.27'


autosummary_generate = True
autosummary_imported_members = True
exclude_patterns = []
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx.ext.autosummary"]
html_theme = "bizstyle"
html_static_path = ['static']
html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "hendrikdutoit",  # Username
    "github_repo": "SQLAlchemyExample",  # Repo name
    "github_version": "master",  # Version
    # "conf_py_path": "/source/",  # Path in the checkout to the docs root
}
language = "en"
# master_doc = 'source/index'
templates_path = ['templates']
