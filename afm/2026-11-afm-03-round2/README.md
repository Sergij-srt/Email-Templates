# AFM - Email 03, round 2 test (from 27 Nov 2026)

Round 1 (AFM Email Campaign #4 November 2026 - A/B/C, 9,639 sends) showed that ~80% of clicks are mail-security scanners (clicks within 60 s of delivery). On real intent - "Book a call" clicks 2+ minutes after delivery - B led slightly: A 0.19%, B 0.28%, C 0.24%. No human replies in round 1.

Round 2 keeps B as the control and changes **one thing per variant**, so each result is readable.

| Path | GHL template | Subject | Preview text | What it tests |
|---|---|---|---|---|
| B1 (34%) | AFM Email 03 R2 - B1 Control (Cinematic) `6b0945fa832f6a0312cfae20` | Six weeks for a film. Your market moved in four days | Why the production calendar, not the idea, is what is costing you. | Control (round-1 winner) |
| B2 (33%) | AFM Email 03 R2 - B2 Subject test (Cinematic) `6b09460e38bdb25efe0526c4` | What if your next campaign film took days, not weeks? | Bring one live brief. We will show you what it looks like made our way. | Subject line only (body identical to B1) |
| D (33%) | AFM Email 03 R2 - D Personal letter (plain) `6b09460ea47910e3845009ac` | Six weeks for a film. Your market moved in four days | One line about the brief on your desk is enough. I will reply myself. | Format: plain personal letter from Danilo, no images or buttons, "just reply" as the main CTA (better for corporate gateways) |

UTM: `utm_campaign=2026-11-afm-03r2`, `utm_content=reel-b1 | reel-b2 | reel-d`.

All `mailto:alex@` links carry `?bcc=info@mail.afmcreatorstudio.com`, so a reply written to Alex also lands in GHL Conversations and starts the "Customer replied" workflow (task + email to Danilo). D has no mailto: replies go straight to the sender address, which GHL reads.

## Build checklist (GHL)

1. New workflow (or copy of #4): Add tag -> Drip -> **pre-send guard** (Email DND / invalid email / `status:hard-bounced`; route **"Eligible"** to the Split) -> Split 34/33/33 -> Email B1 / B2 / D.
2. In each Email action pick the template above; check subject and preview text carried over; open the preview to confirm it is the new version. Turn template sync on.
3. Exclude everyone who already got Email 03 in round 1 (tag `camp #4 nov 2026`).

## How to judge

Human replies first, then "Book a call" clicks that happen 2+ minutes after delivery. Ignore GHL click %, opens and anything within 60 s of delivery.
