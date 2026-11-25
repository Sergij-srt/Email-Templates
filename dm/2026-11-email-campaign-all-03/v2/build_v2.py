"""v2 redesign of DM All #3 November 2026 (A/B/C), built for click-through.
Body copy is imported verbatim from ../build.py (client's doc, Email 3)."""
import html, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "build.py")).read()
ns = {}
exec(src.split("e = html.escape")[0].replace("OUT = sys.argv[1]", "OUT = None")
     .replace("os.makedirs(OUT, exist_ok=True)", ""), ns)
g = ns  # verbatim constants: TITLE, LEDE, P_*, STEPS, CTA_1, CTA_EMAIL, CTA_2, SIGN, IMG, PHOTO, LOGO, ADDRESS, CRED
e = html.escape
OUT = HERE

CAMPAIGN = "2026-11-dm-all-03-v2"
INK, MUTED, BURG, BG, CARD, LINE, CREAM = "#1d1d1f", "#6b6b70", "#8c263c", "#f3f1ec", "#ffffff", "#ebe6df", "#faf8f4"
F_SANS = "Arial,Helvetica,sans-serif"
F_SERIF = "Georgia,'Times New Roman',serif"


def reply_url(v, pos):
    return ("https://go.danilomcgarry.com/mail-to-danilo?w=TOKENOMICS"
            f"&amp;c=tok-e3v2-{v}-{pos}&amp;utm_source=ghl&amp;utm_medium=email"
            f"&amp;utm_campaign={CAMPAIGN}&amp;utm_content=reply-{v}-{pos}")


def guide_url(v, pos):
    return ("https://danilomcgarry.com/free-guide?utm_source=ghl&amp;utm_medium=email"
            f"&amp;utm_campaign={CAMPAIGN}&amp;utm_content=guide-{v}-{pos}")


GREETING = 'Hi{{#if contact.first_name}} <span style="text-transform:capitalize;">{{contact.first_name}}</span>{{/if}},'


def P(text, size=16, lh=27, color=INK, mb=18, extra=""):
    return f'<p style="margin:0 0 {mb}px 0;font-family:{F_SANS};font-size:{size}px;line-height:{lh}px;color:{color};{extra}">{text}</p>'


def button(href, label, bg=BURG, color="#ffffff", full=False, border=None):
    bd = f"border:2px solid {border};" if border else ""
    w = ' width="100%"' if full else ""
    return f"""<table role="presentation"{w} cellpadding="0" cellspacing="0" border="0" class="btn"><tr>
<td align="center" bgcolor="{bg}" style="border-radius:10px;background-color:{bg};{bd}">
<a href="{href}" target="_blank" style="display:block;padding:16px 26px;font-family:{F_SANS};font-size:16px;line-height:20px;font-weight:bold;color:{color};text-decoration:none;border-radius:10px;">{label}</a>
</td></tr></table>"""


def shell(title, preheader, rows):
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
    .px{{padding-left:22px!important;padding-right:22px!important;}}
    .h1{{font-size:27px!important;line-height:33px!important;}}
    .stack{{display:block!important;width:100%!important;padding-left:0!important;padding-right:0!important;}}
    .hide-m{{display:none!important;}}
    .img-m{{width:100%!important;max-width:360px!important;height:auto!important;}}
  }}
</style>
</head>
<body style="margin:0;padding:0;background-color:{BG};">
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;color:{BG};opacity:0;">{e(preheader)}{pad}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{BG};">
<tr><td align="center" style="padding:22px 10px 0 10px;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;">
{rows}
<tr><td class="px" style="padding:22px 36px 34px 36px;font-family:{F_SANS};font-size:12px;line-height:18px;color:#8a8a8e;text-align:center;">
Advertisement from Danilo McGarry, sent on behalf of Illimitato Limited.<br>{g['ADDRESS']}<br>You can unsubscribe from these emails at any time: <a href="{{{{email.unsubscribe_link}}}}" target="_blank" style="color:#8a8a8e;text-decoration:underline;">Unsubscribe</a>
</td></tr>
</table>
</td></tr></table>
</body>
</html>
"""


def topbar():
    return f"""<tr><td style="padding:0 6px 14px 6px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
