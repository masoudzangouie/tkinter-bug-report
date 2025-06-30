# Tkinter Checkbox Bug Report

This repository documents a rare and tricky bug in Tkinter where a `Checkbutton` fails to reflect its `BooleanVar` state unless the variable is explicitly used in a callback.

## 📄 Contents

- [`tkinter-checkbox-bug.md`](tkinter-checkbox-bug.md): Full explanation of the bug and how it was discovered
- Real-world tested workaround
- Written by Masoud Zangouie, June 2025

## 💡 Why this matters

If you're using `BooleanVar` in a `Toplevel` window and your checkbox doesn't reflect its value, this post might save you hours of debugging.
