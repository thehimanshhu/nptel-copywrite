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

### What counts as text and what counts as data

* **Copied word for word:** headings, paragraphs, lists, FAQ questions and answers, contact details, form labels, button labels and table column headings.
* **Small fixed sets written into the page's own code** (a short list of cards, a rotating set of figures, a table of no more than about 25 rows): a placeholder tag, with the content copied in full underneath it.
* **Anything loaded from the database or an API, and any large fixed list (more than about 25 rows):** a placeholder that describes the data, not the data itself. It gives the fields or columns, roughly how many rows, the sort order, and any filters, search or pagination.
* **Learner names, emails and phone numbers** never appear in a file. The repo is public.

## Front matter

```yaml
---
source: https://nptel.ac.in/aboutus     # for templates: the URL pattern
example: https://nptel.ac.in/...         # templates only: the real URL used for checking
captured: 2026-11-18
verified: live                           # live = checked word for word against the rendered page
                                         # source-only = page needs a login; copied from the site's code
---
```

Pages whose URL contains an id are written once as a template, with the values that change as placeholders.

## Tools

The live page is the authority for wording. The site code ([nptel-iitm/nptel-site](https://github.com/nptel-iitm/nptel-site), `main`) is used to tell fixed text apart from data, and to find text that only appears after a click.

```bash
docker build -t nptel-copywrite-render:1.55 -f tools/Dockerfile.render tools   # once
tools/render.sh https://nptel.ac.in/faq /tmp/faq.html --click '.tab-button'     # render in headless Chromium; optional clicks
python3 -I tools/verify.py /tmp/faq.html faq/faq.md                             # word diff, live page vs markdown
```

`verify.py` leaves out the site header, footer and the site-wide migration notice. Results mean:

* `replace`: the wording differs. This must never happen.
* `delete`: text on the live page that is missing from the markdown. It must be copied in, or covered by a placeholder.
* `insert`: text in the markdown that wasn't in the rendered page. This is fine for content behind tabs or clicks that weren't rendered.