<td valign="middle" style="width:50px;"><img src="{g['PHOTO']}" width="42" height="42" alt="Danilo McGarry" style="width:42px;height:42px;border-radius:21px;"></td>
<td valign="middle" style="font-family:{F_SANS};font-size:14px;line-height:19px;color:{INK};"><strong>Danilo McGarry</strong><br><span style="font-size:12px;color:{MUTED};">{g['CRED']}</span></td>
<td valign="middle" align="right" class="hide-m"><img src="{g['LOGO']}" width="118" alt="AI McGarry" style="width:118px;height:auto;"></td>
</tr></table></td></tr>"""


def card_open(pad_top=34):
    return f'<tr><td style="background-color:{CARD};border-radius:14px;border:1px solid {LINE};"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="height:{pad_top}px;line-height:{pad_top}px;font-size:1px;">&nbsp;</td></tr>'


CARD_CLOSE = "</table></td></tr>"


def row(inner, pad="0 36px"):
    return f'<tr><td class="px" style="padding:{pad};">{inner}</td></tr>'


def image(v, pos, width=400, href=None):
    href = href or reply_url(v, pos)
    return f"""<tr><td align="center" class="px" style="padding:4px 36px 26px 36px;">
<a href="{href}" target="_blank"><img class="img-m" src="{g['IMG']}" width="{width}" alt="Stop using a crane to lift a paperclip. Choose AI by the task it must finish." style="width:{width}px;max-width:100%;height:auto;border-radius:10px;border:1px solid #ecd7da;"></a>
</td></tr>"""


def steps_cards():
    out = ""
    for i, (h, t) in enumerate(g["STEPS"], 1):
        out += f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 10px 0;background-color:{CREAM};border-radius:10px;border:1px solid {LINE};"><tr>
<td valign="top" style="width:46px;padding:16px 0 16px 16px;"><table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" valign="middle" width="30" height="30" style="width:30px;height:30px;border-radius:15px;background-color:{BURG};font-family:{F_SANS};font-size:14px;font-weight:bold;color:#ffffff;">{i}</td></tr></table></td>
<td valign="top" style="padding:16px 18px 16px 10px;font-family:{F_SANS};font-size:15px;line-height:23px;color:{INK};"><strong style="font-family:{F_SERIF};font-size:17px;">{e(h)}</strong><br><span style="color:#4a4a4f;">{e(t)}</span></td>
</tr></table>"""
    return out


def quote():
    return f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:6px 0 24px 0;"><tr>
<td style="border-left:4px solid {BURG};padding:2px 0 2px 18px;font-family:{F_SERIF};font-size:20px;line-height:30px;font-style:italic;color:{INK};">{e(g['P_QUESTION'])}</td></tr></table>"""


def reply_para(v):
    return P(f'<strong>{e(g["CTA_1"])}<a href="{reply_url(v, "inline")}" target="_blank" style="color:{BURG};text-decoration:underline;">{g["CTA_EMAIL"]}</a>{e(g["CTA_2"])}</strong>', color=BURG)


def body_core(v, with_image=True):
    """The letter, verbatim, in reading order."""
    r = row(P(e(g["P_CRANE"])))
    if with_image:
        r += image(v, "image")
    r += row(P(e(g["P_REC"])) + P(e(g["P_TOKEN"])) + P(f'<strong>{e(g["P_EVAL"])}</strong>') + steps_cards()
             + '<div style="height:12px;line-height:12px;font-size:12px;">&nbsp;</div>'
             + P(e(g["P_START"])) + P(e(g["P_REVIEW"])) + quote() + reply_para(v))
    return r


def signature():
    return row(f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid {LINE};"><tr>
<td valign="middle" style="width:58px;padding-top:20px;"><img src="{g['PHOTO']}" width="46" height="46" alt="" style="width:46px;height:46px;border-radius:23px;"></td>
<td valign="middle" style="padding-top:20px;font-family:{F_SANS};font-size:15px;line-height:22px;color:{INK};"><strong>{g['SIGN']}</strong><br><span style="font-size:13px;color:{MUTED};">{g['CRED']}</span></td>
</tr></table>""", pad="6px 36px 34px 36px")


