import markdown

md = markdown.Markdown(extensions=[
    "markdown.extensions.extra",
    "markdown.extensions.admonition",
    "markdown.extensions.headerid",
    "markdown.extensions.codehilite",
    "markdown.extensions.sane_lists",
    "markdown.extensions.toc",
    "markdown.extensions.nl2br",
    "markdown.extensions.wikilinks",
    # "markdown.extensions.fenced_code",

    "pymdownx.magiclink",
    "pymdownx.betterem",
    "pymdownx.tilde",
    "pymdownx.emoji",
    "pymdownx.tasklist",
    "pymdownx.superfences",
], )
