#!/usr/bin/env python3
'''lets duck type an iterable object
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''sequence length
    '''
    return [(i, len(i)) for i in lst]
