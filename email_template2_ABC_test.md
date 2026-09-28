# Email 2: A/B/C test

The body copy is identical in all three versions. Only the subject line, the preview text and the layout change.

| Version | File | Subject line | Preview text | Layout |
|---|---|---|---|---|
| A (control) | `email_template2_A.html` | Your most expensive AI model should do the least work | The board metric should not be cost per million tokens. It should be cost per correct business outcome. | Card layout, stat cards, 60/30/10 tier cards, one China AI Tour button at the end |
| B | `email_template2_B.html` | Cost per token is the wrong AI metric | A cheap model that thinks for ten times longer, retries three times and needs human rework can be expensive. | Letter style in one white card, like a personal note; key numbers in coral, left-aligned button |
| C | `email_template2_C.html` | {{contact.first_name}}, would your CFO approve this? | For suitable workloads, the cost reduction can move into the 70-90% zone. | Dark headline block, early "China AI Tour" video link after the intro, large numbers, 60/30/10 bars, two buttons at the end (China AI Tour + Reply with ROUTING) |

## How to run it
- Split openers of Email 1 evenly across A, B and C (at least 1,000 per version, if the list allows).
- Send all three at the same time, so the send time doesn't skew the result.
- Judge the subject line and preview text on open rate. Judge the layout on clicks as a share of opens.
- Count ROUTING replies separately, because they are the highest-intent signal.

## Before sending
- The playlist URL `https://www.youtube.com/playlist?list=PLe9FR2buoEnM` looks cut off (playlist IDs are usually about 34 characters). Replace it in all three files.
- If you want clicks tagged in your email platform, swap the YouTube links for a tracking link created for Email 2.
