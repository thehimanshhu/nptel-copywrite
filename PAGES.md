# Page inventory

The route list is taken from the site's SvelteKit source (`src/routes`). Every route was checked against the live site on 2026-11-18.

Status: `done` = transcribed and checked word for word against the live page, every tab and view rendered on its own · `source-only` = needs a login, copied from the site code

## Public pages

| URL | File | Status |
|---|---|---|
| /aboutus | aboutus/aboutus.md | done |
| /careers | careers/careers.md | done |
| /chair-professors | chair-professors/chair-professors.md | done |
| /conference | conference/conference.md | done |
| /conferences | conferences/conferences.md | done |
| /coordinator | coordinator/coordinator.md | done |
| /csr | csr/csr.md | done |
| /documents | documents/documents.md | done |
| /domains | domains/domains.md | done |
| /domains/discipline | domains/discipline/discipline.md | done |
| /domains/discipline/&lt;id&gt; | domains/discipline/_details/_details.md | done (template) |
| /exam | exam/exam.md | done |
| /exam_1 | exam_1/exam_1.md | done |
| /faq | faq/faq.md | done |
| /fdp | fdp/fdp.md | done |
| /harddisk | harddisk/harddisk.md | done |
| /industrycertification | industrycertification/industrycertification.md | done |
| /initiative | initiative/initiative.md | done |
| /international | international/international.md | done |
| /internship | internship/internship.md | done |
| /localchapter | localchapter/localchapter.md | done |
| /localchapter/details | localchapter/details/details.md | done |
| /localchapter/discipline | localchapter/discipline/discipline.md | done |
| /localchapter/statistics/&lt;collegeid&gt; | localchapter/statistics/_collegeid/_collegeid.md | done (template) |
| /localchapter/statistics/&lt;collegeid&gt;/&lt;semester&gt; | localchapter/statistics/_collegeid/_semester/_semester.md | done (template) |
| /localchapter/lcstars/&lt;collegeid&gt;/&lt;semester&gt; | localchapter/lcstars/_collegeid/_semester/_semester.md | done (template) |
| /nia | nia/nia.md | done |
| /nptelbooks | nptelbooks/nptelbooks.md | done |
| /nptelstars | nptelstars/nptelstars.md | done |
| /nptelstars/domainscholars | nptelstars/domainscholars/domainscholars.md | done |
| /nptelstars/superstars | nptelstars/superstars/superstars.md | done |
| /nptelstars/megastars | nptelstars/megastars/megastars.md | done |
| /nptelstars/evangelists | nptelstars/evangelists/evangelists.md | done |
| /nptelstars/motivatedlearners | nptelstars/motivatedlearners/motivatedlearners.md | done |
| /nptelstars/enthusiasts | nptelstars/enthusiasts/enthusiasts.md | done |
| /nptelstars/disciplinestars | nptelstars/disciplinestars/disciplinestars.md | done |
| /nptelstars/believers | nptelstars/believers/believers.md | done |
| /nptelstars/champions | nptelstars/champions/champions.md | done |
| /nptelstars/domain-stats | nptelstars/domain-stats/domain-stats.md | done |
| /nptelstars/stars-video-feedback | nptelstars/stars-video-feedback/stars-video-feedback.md | done |
| /predocfellowship | predocfellowship/predocfellowship.md | done |
| /semester | semester/semester.md | done |
| /speciallecture | speciallecture/speciallecture.md | done |
| /statistics | statistics/statistics.md | done |
| /translation | translation/translation.md | done |
| /walloflove | walloflove/walloflove.md | done |
| /workshops | workshops/workshops.md | done |
| /yt-courses | yt-courses/yt-courses.md | done |
| /auth/signin | auth/signin/signin.md | done |
| /auth/signup | auth/signup/signup.md | done |

Pages whose URL contains an id (`<id>`, `<collegeid>`, `<semester>`) are written once as a template, with the varying values as placeholders. They are not written once per college or semester.

## Behind sign-in (redirect to /auth/signin)

| URL | File | Status |
|---|---|---|
| /candidate_login | candidate_login/candidate_login.md | source-only |
| /candidate_login/scores | candidate_login/scores/scores.md | source-only |
| /nia/dashboard | nia/dashboard/dashboard.md | source-only |
| /nia/dashboard/enrollment | nia/dashboard/enrollment/enrollment.md | source-only |
| /nia/dashboard/registration | nia/dashboard/registration/registration.md | source-only |
| /nia/dashboard/result | nia/dashboard/result/result.md | source-only |

## Excluded by request

`/`, `/courses`, `/courses/<nptel_id>`