def ps(v):
    return row(P(f'<strong>P.S.</strong> If you are scaling AI beyond the pilot, my free 10-slide playbook covers the governance structures and the 14 mistakes I see most often. <a href="{guide_url(v, "ps")}" target="_blank" style="color:{BURG};text-decoration:underline;font-weight:bold;">Get the free playbook&nbsp;&rarr;</a>', size=15, lh=24, color="#3a3a3f"), pad="0 36px 10px 36px")


# ---------------------------------------------------------------- A: offer card above the fold
def variant_a():
    v = "a"
    offer = f"""<tr><td class="px" style="padding:0 36px 28px 36px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{BURG};border-radius:12px;"><tr><td style="padding:24px 24px 22px 24px;">
<p style="margin:0 0 6px 0;font-family:{F_SANS};font-size:11px;line-height:16px;letter-spacing:2px;text-transform:uppercase;font-weight:bold;color:#f3c9d1;">Free &middot; 10-slide playbook</p>
<p style="margin:0 0 8px 0;font-family:{F_SERIF};font-size:22px;line-height:28px;color:#ffffff;">How to scale your AI programme</p>
<p style="margin:0 0 18px 0;font-family:{F_SANS};font-size:14px;line-height:21px;color:#f6e6e9;">The governance structures and the 14 mistakes that keep AI stuck at the pilot stage.</p>
{button(guide_url(v, "hero"), "Get the free playbook&nbsp;&rarr;", bg="#ffffff", color=BURG, full=True)}
</td></tr></table></td></tr>"""
    rows = topbar() + card_open() + row(f'<h1 class="h1" style="margin:0 0 18px 0;font-family:{F_SERIF};font-size:32px;line-height:39px;font-weight:normal;color:{INK};">{e(g["TITLE"])}</h1>' + P(GREETING) + P(f'<strong>{e(g["LEDE"])}</strong>')) \
        + offer + body_core(v) + row(button(reply_url(v, "bottom"), "Tell Danilo which task is consuming the budget", full=True), pad="4px 36px 26px 36px") \
        + ps(v) + signature() + CARD_CLOSE
    return shell(g["TITLE"], "Cost per successful task: the number finance and the business can actually assess.", rows)


