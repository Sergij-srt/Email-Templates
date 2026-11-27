"""Build 3 A/B/C HTML templates for DM 'Email Campaign for All #3 November 2026'.
Body copy is taken verbatim from the client's doc (Email 3) and shared by all variants."""
import html, os, sys

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

IMG = "https://files.leadconnectorhq.com/file/6b0598838b5100b36ad2f813/crane-paperclip-ai-cost.jpg"
PHOTO = "https://files.leadconnectorhq.com/file/6af482f0512d2edab6a04e58/danilo.png"
LOGO = "https://files.leadconnectorhq.com/file/6afab85077a01e46221fed8c/aimcgarry-logo-small-png-yyv9edw34auzpq3l-1.png"
ADDRESS = "Unit 182, 54 Bloomfield Avenue, Belfast, Northern Ireland, BT5 5AD, United Kingdom"
CRED = "Former Head of AI Fortune 100 companies"

# ---- verbatim copy from the doc (do not edit) ----
TITLE = "Are you paying premium AI prices for routine work?"
LEDE = ("Your AI budget can rise while the value of the work stays exactly the same. "
        "Using your most capable model for every request is one purchasing decision worth challenging.")
P_CRANE = ("The crane lifting a paperclip is deliberately absurd. Yet imagine the same premium model handling "
           "both simple request sorting and complex contract exceptions, with nobody asking whether both jobs need it.")
P_REC = ("My recommendation is to make cost per successful task part of your AI strategy. That connects the "
         "technology decision to an outcome finance and the business can actually assess.")
P_TOKEN = ("Token prices alone will not answer the question. A cheap output that needs repeated correction can "
           "become expensive. A premium output can also cost more than the task warrants.")
P_EVAL = "Here is the evaluation I would put in front of the leadership team:"
STEPS = [
    ("Define success before selecting a model.",
     "Specify the required quality, response time, data protections and escalation rules. Involve the person who will use the answer."),
    ("Compare suitable options on the same work.",
     "Test representative requests and difficult exceptions against the same acceptance criteria. Include simpler options where they could meet the requirements."),
    ("Count the full operating cost.",
     "Include model usage, retries, human checking, integration and ongoing support. Measure the resources needed to produce an acceptable result."),
    ("Route work according to its demands.",
     "Use the simplest option that meets the agreed standard. Send harder cases to a more capable model or a person when appropriate."),
]
P_START = ("I recommend starting with one high-volume workflow because repeated small decisions deserve commercial "
           "scrutiny. It also gives your team a manageable place to test routing before adding complexity elsewhere.")
P_REVIEW = ("Keep reviewing the choice as the work changes. A model that suited the pilot may not be the best fit "
            "for the eventual volume, risk or quality requirements.")
P_QUESTION = ("The leadership question is straightforward: what does it cost us to complete this task successfully, "
              "including the human effort?")
CTA_1 = ("If your AI bill is growing faster than your understanding of its value, or believe it is about to, reply to me at ")
CTA_EMAIL = "hi@danilomcgarry.com"
CTA_2 = (". Tell me which task is consuming the budget and I will show you what tokenomics strategy helps to "
         "ensure you are getting the best output for the cheapest spend.")
SIGN = "Danilo McGarry"

e = html.escape


def link(variant, pos):
    """Tracked CTA: GHL records the click, the page opens the reader's email app (subject TOKENOMICS)."""
    return ("https://go.danilomcgarry.com/mail-to-danilo?w=TOKENOMICS"
            f"&amp;c=tok-e3-{variant}-{pos}&amp;utm_source=ghl&amp;utm_medium=email"
            f"&amp;utm_campaign=2026-11-dm-all-03&amp;utm_content=cta-reply-{variant}-{pos}")


GREETING = 'Hi{{#if contact.first_name}} <span style="text-transform:capitalize;">{{contact.first_name}}</span>{{/if}},'


