from dataclasses import dataclass
from enum import Enum
from typing import Union


class Op(Enum):
    Plus = 0
    Mult = 1
    Div = 3


def string2op(s: str) -> Op:
    match s:
        case "+":
            return Op.Plus
        case "*":
            return Op.Mult
        case "/":
            return Op.Div
        case _:
            assert False


expr = Union[int, "Expr"]


@dataclass
class Expr:
    operator: Op
    left: expr
    right: expr


def step_binop(e: Expr) -> int:
    assert isinstance(e.left, int) and isinstance(e.right, int)
    match e.operator:
        case Op.Plus:
            return e.left + e.right
        case Op.Mult:
            return e.left * e.right
        case Op.Div:
            return int(e.left / e.right)


def step(e: Expr) -> expr:
    if isinstance(e.left, int) and isinstance(e.right, int):
        return step_binop(e)

    if isinstance(e.left, int):
        assert isinstance(e.right, Expr)
        return Expr(operator=e.operator, left=e.left, right=step(e.right))

    assert isinstance(e.left, Expr)
    return Expr(operator=e.operator, left=step(e.left), right=e.right)


def compute(e: expr, plus: bool) -> int:
    if isinstance(e, int):
        return e

    if e.operator == Op.Plus and plus:
        return


class Solution:
    def calculate(self, s: str) -> int:
        s = "".join([x for x in s if x != " "])

        def build(i: int, prev: str) -> Expr | int:
            if i >= len(s):
                return int(prev)

            if s[i] in {"+", "*", "/"}:
                return Expr(
                    operator=string2op(s[i]), left=int(prev), right=build(i + 1, "")
                )

            if s[i] == "-":
                return Expr(operator=Op.Plus, left=int(prev), right=build(i + 1, "-"))

            return build(i + 1, prev + s[i])

        res = build(0, "")
        return res if isinstance(res, int) else fold(res)
