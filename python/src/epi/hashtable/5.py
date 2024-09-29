def eq_metric(words: list[str]) -> int | None:
    pairs: dict[str, tuple[int, int | None]] = {}

    for idx, word in enumerate(words):
        if word not in pairs:
            pairs[word] = (idx, None)
            continue

        l, r = pairs[word]
        if r is None:
            pairs[word] = (l, idx)
            continue

        if r - l > idx - r:
            pairs[word] = (r, idx)

    filtered = [b - a for a, b in pairs.values() if b is not None]
    return min(filtered) if len(filtered) > 0 else None
