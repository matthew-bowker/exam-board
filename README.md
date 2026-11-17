# The Exam Board

An assessment design game for medical educators. Players build an assessment for a brief, the model scores it on reliability, validity, educational impact, acceptability and cost (van der Vleuten's utility model), and an exam board gives its verdict.

## Files

| File | What it is |
| --- | --- |
| `index.html` | The whole game as one self-contained page. This is the file GitHub Pages serves. |
| `src/app.html` | The game's source: page markup, styles and the model's JavaScript. Edit this file, not `index.html`. |
| `build.py` | Packs `src/app.html` into `index.html`. |
| `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `icon-512.png`, `site.webmanifest` | Browser tab and home-screen icons. |
| `.nojekyll` | Tells GitHub Pages to serve the files as they are, without running Jekyll. |
| `exam-board-references.md` | The checked reference list behind the model's figures. |

`The Exam Board.html` is the original export from before the home page was added. The site does not use it, so leave it out of the repository or delete it.

## Changing the game

1. Edit `src/app.html`.
2. Run `python3 build.py` (Python 3, no extra packages).
3. Open `index.html` in a browser to check the change.

In `src/app.html`, leave the long IDs such as `35b626f5-fd93-419a-a027-a70eeee01349` as they are. When the page opens, its loader replaces each one with the React library, page runtime or font file packed inside `index.html`.

## Publishing on GitHub Pages

1. Create a repository on GitHub, for example `exam-board`.
2. Add these files to it: `index.html`, the icon files, `site.webmanifest`, `.nojekyll`, and optionally `src/`, `build.py`, `README.md` and `exam-board-references.md`.
3. In the repository, open **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, then the `main` branch and the `/ (root)` folder, and save.
4. After a minute or two the game is live at `https://<your-username>.github.io/exam-board/`.

The page has no server code and no build step on GitHub, so any static host works the same way.

## Links into the game

Each screen has its own address, so the browser's back button works and you can link straight to a part of the game:

- `#finals`, `#ssc`, `#pgcert`, `#sandbox`: open a brief
- `#about`, `#references`: open the home page at that section
