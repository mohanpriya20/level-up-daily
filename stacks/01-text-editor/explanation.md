# Text Editor — explanation

## Idea

A small text editor that supports **undo** and **redo** using two stacks. Whatever you type is the “current” text; undo goes back to the previous state, redo brings forward a state you undid.

## Data we keep

- **`self.text`** — The current text (what you see).
- **`self.undo`** — A stack of previous texts. Before each change we push the current text here so we can restore it on undo.
- **`self.redo`** — A stack of “future” texts. When we undo, we push the current text here so we can bring it back on redo.

## How each part works

**`write_text(text)`**  
Before changing anything, we push the current `self.text` onto `self.undo`. Then we append the new `text` to `self.text`. We clear `self.redo` because any old redo history is no longer valid after a new edit.

**`undo_action()`**  
If there’s something on `self.undo`, we push the current text onto `self.redo` (so we can redo later), then we replace `self.text` with whatever we pop from `self.undo`. If the undo stack is empty, we just say there’s nothing to undo.

**`redo_action()`**  
If there’s something on `self.redo`, we push the current text onto `self.undo`, then we replace `self.text` with whatever we pop from `self.redo`. If the redo stack is empty, we say there’s nothing to redo.

**`show_text()`**  
Prints the current text so you can see the state after each operation.

## Why stacks?

Undo needs “last in, first out”: we always go back to the most recent state, which is exactly what a stack gives. Redo is the same in the other direction. So two stacks (undo and redo) are a natural fit for this behavior.
