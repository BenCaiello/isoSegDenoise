# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'isosegdenoise'
copyright = '2024-2025, Medical University of South Carolina'
author = 'Ben Caiello'
release = '0.2.4'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_rtd_theme',
'sphinx.ext.napoleon',
'autoapi.extension',
'nbsphinx'
]
autoapi_dirs = ['../../isosegdenoise']

autoapi_ignore = ['*migrations*',  ## default of autoapi_ignore
                '*entry*',
                '*GUI*',
                '*vendors*',
                '*shared*']


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
