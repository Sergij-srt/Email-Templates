# Backlog: email marketing (DM + AFM)

Tasks agreed with Serhii to do later. Newest first.

## Hygiene workflows in place (26 Nov 2026), for reference

- DM `DM | Utility - Set Email DND (tag action:email-dnd)`: add tag `action:email-dnd` to any contacts (bulk is fine) → Email DND, score −100, tag removed. Use it instead of per-contact DND.
- DM `DM | Hygiene - Bounce suppression (2 strikes)`: Mailgun `failed` → 1st time `status:bounce-1`; 2nd time `status:hard-bounced` + `invalid email/bounced` + Email DND + score −100 + remove good/risky/hot lead/warm lead.
- DM `Mark invalid emails (validator bad/undeliverable)` (was "Mark bounced emails as invalid"): now only validator tags `bad` / `undeliverable` → `invalid email/bounced` + Email DND. The any-bounce trigger and `unknown_deliverability` trigger were removed.
- DM seeds: 235 warm-up inboxes (`trunk-rocky` replies) tagged `status:seed` + Email DND.
- AFM `AFM | Hygiene - Bounce suppression (2 strikes)`: same logic as DM.

## Still open from the audit

- DM: Customer replied → pipeline + task (copy of the AFM workflow; owner to confirm).
- DM: rebuild scoring on intent; switch off the open-based scoring workflows.
- Reply-to on both brands to an address on the mail. subdomain so replies land in GHL Conversations.
- DM #3 live email copies still show the old credential line (needs DM token or paste in UI).
- Campaign skeleton workflow (pre-send guard correctly wired) to clone for every send.
- Monthly report: replies, opportunities, meetings per campaign.
- DMARC rua on both mail. subdomains; then p=quarantine; DKIM 2048-bit.

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
