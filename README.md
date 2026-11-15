# tsveto.com

Tsvetomir Batinov's portfolio, styled as an exhibition catalogue: each project is a "work" with a plate and a museum-style label.

Static HTML, CSS and a little JavaScript. No framework and no build step; deploy the folder as is (Vercel config in `vercel.json`).

```sh
python3 -m http.server 4000   # then open http://localhost:4000
```

## Layout

- `index.html`: the whole catalogue
- `assets/styles.css`, `assets/main.js`
- `assets/fonts/`: Cormorant and Golos Text, self-hosted (SIL OFL, licences alongside)
- `assets/img/`: plates. Screenshots were taken from the products running locally with demo data.
- `src/gen_diagrams.py`: generates the three schematic drawings that are inlined in `index.html`
- `src/og.html`: the social card, rendered to `assets/img/og.png`
- `PRODUCT.md`, `DESIGN.md`: product and design notes

## Editing a work

Each work is an `<article class="work">` with plates, a `.label` (Medium, Dimensions, Role) and wall text. Keep the "Dimensions" numbers measured, not estimated.
