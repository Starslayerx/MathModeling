from recommonmark.parser import CommonMarkParser

master_doc = 'index'
project = 'MathModeling'
copyright = '2021, starslayerx'
author = 'starslayerx'
release = '0.1'

source_suffix = ['.rst', '.md']

extensions = [
    "sphinx.ext.mathjax",
    "recommonmark",
    "sphinx_markdown_tables",
]


language = 'zh_CN'
templates_path = ['_templates']
exclude_patterns = []

smartquotes = False

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'canonical_url': 'https://self-contained.github.io/',
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'collapse_navigation': False,
    'sticky_navigation': False,
    'navigation_depth': 3,
    'includehidden': True,
    'titles_only': False
    }
html_title = 'MathModeling'
html_static_path = ['_static']