# ---------------------------------------------------------------- B: one-tap poll first
def variant_b():
    v = "b"
    opts = [("under-10", "Under 10%"), ("10-30", "10&ndash;30%"), ("30-60", "30&ndash;60%"), ("over-60", "Over 60%")]

    def cell(key, label, side):
        padd = "0 6px 12px 0" if side == "l" else "0 0 12px 6px"
        return f"""<td class="stack" width="50%" valign="top" style="width:50%;padding:{padd};">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="border:2px solid {BURG};border-radius:12px;background-color:#ffffff;">
<a href="{guide_url(v, 'poll-' + key)}" target="_blank" style="display:block;padding:18px 10px;font-family:{F_SANS};font-size:19px;line-height:22px;font-weight:bold;color:{BURG};text-decoration:none;">{label}</a>
</td></tr></table></td>"""
    grid = f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{cell(*opts[0], "l")}{cell(*opts[1], "r")}</tr><tr>{cell(*opts[2], "l")}{cell(*opts[3], "r")}</tr></table>'
    poll = f"""<tr><td class="px" style="padding:0 36px 26px 36px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{CREAM};border:1px solid {LINE};border-radius:14px;"><tr><td style="padding:24px 22px 12px 22px;">
<p style="margin:0 0 6px 0;font-family:{F_SANS};font-size:11px;line-height:16px;letter-spacing:2px;text-transform:uppercase;font-weight:bold;color:{BURG};">One-tap question</p>
<p style="margin:0 0 16px 0;font-family:{F_SERIF};font-size:23px;line-height:30px;color:{INK};">How much of your AI spend goes on routine work?</p>
{grid}
<p style="margin:2px 0 10px 0;font-family:{F_SANS};font-size:12px;line-height:18px;color:{MUTED};">Tap your answer. It opens my free 10-slide AI scaling playbook.</p>
</td></tr></table></td></tr>"""
    rows = topbar() + card_open(30) + poll \
        + row(f'<h1 class="h1" style="margin:0 0 18px 0;font-family:{F_SERIF};font-size:30px;line-height:37px;font-weight:normal;color:{INK};">{e(g["TITLE"])}</h1>' + P(GREETING) + P(f'<strong>{e(g["LEDE"])}</strong>')) \
        + body_core(v) + row(button(reply_url(v, "bottom"), "Reply to Danilo&nbsp;&rarr;", full=True), pad="4px 36px 26px 36px") \
        + ps(v) + signature() + CARD_CLOSE
    return shell(g["TITLE"], "Your AI budget can rise while the value of the work stays exactly the same.", rows)


# ---------------------------------------------------------------- C: image hero + two clear choices
def variant_c():
    v = "c"
    hero = f"""<tr><td align="center" class="px" style="padding:0 36px 22px 36px;">
<a href="{guide_url(v, 'hero-image')}" target="_blank"><img class="img-m" src="{g['IMG']}" width="380" alt="Stop using a crane to lift a paperclip. Choose AI by the task it must finish." style="width:380px;max-width:100%;height:auto;border-radius:12px;border:1px solid #ecd7da;"></a>
</td></tr>"""
    choices = f"""<tr><td class="px" style="padding:0 36px 28px 36px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
<td class="stack" width="50%" valign="top" style="width:50%;padding:0 6px 10px 0;">{button(guide_url(v, 'top'), "Get the free playbook&nbsp;&rarr;", full=True)}</td>
<td class="stack" width="50%" valign="top" style="width:50%;padding:0 0 10px 6px;">{button(reply_url(v, 'top'), "Ask Danilo about my AI&nbsp;spend", bg="#ffffff", color=BURG, full=True, border=BURG)}</td>
</tr></table>
<p style="margin:2px 0 0 0;font-family:{F_SANS};font-size:12px;line-height:18px;color:{MUTED};text-align:center;">Free 10-slide AI scaling playbook &middot; or reply and tell me which task is consuming the budget</p>
</td></tr>"""
    rows = topbar() + card_open(30) + hero \
        + row(f'<h1 class="h1" style="margin:0 0 18px 0;font-family:{F_SERIF};font-size:31px;line-height:38px;font-weight:normal;color:{INK};">{e(g["TITLE"])}</h1>' + P(f'<strong>{e(g["LEDE"])}</strong>', mb=22)) \
        + choices + row(P(GREETING)) + body_core(v, with_image=False) \
        + row(button(guide_url(v, "bottom"), "Get the free playbook&nbsp;&rarr;", full=True), pad="4px 36px 26px 36px") \
        + signature() + CARD_CLOSE
    return shell(g["TITLE"], "The four-step evaluation I would put in front of your leadership team.", rows)


for name, fn in (("variant-a-v2-offer-card.html", variant_a),
                 ("variant-b-v2-one-tap-poll.html", variant_b),
                 ("variant-c-v2-image-two-choices.html", variant_c)):
    open(os.path.join(OUT, name), "w").write(fn())
    print("wrote", name)
