#!/usr/bin/env python3
"""element_length."""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Description.

    -----------
    function to add annotations.
    """
    return [(i, len(i)) for i in lst]