def shell(title, preheader, body, bg):
    pad = "&#847;&zwnj;&nbsp;" * 20
    return f"""<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>{e(title)}</title>
<style>
  body{{margin:0!important;padding:0!important;width:100%!important;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;}}
  table{{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0;}}
  img{{border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;display:block;}}
  a{{text-decoration:none;}}
  @media only screen and (max-width:620px){{
    .wrap{{width:100%!important;}}
    .px{{padding-left:20px!important;padding-right:20px!important;}}
    .h1{{font-size:26px!important;line-height:32px!important;}}
    .stack{{display:block!important;width:100%!important;}}
    .stack-pad{{padding:0 0 12px 0!important;}}
    .hide-m{{display:none!important;}}
    .btn a{{display:block!important;}}
    .img-m{{width:100%!important;max-width:340px!important;height:auto!important;}}
  }}
</style>
</head>
<body style="margin:0;padding:0;background-color:{bg};">
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;color:{bg};opacity:0;">{e(preheader)}{pad}</div>
{body}
</body>
</html>
"""


def p(text, style):
    return f'<p style="margin:0 0 18px 0;{style}">{text}</p>'


def compliance(muted, align):
    return (f'Advertisement from Danilo McGarry, sent on behalf of Illimitato Limited.<br>{ADDRESS}<br>'
            f'You can unsubscribe from these emails at any time: '
            f'<a href="{{{{email.unsubscribe_link}}}}" target="_blank" style="color:{muted};text-decoration:underline;">Unsubscribe</a>')


def footer(color, muted):
    return f"""
<tr><td class="px" style="padding:22px 40px 34px 40px;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:18px;color:{muted};text-align:center;">
{compliance(muted, "center")}
</td></tr>"""


def button(href, label, bg, color="#ffffff", align="center", radius=6, size=16):
    return f"""<table role="presentation" cellpadding="0" cellspacing="0" border="0" align="{align}" class="btn" style="margin:0 auto;">
<tr><td align="center" bgcolor="{bg}" style="border-radius:{radius}px;background-color:{bg};">
<a href="{href}" target="_blank" style="display:inline-block;padding:15px 28px;font-family:Arial,Helvetica,sans-serif;font-size:{size}px;line-height:20px;font-weight:bold;color:{color};text-decoration:none;border-radius:{radius}px;">{label}</a>
</td></tr></table>"""


