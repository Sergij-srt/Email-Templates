"""Certified Renewables | Cold Outreach Campaign #2 for All, November 2026 | Templates 1-3 (A/B/C).

Body copy is verbatim from the brief (Certified_Renewables_3_Email_Campaign_1.pdf, email 1).
Only layout, CTA placement, images and the legal footer differ between variants.

    python3 build_v2.py   # writes the three HTML files next to this script
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

SUBJECT = "The Government says prepare for power cuts. Is your home ready?"
PREHEADER = "An emergency kit is a good start. What about keeping essential electricity running?"
BASE_URL = "https://certifiedrenewables.com/contact-renewable-energy-solutions-uk"
SITE = "https://certifiedrenewables.com/"

IMG_HOME = ("https://assets.zyrosite.com/cdn-cgi/image/format=jpeg,width=1040,height=650,fit=crop,"
            "gravity=0.5x0.55,quality=80,metadata=none/Yg2WVpRW9bsOE2Kk/20250127_093104-mP42BqO4kRSwa2rj.jpg")
IMG_BATTERY = ("https://assets.zyrosite.com/cdn-cgi/image/format=jpeg,width=560,height=700,fit=crop,"
               "gravity=0.47x0.62,quality=80,metadata=none/Yg2WVpRW9bsOE2Kk/"
               "whatsapp-image-2025-02-07-at-17.45.59-YbNqlqrwRLiQ7pGn.jpeg")


def link(variant, content):
    return (f"{BASE_URL}?utm_source=ghl&amp;utm_medium=email&amp;utm_campaign=crs_nov_all2"
            f"&amp;utm_content=t{variant}_{content}")


GREETING = "Hi {{contact.first_name}},"
LEAD = ("The Government has just encouraged UK households to prepare for disruptions to power "
        "and other everyday services. If your electricity went off tonight, what would still work in your home?")
P1 = ("Most of us think about torches, bottled water and charging our phones. But there is another question "
      "worth asking: could your home generate and store some of the electricity it needs?")
P2 = ("At Certified Renewables, we assess solar panels, battery storage and properly designed backup systems. "
      "With the right equipment, selected essential circuits can remain powered during an outage. "
      "Standard grid-connected solar panels alone cannot do this.")
P3 = ("Whether a disruption is caused by severe weather, an equipment failure or a cyber incident, "
      "it makes sense to know your options before it happens.")
P4_A = "Speak to one of our engineers"
P4_B = (" about what your home could realistically power, the battery capacity you might need and the cost of "
        "a suitable system. The consultation and quotation are free, with no obligation.")
P4 = P4_A + P4_B
CTA = "ASK AN ENGINEER ABOUT HOME BACKUP"
CTA_SUB = "Visit our free-quotation page and request a convenient time to speak with an engineer."

DARK, GREEN, GREEN_DK = "#173A2C", "#1F8A4F", "#17703F"   # GREEN on white: 4.6:1 contrast (AA)
TEXT, MUTED, LINE = "#262626", "#5E5E5E", "#DCE5DE"
FONT = "Arial, Helvetica, sans-serif"


def head(variant, bg):
    return f"""<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="x-apple-disable-message-reformatting">
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no, url=no">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>{SUBJECT}</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<style>
  :root {{ color-scheme: light; supported-color-schemes: light; }}
  body {{ margin:0 !important; padding:0 !important; width:100% !important; }}
  a[x-apple-data-detectors] {{ color:inherit !important; text-decoration:none !important; }}
  u + #body a {{ color:inherit; text-decoration:none; }}
  @media only screen and (max-width:620px) {{
    .container {{ width:100% !important; }}
    .px {{ padding-left:22px !important; padding-right:22px !important; }}
    .h1 {{ font-size:22px !important; line-height:30px !important; }}
    .fluid {{ width:100% !important; height:auto !important; }}
  }}
