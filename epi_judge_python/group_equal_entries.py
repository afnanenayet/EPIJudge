import collections
import functools
from typing import List, Dict

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Person = collections.namedtuple("Person", ("age", "name"))


def group_by_age(people: List[Person]) -> None:
    # Keep track of the counts for each key, which is the desired length for each array
    key_counts = collections.Counter([person.age for person in people])
    array_offsets: Dict[int, int] = {x: 0 for x in key_counts.keys()}

    running_count = 0

    # The offsets for each array inside the larger array. This marks the start
    # index of each subarray within the larger array.
    for key in key_counts.keys():
        array_offsets[key] = running_count
        running_count += key_counts[key]

    # Swap one element at a time to its proper location
    while array_offsets:
        # Select from element from a subarray that hasn't been completed yet.
        # The element at `people[from_key]` hasn't been populated yet, so it we
        # need to put it in the proper subarray
        from_key = next(iter(array_offsets.keys()))
        from_idx = array_offsets[from_key]

        # Figure out where we need to swap this element to
        student_at_from_idx = people[from_idx]
        to_key = student_at_from_idx.age
        to_idx = array_offsets[to_key]

        # swap (from_idx, to_idx)
        people[from_idx], people[to_idx] = people[to_idx], people[from_idx]

        # Decrement the key count so we can figure out when a subarray has been
        # fully populated
        key_counts[to_key] -= 1

        # Delete the array offset from the candidate pool because that array
        # has been saturated. Otherwise increment the index so we can add to
        # the array later
        if key_counts[to_key] == 0:
            del array_offsets[to_key]
        else:
            array_offsets[to_key] += 1


@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure("Empty result")

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure("Entry set changed")

    ages = set()
    last_age = people[0].age

    for x in people:
        if x.age in ages:
            raise TestFailure("Entries are not grouped by age")
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "group_equal_entries.py",
            "group_equal_entries.tsv",
            group_by_age_wrapper,
        )
    )