# ======================================================================
# Variant A - Executive brief, reply CTA above the fold (structure of best-replying Nov #2 variant)
# ======================================================================
def variant_a():
    V = "a"
    ink, muted, burg, bg, card = "#1f1f1f", "#5f5f5f", "#8c263c", "#f5f3ef", "#ffffff"
    body_p = f"font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:26px;color:{ink};"
    steps = ""
    for i, (h, t) in enumerate(STEPS, 1):
        border = "" if i == len(STEPS) else "border-bottom:1px solid #ebe6df;"
        steps += f"""<tr>
<td valign="top" style="width:34px;padding:14px 0;{border}font-family:Georgia,'Times New Roman',serif;font-size:22px;line-height:24px;font-weight:bold;color:{burg};">{i}.</td>
<td valign="top" style="padding:14px 0;{border}font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:24px;color:{ink};"><strong>{e(h)}</strong> {e(t)}</td>
</tr>"""
    content = f"""
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{bg};">
<tr><td align="center" style="padding:24px 10px 0 10px;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;">
  <!-- header -->
  <tr><td style="padding:0 0 16px 0;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
      <td valign="middle" style="width:56px;padding:0 12px 0 20px;"><img src="{PHOTO}" width="48" height="48" alt="Danilo McGarry" style="width:48px;height:48px;border-radius:6px;"></td>
      <td valign="middle" style="font-family:Georgia,'Times New Roman',serif;font-size:18px;line-height:22px;color:{ink};">Danilo McGarry<br><span style="font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:18px;color:{muted};">{CRED}</span></td>
      <td valign="middle" align="right" class="hide-m" style="padding-right:20px;"><img src="{LOGO}" width="140" alt="AI McGarry" style="width:140px;height:auto;"></td>
    </tr></table>
  </td></tr>
  <!-- card -->
  <tr><td style="background-color:{card};border-top:3px solid {burg};">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
      <tr><td class="px" style="padding:36px 40px 8px 40px;">
        <h1 class="h1" style="margin:0 0 22px 0;font-family:Georgia,'Times New Roman',serif;font-size:31px;line-height:38px;font-weight:normal;color:{ink};">{e(TITLE)}</h1>
        {p(GREETING, body_p)}
        {p(f"<strong>{e(LEDE)}</strong>", body_p)}
      </td></tr>
      <!-- early CTA -->
      <tr><td class="px" style="padding:4px 40px 26px 40px;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#fbf3f4;border:1px solid #f0d9dd;border-radius:8px;">
          <tr><td align="center" style="padding:22px 20px 20px 20px;">
            <p style="margin:0 0 14px 0;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;font-weight:bold;color:{burg};">Which task is consuming your AI budget?</p>
            {button(link(V, "top"), "Ask Danilo about my AI&nbsp;spend&nbsp;&rarr;", burg)}
            <p style="margin:12px 0 0 0;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:18px;color:{muted};">Opens a reply to Danilo. You can also just reply to this email.</p>
          </td></tr>
        </table>
      </td></tr>
      <tr><td class="px" style="padding:0 40px;">
        {p(e(P_CRANE), body_p)}
      </td></tr>
      <tr><td align="center" style="padding:6px 40px 26px 40px;">
        <a href="{link(V, 'image')}" target="_blank"><img class="img-m" src="{IMG}" width="380" alt="Stop using a crane to lift a paperclip. Choose AI by the task it must finish." style="width:380px;max-width:100%;height:auto;border:1px solid #e7c9ce;"></a>
      </td></tr>
      <tr><td class="px" style="padding:0 40px;">
        {p(e(P_REC), body_p)}
        {p(e(P_TOKEN), body_p)}
        {p(e(P_EVAL), body_p)}
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 20px 0;">{steps}</table>
        {p(e(P_START), body_p)}
        {p(e(P_REVIEW), body_p)}
      </td></tr>
      <!-- pull quote -->
      <tr><td class="px" style="padding:4px 40px 22px 40px;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
          <td style="border-left:4px solid {burg};padding:4px 0 4px 18px;font-family:Georgia,'Times New Roman',serif;font-size:20px;line-height:30px;font-style:italic;color:{ink};">{e(P_QUESTION)}</td>
        </tr></table>
      </td></tr>
      <tr><td class="px" style="padding:0 40px;">
        {p(f'<strong>{e(CTA_1)}<a href="{link(V, "inline")}" target="_blank" style="color:{burg};text-decoration:underline;">{CTA_EMAIL}</a>{e(CTA_2)}</strong>', f"font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:26px;color:{burg};")}
      </td></tr>
      <tr><td class="px" align="center" style="padding:8px 40px 30px 40px;">
        {button(link(V, "bottom"), "Tell Danilo which task is consuming the budget", burg)}
      </td></tr>
      <!-- signature -->
      <tr><td class="px" style="padding:0 40px 34px 40px;">
        <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid #ebe6df;width:100%;"><tr>
          <td valign="middle" style="width:60px;padding-top:20px;"><img src="{PHOTO}" width="48" height="48" alt="" style="width:48px;height:48px;border-radius:24px;"></td>
          <td valign="middle" style="padding-top:20px;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:22px;color:{ink};"><strong>{SIGN}</strong><br><span style="font-size:13px;color:{muted};">{CRED}</span></td>
        </tr></table>
      </td></tr>
    </table>
  </td></tr>
  {footer(ink, "#8a8a8a")}
</table>
</td></tr></table>"""
    return shell(TITLE, "Cost per successful task: the number finance and the business can actually assess.", content, bg)


