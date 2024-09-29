dtype = dict[str, "str | dtype"]


def prefix(pref: str, key: str) -> str:
    if key == "" and pref == "":
        return ""

    if key != "" and pref == "":
        return key

    return pref + "." + key if key != "" else pref


def flatten_dictionary(dictionary: dtype) -> dict[str, str]:
    acc: dict[str, str] = {}
    stack: list[tuple[str, dtype]] = [("", dictionary)]

    while len(stack) > 0:
        pref, node = stack.pop()

        for key, value in node.items():
            if type(value) == dict:
                stack.append((prefix(pref, key), value))
            else:
                assert type(value) == str
                acc[prefix(pref, key)] = value

    return acc
