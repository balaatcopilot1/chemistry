# Class 12 Chemistry Practice

Pick a section (One / Two / Three / Four / Five Marks), or pick a chapter and then a section, and practise 10 random questions at a time.

## Adding questions
Put one `.md` file per question in the matching folder under `Questions/`:

    Questions/One Marks/    Questions/Two Marks/
    Questions/Three Marks/  Questions/Four Marks/
    Questions/Five Marks/

Add `Chapter:` and `Paper:` lines at the top (if `Paper:` is missing, the paper name is taken from the file name, e.g. `Mar2024-Q05.md` gives Mar2024). Students tick chapters before practising; questions with the same chapter name (spelling and case ignored) are grouped together. A file with no `Chapter:` line goes under "Other". The `## Answer` line splits question and answer:

    Chapter: Metals and Non-metals
    Paper: Mar2024

    Which gas is released when zinc reacts with dilute HCl?

    - A) O₂
    - B) H₂
    - C) Cl₂
    - D) CO₂

    ## Answer

    **B)** Zn + 2HCl → ZnCl₂ + H₂

Chemical notation: use Unicode (H₂SO₄, Fe³⁺, →, ⇌, ⁻, ↑, ↓) or HTML (`H<sub>2</sub>O`, `Fe<sup>3+</sup>`). Do not use LaTeX.
Commit and push: the site rebuilds its question index automatically from every `.md` file.
