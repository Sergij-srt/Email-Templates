# DM – Email Campaign for All #3, November 2026 (A/B/C)

Brand: Danilo McGarry (DM sub-account). Source copy: "Email 3 – Are you paying premium AI prices for routine work?" from *Danilo_McGarry_AI_Email_Campaign.pdf*.
The body copy is identical in all three variants and verbatim from the doc. Only the subject line, preview text, layout and calls to action differ.

Workflow: **Email Campaign for All #3 November 2026** → Random split → Path A (33%) → Email 1, Path B (33%) → Email 2, Path C (34%) → Email 3.

| Path | GHL template (folder "Email Campaign November 2026") | Subject | Preview text |
|---|---|---|---|
| A → Email 1 | All #3 Nov 2026 - A - Executive brief (early reply CTA) | Are you paying premium AI prices for routine work? | Cost per successful task: the number finance and the business can actually assess. |
| B → Email 2 | All #3 Nov 2026 - B - Personal letter (plain) | Stop using a crane to lift a paperclip | Your AI budget can rise while the value of the work stays exactly the same. |
| C → Email 3 | All #3 Nov 2026 - C - Visual + task picker | What does each AI task really cost you? | The four-step evaluation I would put in front of your leadership team. |

## What each variant tests

- **A – Executive brief.** Same structure as the best-replying variant of *All #2 November* (Email 1: 14 replies vs 5 and 11): reply CTA right after the opening paragraph, illustration, numbered steps, pull-quote, closing CTA. Subject = the doc's question.
- **B – Personal letter.** Light HTML that reads like a one-to-one email: no header images, no buttons, two text links. Built for corporate gateways (Proofpoint/Mimecast) flagged in the audit. Subject = curiosity line from the illustration.
- **C – Visual + task picker.** Illustration first, steps as cards, the leadership question highlighted, and a one-tap picker ("Which task is consuming your budget?"). Each choice is tracked separately, so clicks show which task people care about even when they do not send the email. Subject = outcome question.

## Calls to action and tracking

All CTAs go to `https://go.danilomcgarry.com/mail-to-danilo?w=TOKENOMICS&c=…`. GHL records the click; the page opens the reader's email app to hi@danilomcgarry.com with **TOKENOMICS** in the subject.

- `c` = `tok-e3-<variant>-<position>` (e.g. `tok-e3-a-top`, `tok-e3-c-pick-contracts`)
- UTM: `utm_source=ghl&utm_medium=email&utm_campaign=2026-11-dm-all-03&utm_content=cta-reply-<variant>-<position>`

Greeting uses `Hi{{#if contact.first_name}} {{contact.first_name}}{{/if}},` with CSS capitalisation (many first names are stored in lower case). An empty name renders "Hi,".

Image: `crane-paperclip-ai-cost.jpg` in DM Media Storage.

## Before sending

1. In each Email action of the workflow pick the template above (subject and preview text are saved on the template – check they carried over).
2. From: Danilo McGarry. Set **Reply-to** to an address GHL reads so normal replies land in Conversations.
3. Confirmed hard bounces (tag `status:hard-bounced`) already have Email DND in DM.
4. Send a test of each template to a seed inbox: check the name merge field, images, links, and that GHL adds the **unsubscribe footer** (the templates contain the postal address, not their own unsubscribe link).

## How to judge the winner

Replies first, then clicks on the `c=` codes, read per path. Ignore opens (Apple MPP) and clicks within seconds of delivery (link scanners).
