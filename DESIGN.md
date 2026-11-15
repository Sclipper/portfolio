# Design

The site is an exhibition catalogue. The wall is warm paper; each project is a *work* hung as a plate (a real screenshot, a screen recording, or a schematic drawing) with a museum label beside it and wall text beneath.

## World

- **Cover**: the name set large in the display serif, "Works, 2017–2026" in italic, a short wall text, and the *List of works* (the catalogue checklist) as the first thing to read. Hovering a row hangs that work's plate beside the list (the one authored interaction).
- **Works**: plates take eight columns; the label sits in the remaining four and stays at eye level (sticky) while the plates scroll. Drawings hang full width with the label above.
- **Labels**: number in vermilion, title, gloss in italic for Bulgarian titles, date in italic, then a ruled table: Medium, Dimensions (always measured, never estimated), Role, Visit or Licence. Credit lines in italic ("Lent by…", "Not illustrated.").
- **Drawings**: inline SVG schematics on a drawing sheet (paper, inset ruled border, title block bottom right). Boxes are 1.25px ink; the part where language models work is the only accent fill.
- **Close**: the lights go down for *Write to me.* on ink, then the colophon.

## Tokens

| Token | Value | Use |
|---|---|---|
| `--wall` | `oklch(0.965 0.009 85)` | page |
| `--paper` | `oklch(0.985 0.006 90)` | plates, drawing sheets |
| `--ink` | `oklch(0.21 0.012 60)` | text, rules under headings, contact ground |
| `--ink-2` | `oklch(0.43 0.014 60)` | secondary text, italics |
| `--ink-3` | `oklch(0.51 0.012 65)` | label terms, row numbers (≥4.5:1 on wall) |
| `--rule` | `oklch(0.84 0.012 78)` | hairlines |
| `--accent` | `oklch(0.555 0.185 33)` | catalogue vermilion: numbers, focus, selection, the LLM boxes |
| `--accent-wash` | `oklch(0.93 0.035 45)` | accent fills in drawings |

Shadow `--hang`: three layers, offset down, soft, like a framed print on a wall.

## Type

- Display: **Cormorant** (variable, self-hosted, Latin and Cyrillic). Bulgarian titles carry `lang="bg"` so the Bulgarian Cyrillic forms render. Display tops out at 6rem.
- Text and labels: **Golos Text** (variable, self-hosted). Tabular lining numerals in labels and the list.
- Scale: `--step--1` to `--step-4` fluid clamps in `styles.css`.

## Rules

- One accent colour, used for meaning, not decoration.
- No cards, no eyebrows over headings, no gradient text, no grid backgrounds.
- Every number on a label must be measured from the repository or the CV.
- Client work shows architecture only, and says so on the label.
