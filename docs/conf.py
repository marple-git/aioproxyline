project = 'aioproxyline'
copyright = '2022, Marple'
author = 'Marple'
release = '1.0'


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autodoc.typehints',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


html_theme = 'furo'
html_logo = '_static/logo.jpg'
html_static_path = ['_static']

source_suffix = '.rst'
master_doc = 'index'

rst_prolog = """
.. role:: pycode(code)
   :language: python3
"""

latex_documents = [
    (master_doc, f'{project}.tex', f'{project} Documentation', author, 'manual'),
]

man_pages = [(master_doc, project, f'{project} Documentation', [author], 1)]

texinfo_documents = [
    (
        master_doc,
        project,
        f'{project} Documentation',
        author,
        project,
        'Modern and fully asynchronous framework for proxyline.net API',
        'Miscellaneous',
    ),
]