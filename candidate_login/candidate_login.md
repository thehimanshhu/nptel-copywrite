---
source: https://nptel.ac.in/candidate_login
captured: 2026-11-18
verified: source-only
---

> **[CALLOUT BOX]** Shown only to administrators viewing a learner's page, above everything else.
> **Admin View:** Viewing profile as {learner email}
>
> **[Revert to My Profile](https://nptel.ac.in/candidate_login)** *(button)*

> **[IMAGE]** Learner's profile photo (a grey placeholder block when there is none).

# {learner name}

> **[TEXT · data]** Shows "NPTEL Candidate" when the learner has no name on record.

Email: {learner email}  (shows "N/A" when empty)

Date of Birth: {learner date of birth}

**[Logout](https://nptel.ac.in/auth/signout)** *(button)*

> **[FORM]** Shown to administrators only, below the profile card.
>
> View as student (admin only)
>
> Email *(text box, placeholder "student@example.com (leave empty to view your own profile)")*  **View** *(button)*

> **[TABLE · data]** Shown only when the learner has internship opportunities.

## NPTEL Internship

> **[BADGE · data]** Count of internships followed by the word "Opportunity" (one) or "Opportunities" (several).

> **[TABLE · data]** Columns: Course ID | Course Name | Start Date | End Date | Last Date to Apply | Apply | Attendance. One row per internship opportunity. Last Date to Apply always shows "-". Apply shows the internship status; when the status is "View" it is a link (opens in a new tab) to the internship application form on archive.nptel.ac.in. Attendance shows a "Submit Attendance" link (new tab, archive.nptel.ac.in) while attendance is open, otherwise the text "Closed".

> **[CARD · data]** Shown only when the learner has NPTEL Stars (two-column area, left card).

## NPTEL Stars

> **[BUTTON]** **Hide** / **Show** toggle at the right of the card heading; the list is shown by default.

> **[LIST · data]** One entry per star recognition: roll number, then "{category} • {timeline}". Buttons per entry: **Download** (the star certificate), **LinkedIn** (share the certificate image on LinkedIn), **Facebook** (share the certificate image on Facebook); all open in a new tab.

> **[CARD · data]** Shown only when the learner has internship certificates (two-column area, right card).

## Internships

> **[BUTTON]** **Hide** / **Show** toggle at the right of the card heading; the list is shown by default.

> **[LIST · data]** One entry per internship certificate: roll number, then "{internship name} • {timeline}", with a **Download** button (new tab).

> **[CARD · data]** Shown only when the learner has exam results.

## Exam Results

> **[FORM]** Marklist form wrapping the table below.

> **[TABLE · data]** Columns: (checkbox, with a "Select all" checkbox in the heading) | Timeline | Course | Assignment | Exam | Final | Action. One row per course the learner took. Action holds "Download Certificate" (link, new tab) when the learner is eligible, otherwise the text "Not eligible", plus a "View details" link to https://nptel.ac.in/candidate_login/scores?courseid={course id} (for administrators the link also carries &email={learner email}).

**Download Marklist ({n} selected)** *(button, disabled until a row is ticked; reads "Preparing…" while the file is generated)*

> **[CARD · data]** Shown only for learners with January 2020 records.

## January 2020 - Assignments & Refunds

### Refunds

> **[LIST · data]** One line per refund: "{course id} — {status} — Rs. {amount}".

### Assignments

> **[LIST · data]** One line per course: "{course id} — {course name} — Score: {assignment score}".

> **[CARD · data]** Shown only when the learner has BCBR certificates.

## BCBR Certificates

> **[TABLE · data]** Columns: Timeline | Course | Assignment | Exam | Final | Action. One row per BCBR course. Action holds "Download Certificate" (link, new tab) when eligible, otherwise the text "Not eligible".
