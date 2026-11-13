"""Keep hidden Vale controls from dividing one rendered list into several."""
import re

# The compiler emits separate list nodes around an intervening HTML comment.
# Join only matching plain list types separated exclusively by Vale controls.
# Keep ordinary comments, prose, headings and explicitly restarted lists intact.
_BOUNDARY = re.compile(
    r'</(?P<tag>ul|ol)>\s*'
    r'(?P<controls>(?:<!--\s*vale\s+[A-Za-z0-9_.-]+\s*=\s*(?:NO|YES)\s*-->\s*)+)'
    r'<(?P=tag)(?:\s+type="1")?>'
)


def join_lint_split_lists(markup: str) -> tuple[str, int]:
    return _BOUNDARY.subn(lambda m: '\n'+m.group('controls'), markup)
