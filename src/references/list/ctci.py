from list import a, L, List

# 2.1 Remove duplicates


# With O(n) space for hashtable
def remdup(lst: L[a]) -> L[a]:
    def aux(lst: L[a], s: set[a], acc: L[a]) -> L[a]:
        if lst is None:
            return acc

        if lst.value not in s:
            return aux(
                lst.next, s.union([lst.value]), List[a](value=lst.value, next=acc)
            )

        return aux(lst.next, s, acc)

    return aux(lst, set(), None)


print(remdup(List(1, List(1, List(1, List(1, None))))))

# With O(1) space but O(nlogn) time with sorting
# TODO!


# 2.2 Kth to last
def ktolast(lst: L[a], k: int) -> a:
    def take(lst: L[a], n: int) -> L[a]:
        if n == 0:
            return lst

        if lst is None:
            return None

        return take(lst.next, n - 1)

    bunny = take(lst=lst, n=k)
    hare = lst

    def iter2end(fast: L[a], slow: L[a]) -> a:
        if fast is None:
            raise Exception

        assert slow is not None
        if fast.next is None:
            return slow.value

        return iter2end(fast.next, slow.next)

    return iter2end(bunny, hare)


print(ktolast(List(1, List(2, List(3, None))), k=0))
