# nptel-copywrite

The text of every page on [nptel.ac.in](https://nptel.ac.in), as Markdown, one file per page.

Out of scope: the landing page (`/`), `/courses` and `/courses/<nptel_id>`. Site header, navigation and footer are left out of every page.

## Layout

The folder tree mirrors the URL. A page lives in a folder named after its last path segment, in a file of the same name:

```
nptelstars/
  nptelstars.md                      -> /nptelstars
  superstars/superstars.md           -> /nptelstars/superstars
  domainscholars/domainscholars.md   -> /nptelstars/domainscholars
aboutus/
  aboutus.md                         -> /aboutus
```

`PAGES.md` lists every page and its status.

## Rules

1. **Text is copied exactly.** Spelling, capitalisation, punctuation and stray spaces are kept as they appear on the live page, typos included.
2. **Formatting follows the page.** Headings, lists, numbered steps, bold labels, tables and links are reproduced as they appear. Links point at their real targets.
3. **Anything that is not plain text becomes a placeholder.** Data from the database, images, carousels, tabs, cards, and so on.

## Placeholders

A placeholder is a blockquote that starts with a bold tag in square brackets, followed by a description of what is shown there:

```markdown
> **[TABLE · data]** Learners recognised in each category, by semester.
> Columns: NPTEL Stars | Jul-Dec 2019 | … | Jan-Apr 2026. One row per star category (9 rows).
```

Placeholders use a blockquote rather than `<angle brackets>` because GitHub treats `<…>` as an HTML tag and hides it.

Common tags:

* `CAROUSEL`, `ICON`, `IMAGE`, `VIDEO`: media, with alt text or file name
* `TABLE · data`, `GRID · data`, `LIST · data`, `CHART · data`: database content. The description gives the columns or card fields and roughly how many rows.
* `TABS`: each tab is its own `####` heading, and the placeholder says which tab opens by default
* `CALLOUT BOX`, `ROTATING STAT CARD`, `MODAL`: layout containers. Any static text inside them is copied in full.

Each file starts with front matter giving the source URL and the capture date.
