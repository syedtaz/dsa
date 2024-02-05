from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:

        def f(i: int, multi: bool, acc: list[str]) -> list[str]:
            if i >= len(source):
                return acc

            if multi:
                close_delim = source[i].find("*/")
                if close_delim == -1:
                    return f(i + 1, multi, acc)

                source[i] = source[i][close_delim + 2 :]
                return f(i, False, acc)

            single, open_delim = source[i].find("//"), source[i].find("/*")
            match (single == -1, open_delim == -1):
                case True, True:
                    return f(i + 1, multi, acc + [source[i]])
                case False, True:
                    return (
                        f(i + 1, multi, acc)
                        if single == 0
                        else f(i + 1, multi, acc + [source[i][:single]])
                    )
                case True, False:
                    return (
                        f(i + 1, True, acc)
                        if open_delim == 0
                        else f(i + 1, True, acc + [source[i][:open_delim]])
                    )
                case False, False:
                    if single <= open_delim:
                        return (
                            f(i + 1, multi, acc)
                            if single == 0
                            else f(i + 1, multi, acc + [source[i][:single]])
                        )
                    else:
                        return (
                            f(i + 1, True, acc)
                            if open_delim == 0
                            else f(i + 1, True, acc + [source[i][:open_delim]])
                        )
                case _:
                    assert False

        return f(0, False, [])


s = Solution()
print(s.removeComments(source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