</style>
</head>
<body id="body" style="margin:0;padding:0;background-color:{bg};-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;">
<!-- Certified Renewables | Cold Outreach Campaign #2 for All Nov 2026 | Template {variant} -->
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;color:{bg};">{PREHEADER}{'&#8199;&#65279;&#847; ' * 30}</div>
"""


def open_wrap(bg):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{bg}" style="background-color:{bg};">'
            f'<tr><td align="center" style="padding:24px 10px;">\n'
            '<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->\n'
            '<table role="presentation" class="container" width="600" cellpadding="0" cellspacing="0" border="0" '
            'style="width:600px;max-width:600px;background-color:#ffffff;border-collapse:collapse;">\n')


def close_wrap():
    return ("</table>\n<!--[if mso]></td></tr></table><![endif]-->\n</td></tr></table>\n</body>\n</html>\n")


def p(text, size=16, color=TEXT, weight="normal", mb=16):
    lh = round(size * 1.55)
    return (f'<p style="margin:0 0 {mb}px 0;font-family:{FONT};font-size:{size}px;line-height:{lh}px;'
            f'color:{color};font-weight:{weight};">{text}</p>\n')


def button(url, radius=6):
    return f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;">
<tr><td align="center" bgcolor="{GREEN}" style="background-color:{GREEN};border-radius:{radius}px;border-bottom:3px solid {GREEN_DK};padding:0;">
<a href="{url}" target="_blank" style="display:block;padding:18px 16px;font-family:{FONT};font-size:17px;line-height:22px;font-weight:bold;letter-spacing:0.3px;color:#ffffff;text-decoration:none;border-radius:{radius}px;mso-line-height-rule:exactly;">{CTA}&nbsp;&rarr;</a>
</td></tr></table>
"""


def image(src, url, alt, w, h, radius=6):
    return (f'<a href="{url}" target="_blank" style="text-decoration:none;display:block;">'
            f'<img src="{src}" width="{w}" height="{h}" alt="{alt}" class="fluid" '
            f'style="display:block;width:{w}px;max-width:100%;height:auto;border:0;outline:none;text-decoration:none;'
            f'border-radius:{radius}px;font-family:{FONT};font-size:14px;color:{MUTED};"></a>')


def wordmark(size, on_dark=False):
    a, b = ("#ffffff", "#8EDDB0") if on_dark else (DARK, GREEN)
    return (f'<a href="{SITE}" target="_blank" style="text-decoration:none;font-family:{FONT};font-size:{size}px;'
            f'line-height:{round(size * 1.25)}px;font-weight:bold;letter-spacing:0.5px;">'
            f'<span style="color:{a};">CERTIFIED</span> <span style="color:{b};">RENEWABLES</span></a>')


def signoff():
    return p("Kind regards,", mb=4) + p("The Certified Renewables Team", color=DARK, weight="bold", mb=0)


def footer(bg="#ffffff"):
    return f"""<tr><td class="px" bgcolor="{bg}" style="background-color:{bg};padding:22px 40px 30px 40px;border-top:1px solid {LINE};">
<p style="margin:0 0 10px 0;font-family:{FONT};font-size:13px;line-height:21px;color:{MUTED};">
<a href="{SITE}" target="_blank" style="color:{GREEN};text-decoration:underline;font-size:14px;">www.certifiedrenewables.com</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="tel:+442037527044" style="color:{MUTED};text-decoration:none;">0203&nbsp;752&nbsp;7044</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="mailto:info@certifiedrenewables.com" style="color:{MUTED};text-decoration:none;">info@certifiedrenewables.com</a></p>
<p style="margin:0 0 10px 0;font-family:{FONT};font-size:12px;line-height:19px;color:{MUTED};">
Certified Renewable Solutions Ltd | Company No. 16087435<br>
Harrow Business Centre, 429-433 Pinner Road, Harrow, HA1 4HN</p>
<p style="margin:0;font-family:{FONT};font-size:12px;line-height:19px;color:{MUTED};">
This is a marketing email from Certified Renewable Solutions Ltd. To stop receiving marketing emails, <a href="{{{{email.unsubscribe_link}}}}" target="_blank" style="color:{MUTED};text-decoration:underline;">unsubscribe</a>.</p>
</td></tr>
"""


def body_paras(variant, inline_link=False, last_mb=16):
    p4 = (f'<a href="{link(variant, "inline")}" target="_blank" style="color:{GREEN};text-decoration:underline;font-weight:bold;">{P4_A}</a>{P4_B}'
          if inline_link else P4)
    return p(P1) + p(P2) + p(P3) + p(p4, mb=last_mb)


def wrap(variant, inner, bg):
    return head(variant, bg) + open_wrap(bg) + inner + close_wrap()


