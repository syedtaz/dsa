# Design a text editor with a cursor that can do the following:

# Add text to where the cursor is.
# Delete text from where the cursor is (simulating the backspace key).
# Move the cursor either left or right.
# When deleting text, only characters to the left of the cursor will be deleted.
# The cursor will also remain within the actual text and cannot be moved beyond it.
# More formally, we have that 0 <= cursor.position <= currentText.length always holds.

# Implement the TextEditor class:

# TextEditor() Initializes the object with empty text.
# void addText(string text) Appends text to where the cursor is.
# The cursor ends to the right of text.

# int deleteText(int k) Deletes k characters to the left of the cursor.
# Returns the number of characters actually deleted.

# string cursorLeft(int k) Moves the cursor to the left k times.
# Returns the last min(10, len) characters to the left of the cursor, where len
# is the number of characters to the left of the cursor.

# string cursorRight(int k) Moves the cursor to the right k times. Returns the
# last min(10, len) characters to the left of the cursor, where len is the number
# of characters to the left of the cursor.

from enum import Enum

class Left(Enum):
   t = 1

class Right(Enum):
   t = 1

class Node():
  val: str
  prev: 'Node | Left'
  next: 'Node | Right'

  def __init__(self, val : str, prev = None, next = None):
     self.val = val
     self.prev = prev
     self.next = next


def collect_aux(cur: Node | Right, end: Node | Right, acc: str) -> str:
   if cur == end:
      return acc

   assert cur is not Right.t
   return collect_aux(cur.next, end, acc + cur.val)

def collect(begin: Node, end: Node | Right) -> str:
  return collect_aux(begin, end, "")


class TextEditor:
  cursor : Node | None
  left : Node | None

  def is_empty(self) -> bool:
     return self.cursor is None and self.left is None

  def adjust_cursor(self) -> None:
     count = 0
     cur = self.cursor
     if cur is None:
        return

     if cur.prev is Left.t:
        return


     while cur.prev is not Sentinel.LEFT or count != 10:
      cur = cur.prev
      count += 1

  def __init__(self):
     self.cursor, self.left, self.right = None, None, None

  def addText(self, text: str) -> None:
    if self.is_empty():




  def deleteText(self, k: int) -> int:


  def cursorLeft(self, k: int) -> str:


  def cursorRight(self, k: int) -> str:
