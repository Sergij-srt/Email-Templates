# Backlog: email marketing (DM + AFM)

Tasks agreed with Serhii to do later. Newest first.

## Out-of-office classifier with a temporary tag (both accounts, AFM first)

Agreed 26 Nov 2026. Not built yet.

- Trigger: Customer replied (email) and the body contains auto-reply phrases ("out of office", "automatic reply", "annual leave", "on leave", "away from the office", "back on", ...).
- Add tag `status:ooo` and set custom field `OOO since` = today. **No DND.**
- Wait: 90 days if the text mentions maternity / parental leave / sabbatical, otherwise 14 days.
- Then remove `status:ooo`, so the contact gets campaigns again.
- Re-entry on, so a later auto-reply starts a new pause.
- The "Customer replied" workflow removes `status:ooo` early when a human reply arrives.
- Campaign guard (pre-send if/else) skips contacts with `status:ooo` while the tag is on.
- Separate branch, permanent: "left the company" / "no longer with" / "no longer work" → tag `status:left-company` + Email DND + engagement score to 0.
- Limitation: GHL cannot read the return date from the text, so the wait is fixed (14 / 90 days).