# ---- Template 1 (A): branded letter, house photo under the lead, one button after the copy ----
T1 = wrap("1 (A)", f"""<tr><td class="px" style="padding:30px 40px 14px 40px;">{wordmark(24)}</td></tr>
<tr><td class="px" style="padding:0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="{GREEN}" height="6" style="height:6px;font-size:0;line-height:0;background-color:{GREEN};">&nbsp;</td></tr></table></td></tr>
<tr><td class="px" style="padding:26px 40px 4px 40px;">
{p(GREETING)}<h1 class="h1" style="margin:0 0 20px 0;font-family:{FONT};font-size:21px;line-height:30px;color:{DARK};font-weight:bold;">{LEAD}</h1>
</td></tr>
<tr><td class="px" style="padding:0 40px 22px 40px;">{image(IMG_HOME, link("1", "photo"), "UK home with solar panels installed by Certified Renewables", 520, 325)}</td></tr>
<tr><td class="px" style="padding:0 40px 6px 40px;">
{body_paras("1")}</td></tr>
<tr><td class="px" style="padding:6px 40px 0 40px;">{button(link("1", "button"))}</td></tr>
<tr><td class="px" align="center" style="padding:12px 40px 26px 40px;">{p(CTA_SUB, size=14, color=MUTED, mb=0)}</td></tr>
<tr><td class="px" style="padding:0 40px 26px 40px;">{signoff()}</td></tr>
{footer()}""", bg="#EDF3EE")

# ---- Template 2 (B): dark hero with CTA above the fold, battery photo, CTA repeated ----
T2 = wrap("2 (B)", f"""<tr><td class="px" bgcolor="{DARK}" style="background-color:{DARK};padding:26px 40px 0 40px;">{wordmark(20, on_dark=True)}</td></tr>
<tr><td class="px" bgcolor="{DARK}" style="background-color:{DARK};padding:20px 40px 30px 40px;">
<h1 class="h1" style="margin:0 0 24px 0;font-family:{FONT};font-size:24px;line-height:33px;color:#ffffff;font-weight:bold;">{LEAD}</h1>
{button(link("2", "button_top"), radius=30)}
<p style="margin:12px 0 0 0;font-family:{FONT};font-size:14px;line-height:21px;color:#D3E6DA;text-align:center;">{CTA_SUB}</p>
</td></tr>
<tr><td bgcolor="{GREEN}" height="6" style="height:6px;font-size:0;line-height:0;background-color:{GREEN};">&nbsp;</td></tr>
<tr><td class="px" style="padding:30px 40px 4px 40px;">
{p(GREETING, weight="bold", color=DARK)}{p(P1)}{p(P2)}</td></tr>
<tr><td class="px" align="center" style="padding:4px 40px 22px 40px;">
<table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td bgcolor="#F0F6F1" style="background-color:#F0F6F1;padding:14px;border-radius:8px;">
{image(IMG_BATTERY, link("2", "photo"), "Home battery and inverter installed by Certified Renewables", 280, 350)}
</td></tr></table></td></tr>
<tr><td class="px" style="padding:0 40px 6px 40px;">{p(P3)}{p(P4)}</td></tr>
<tr><td class="px" style="padding:4px 40px 30px 40px;">{button(link("2", "button_bottom"), radius=30)}</td></tr>
<tr><td class="px" style="padding:0 40px 26px 40px;">{signoff()}</td></tr>
{footer(bg="#F5F9F6")}""", bg="#EDF3EE")

# ---- Template 3 (C): plain personal letter, no images, inline link + text CTA ----
T3 = wrap("3 (C)", f"""<tr><td class="px" style="padding:28px 40px 0 40px;border-top:4px solid {GREEN};">{wordmark(15)}</td></tr>
<tr><td class="px" style="padding:24px 40px 6px 40px;">
{p(GREETING)}
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 20px 0;"><tr>
<td width="4" bgcolor="{GREEN}" style="width:4px;background-color:{GREEN};font-size:0;line-height:0;">&nbsp;</td>
<td bgcolor="#F0F6F1" style="background-color:#F0F6F1;padding:16px 18px;">
<p style="margin:0;font-family:{FONT};font-size:17px;line-height:26px;color:{DARK};font-weight:bold;">{LEAD}</p>
</td></tr></table>
{body_paras("3", inline_link=True, last_mb=22)}<p style="margin:0 0 6px 0;font-family:{FONT};font-size:17px;line-height:26px;font-weight:bold;">
<a href="{link("3", "text_link")}" target="_blank" style="color:{GREEN};text-decoration:underline;">{CTA}&nbsp;&rarr;</a></p>
{p(CTA_SUB, size=14, color=MUTED, mb=26)}{signoff()}</td></tr>
<tr><td style="height:24px;font-size:0;line-height:0;">&nbsp;</td></tr>
{footer()}""", bg="#ffffff")

FILES = {
    "template-1-A.html": T1,
    "template-2-B.html": T2,
    "template-3-C.html": T3,
}

if __name__ == "__main__":
    for name, html in FILES.items():
        path = os.path.join(OUT, "cr_nov2026_all-2_" + name)
        with open(path, "w") as f:
            f.write(html)
        print(path, len(html.encode()), "bytes")