# ======================================================================
# Variant B - Personal plain-text letter (light HTML, 2 links, no header images)
# ======================================================================
def variant_b():
    V = "b"
    ink, muted, link_c = "#222222", "#6b6b6b", "#8c263c"
    body_p = f"font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:26px;color:{ink};"
    steps = "".join(
        f'<p style="margin:0 0 14px 0;{body_p}">{i}. <strong>{e(h)}</strong> {e(t)}</p>'
        for i, (h, t) in enumerate(STEPS, 1))
    content = f"""
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#ffffff;">
<tr><td align="center" style="padding:0 10px;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;">
  <tr><td class="px" style="padding:32px 24px 6px 24px;">
    {p(GREETING, body_p)}
    {p(f"<strong>{e(LEDE)}</strong>", body_p)}
    {p(e(P_CRANE), body_p)}
  </td></tr>
  <tr><td align="left" class="px" style="padding:0 24px 22px 24px;">
    <img class="img-m" src="{IMG}" width="320" alt="Stop using a crane to lift a paperclip. Choose AI by the task it must finish." style="width:320px;max-width:100%;height:auto;border:1px solid #e5e5e5;">
  </td></tr>
  <tr><td class="px" style="padding:0 24px;">
    {p(e(P_REC), body_p)}
    {p(e(P_TOKEN), body_p)}
    {p(e(P_EVAL), body_p)}
    {steps}
    <div style="height:4px;line-height:4px;font-size:4px;">&nbsp;</div>
    {p(e(P_START), body_p)}
    {p(e(P_REVIEW), body_p)}
    {p(e(P_QUESTION), body_p)}
    {p(f'<strong>{e(CTA_1)}<a href="{link(V, "inline")}" target="_blank" style="color:{link_c};text-decoration:underline;">{CTA_EMAIL}</a>{e(CTA_2)}</strong>', body_p)}
    {p(f'<a href="{link(V, "textlink")}" target="_blank" style="color:{link_c};text-decoration:underline;font-weight:bold;">&rarr; Reply with the one task consuming your AI budget</a>', body_p)}
    <p style="margin:26px 0 4px 0;{body_p}">{SIGN}</p>
    <p style="margin:0 0 28px 0;font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:20px;color:{muted};">{CRED}<br>danilomcgarry.com</p>
  </td></tr>
  <tr><td class="px" style="padding:0 24px;"><div style="border-top:1px solid #eeeeee;height:1px;line-height:1px;font-size:1px;">&nbsp;</div></td></tr>
  <tr><td class="px" style="padding:16px 24px 30px 24px;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:18px;color:#999999;">
    {compliance("#999999", "left")}
  </td></tr>
</table>
</td></tr></table>"""
    return shell("Stop using a crane to lift a paperclip", LEDE.split(". ")[0] + ".", content, "#ffffff")


# ======================================================================
# Variant C - Visual-first, scannable cards, one-tap task picker
# ======================================================================
def variant_c():
    V = "c"
    ink, muted, burg, red, bg, cream = "#1d1e20", "#606266", "#8c263c", "#c8102e", "#efece6", "#faf8f5"
    body_p = f"font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:26px;color:{ink};"

    def card(i, h, t):
        return f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{cream};border:1px solid #ece6dc;border-radius:8px;">
<tr><td style="padding:18px 18px 16px 18px;">
  <table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" valign="middle" width="30" height="30" style="width:30px;height:30px;border-radius:15px;background-color:{burg};font-family:Arial,Helvetica,sans-serif;font-size:14px;font-weight:bold;color:#ffffff;">{i}</td></tr></table>
  <p style="margin:12px 0 6px 0;font-family:Georgia,'Times New Roman',serif;font-size:17px;line-height:23px;font-weight:bold;color:{ink};">{e(h)}</p>
  <p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:21px;color:{muted};">{e(t)}</p>
</td></tr></table>"""

    grid = ""
    for row in (STEPS[0:2], STEPS[2:4]):
        base = STEPS.index(row[0]) + 1
        grid += f"""<tr>
<td class="stack stack-pad" valign="top" width="50%" style="width:50%;padding:0 6px 12px 0;">{card(base, *row[0])}</td>
<td class="stack stack-pad" valign="top" width="50%" style="width:50%;padding:0 0 12px 6px;">{card(base + 1, *row[1])}</td>
</tr>"""

    choices = [("routing", "Request sorting &amp; triage"),
               ("contracts", "Contract &amp; document exceptions"),
               ("service", "Customer service replies"),
               ("other", "Another task")]
    picker = "".join(
        f"""<tr><td style="padding:0 0 10px 0;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
