#!/usr/bin/env python3
"""safe_first_element."""


from typing import Sequence, Any, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Description.

    -----------
    Duck typing -first element of a sequence.
    """
    if lst:
        return lst[0]
    else:
        return None
