from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

     Approach:
    - Convert the second sequence to a set for faster membership checks.
    - Use a set to track items already added and avoid duplicates.
    - Preserve the order of items as they appear in the first sequence.

    Time Complexity: O(n + m) on average, because set lookups take O(1)
    on average and we iterate through both sequences.

    Space Complexity: O(n + m) as an upper bound for the sets and output.
    More precisely, O(m + k), where k is the number of unique common items.

    Optimal Time Complexity: O(n + m) on average, assuming hashable items
    and constant-time set operations on average.
    """
    second_items = set(second_sequence)
    common_items: List[ItemType] = []
    seen_items = set()

    for item in first_sequence:
        if item in second_items and item not in seen_items:
            common_items.append(item)
            seen_items.add(item)

    return common_items