<td style="border:2px solid {burg};border-radius:8px;background-color:#ffffff;">
<a href="{link(V, 'pick-' + key)}" target="_blank" style="display:block;padding:14px 18px;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:20px;font-weight:bold;color:{burg};text-decoration:none;">{label} <span style="float:right;">&rarr;</span></a>
</td></tr></table></td></tr>""" for key, label in choices)

    content = f"""
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{bg};">
<tr><td align="center" style="padding:20px 10px 0 10px;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background-color:#ffffff;border-radius:10px;">
  <!-- slim header -->
  <tr><td class="px" style="padding:18px 32px;border-bottom:1px solid #eeeae4;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
      <td valign="middle" style="font-family:Arial,Helvetica,sans-serif;font-size:11px;line-height:16px;letter-spacing:2px;text-transform:uppercase;color:{burg};font-weight:bold;">AI cost brief</td>
      <td valign="middle" align="right" style="font-family:Georgia,'Times New Roman',serif;font-size:15px;line-height:20px;color:{ink};">Danilo McGarry</td>
    </tr></table>
  </td></tr>
  <!-- hero image first -->
  <tr><td align="center" style="padding:28px 32px 8px 32px;background-color:#ffffff;">
    <a href="{link(V, 'hero')}" target="_blank"><img class="img-m" src="{IMG}" width="360" alt="Stop using a crane to lift a paperclip. Choose AI by the task it must finish." style="width:360px;max-width:100%;height:auto;border-radius:6px;border:1px solid #e9d3d6;"></a>
  </td></tr>
  <tr><td class="px" style="padding:22px 40px 0 40px;">
    <h1 class="h1" style="margin:0 0 20px 0;font-family:Georgia,'Times New Roman',serif;font-size:29px;line-height:36px;font-weight:normal;color:{ink};">{e(TITLE)}</h1>
    {p(GREETING, body_p)}
    {p(f'<strong>{e(LEDE)}</strong>', body_p)}
    {p(e(P_CRANE), body_p)}
    {p(e(P_REC), body_p)}
    {p(e(P_TOKEN), body_p)}
    {p(f'<strong>{e(P_EVAL)}</strong>', body_p)}
  </td></tr>
  <tr><td class="px" style="padding:2px 40px 8px 40px;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{grid}</table>
  </td></tr>
  <tr><td class="px" style="padding:6px 40px 0 40px;">
    {p(e(P_START), body_p)}
    {p(e(P_REVIEW), body_p)}
  </td></tr>
  <!-- highlighted question -->
  <tr><td class="px" style="padding:4px 40px 24px 40px;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{ink};border-radius:8px;"><tr>
      <td style="padding:22px 24px;font-family:Georgia,'Times New Roman',serif;font-size:19px;line-height:28px;color:#ffffff;">{e(P_QUESTION)}</td>
    </tr></table>
  </td></tr>
  <tr><td class="px" style="padding:0 40px 6px 40px;">
    {p(f'<strong>{e(CTA_1)}<a href="{link(V, "inline")}" target="_blank" style="color:{burg};text-decoration:underline;">{CTA_EMAIL}</a>{e(CTA_2)}</strong>', f"font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:26px;color:{burg};")}
  </td></tr>
  <!-- one-tap picker -->
  <tr><td class="px" style="padding:4px 40px 10px 40px;">
    <p style="margin:0 0 12px 0;font-family:Georgia,'Times New Roman',serif;font-size:19px;line-height:26px;color:{ink};">Which task is consuming your budget?</p>
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{picker}</table>
    <p style="margin:4px 0 26px 0;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:18px;color:{muted};">One tap opens a reply to Danilo. You can also just reply to this email.</p>
  </td></tr>
  <!-- signature -->
  <tr><td class="px" style="padding:0 40px 32px 40px;">
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="width:100%;border-top:1px solid #eeeae4;"><tr>
      <td valign="middle" style="width:60px;padding-top:20px;"><img src="{PHOTO}" width="48" height="48" alt="" style="width:48px;height:48px;border-radius:24px;"></td>
      <td valign="middle" style="padding-top:20px;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:22px;color:{ink};"><strong>{SIGN}</strong><br><span style="font-size:13px;color:{muted};">{CRED}</span></td>
    </tr></table>
  </td></tr>
</table>
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;">{footer(ink, "#8a8a8a")}</table>
</td></tr></table>"""
    return shell("What does each AI task really cost you?", "The four-step evaluation I would put in front of your leadership team.", content, bg)


for name, fn in (("variant-a-executive-brief.html", variant_a),
                 ("variant-b-personal-letter.html", variant_b),
                 ("variant-c-visual-task-picker.html", variant_c)):
    open(os.path.join(OUT, name), "w").write(fn())
    print("wrote", name)
