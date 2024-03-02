# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Truly Understanding the Teachings of the Buddha'
copyright = '2016 Anthony Markwell, 2019 revised edition'
author = 'Anthony Markwell'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'linuxdoc.rstFlatTable',
]
#extlinks={'audio':('https://woodem.eu/~eudoxos/mttc-audio/%s','%s')}
#rst_prolog='''
#.. role:: pdfpage
#'''
myst_enable_extensions=['attrs_inline','linkify']


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = <'pydata_sphinx_theme'
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_css_files=[
    'custom.css'
]
html_js_files=[
    # 'audio0.js'
]

html_theme_options = dict(
  show_nav_level=4,
  navigation_depth=4,
  # these unfortunatley don't work as we need
  # unless the sections are in separate files
  # see https://github.com/executablebooks/sphinx-book-theme/issues/735
  show_navbar_depth=10, # zero makes the expand arrow show
  max_navbar_depth=10,
#  'html_title':'MTTC',
  navigation_with_keys=False,
  # home_page_in_toc=True,
  # collapse_navbar=False,
  use_download_button=False,
  footer_content_items=['copyright.html','extra-footer.html'],
)

show_navbar_depth=4
max_navbar_depth=5
show_nav_level=4
navigation_depth=4

sidebar_collapse=True
html_show_sphinx=False
fixed_sidebar=True
collapse_navbar=True
navigation_with_keys=False
html_title='Truly Understanding …'


latex_engine='lualatex'
latex_documents=[('index','markwell-truly-understanding.tex',project,author,'manual')]
latex_elements=dict(
    preamble=r'''
        \newcommand{\DUrolepdfpage}[1]{\marginpar{\textcolor{gray}{\scriptsize [#1]}}}
    ''',
    fontpkg=r'\usepackage{termes-otf}\usepackage{heros-otf}'
)
latex_additional_files=['termes-otf.sty','heros-otf.sty']


epub_title = project
epub_author = author
epub_publisher = ''
epub_copyright = copyright
epub_cover = ('cover.png','epub-cover.html')
epub_language='en'
epub_basename='markwell-truly-understanding'
epub_use_index=False
epub_scheme='ISBN'
epub_identifier = ''
# A unique identification for the text.
epub_uid = 'markwell-truly-understanding'

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

