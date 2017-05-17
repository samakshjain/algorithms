"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,
    return out


def print_intervals(intervals):
    res = []
    for i in intervals:
        res.append('[' + str(i.start) + ',' + str(i.end) + ']')
    print("".join(res))


# >>>>>>>

def merge_overlapping(intervals):
    final = [intervals[0]]
    for idx, interval in enumerate(intervals[1:]):
        if final[-1][1] > interval[0]:
            final[-1] = [final[-1][0], interval[1]]
        else:
            final.append(interval)
    return final


if __name__ == "__main__":
    given = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = []
    for l, r in given:
        intervals.append(Interval(l, r))
    print_intervals(intervals)
    print_intervals(merge(intervals))
    print merge_overlapping(given)
