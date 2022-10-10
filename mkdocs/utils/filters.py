from __future__ import annotations

try:
    from jinja2 import pass_context as contextfilter  # type: ignore
except ImportError:
    from jinja2 import contextfilter  # type: ignore

from mkdocs.utils import normalize_url


@contextfilter
def url_filter(context, value: str) -> str:
    """A Template filter to normalize URLs."""
    return normalize_url(
        value, page=context['page'], base=context['base_url'], files=context['_files']
    )
