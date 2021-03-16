project = 'MathModeling'
copyright = '2021, starslayerx'
author = 'starslayerx'
release = '0.1'

extensions = [
    "nbsphinx",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
]

language = 'zh_CN'
templates_path = ['_templates']
exclude_patterns = []

smartquotes = False

html_theme = 'sphinx_rtd_theme'
html_theme_options = {'canonical_url': "https://self-contained.github.io/"}
html_static_path = ['_static']
