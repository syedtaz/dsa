import asyncio
from typing import Callable


class Foo:
    ref_fst: asyncio.Event
    ref_sec: asyncio.Event
    ref_thd: asyncio.Event

    def __init__(self) -> None:
        self.ref_fst = asyncio.Event()
        self.ref_snd = asyncio.Event()
        self.ref_thd = asyncio.Event()

    async def first(self, printFirst: "Callable[[], None]") -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        asyncio.run(self.ref_thd.wait())
        self.ref_fst.set()

    async def second(self, printSecond: "Callable[[], None]") -> None:
        await self.ref_fst.wait()

        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

        self.ref_sec.set()

    async def third(self, printThird: "Callable[[], None]") -> None:
        await self.ref_sec.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.ref_thd.set()
