from enum import Enum
from typing import Optional
from dataclasses import dataclass

class Color(Enum):
  Black = 0
  Red = 1

@dataclass
class Tree[A]:
  color: Color
  elem: A
  left: Optional['Tree[A]']
  right: Optional['Tree[A]']