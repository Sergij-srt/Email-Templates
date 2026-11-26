# Certified Renewables: аудит email і бази (26.11.2026)

Дані з HighLevel (location `2AXJ8oBA7rR8yz7j0Sg9`) і публічного DNS. Workflow API для цього акаунта закритий (403 `WORKFLOW_API_NOT_ENABLED_FOR_LOCATION`, тікет у підтримку подано), тому самі воркфлоу я не читав і не змінював.

## Цифри

| Показник | Значення |
|---|---|
| Контактів усього | 67,775 (з email: 66,974) |
| З тегом `dmcg` (імпорт 30.04.2025, корпоративні адреси) | 65,548 (97%) |
| Власні контакти CR (без `dmcg`) | 2,228 |
| Тег bounce (`hard bounced`, `hard bouced`, `invalid email/bounced`) | 1,341, **з них з Email DND: 0** |
| Тег валідатора `bad`, без тегу bounce | 1,290 |
| Тег `risky` / `good` | 33,533 / 22,862 |
| Email DND усього | 107 |
| Угоди: усього / open / won | 1,353 / 1,317 / 8 |

## Кампанії (статистика GHL)

| Кампанія | Надіслано | Open | Click | Replied | Bounce |
|---|---|---|---|---|---|
| #1 for All, Nov 2026 | 46,032 | 34.7% | 0.93% | 9 | 0.97% (438) |
| #1 for Openers, Nov 2026 | 16,006 | 40.5% | 0.71% | 8 | 0.76% |
| #1 for Non-Openers, Nov 2026 | 14,443 | 0.53% | 0.23% | 0 | 0.21% |
| #3 for Openers, Oct 2026 | 15,925 | 48.2% | 0.90% | 4 | 0.51% |
| #3 for Non-Openers, Oct 2026 | 15,716 | 1.83% | 0.27% | 1 | 0.33% |
| #1, Oct 2026 | 46,789 | 9.45% | 0.86% | 18 | 0.50% |

Open rate завищений Apple MPP і корпоративними сканерами (в AFM ~80% кліків — сканери), тому дивитися треба на відповіді й угоди.

## Знахідки

1. **Bounce не пригнічуються.** 1,341 контакт із тегом bounce без DND; 154 з них отримали #1 for All Nov, 57 «bad» теж. Bounce rate «for all» 0.97% — на межі 1%.
2. **Сегмент non-openers (~14.5k) мертвий:** 0.5–1.8% відкриттів за кожну кампанію. Регулярна відправка йому б'є по репутації домену.
3. **Частота:** у старих контактів по ~60 тегів кампаній за 15 місяців (~щотижня).
4. **Аудиторія ≠ оффер.** 97% бази — корпоративні адреси (`dmcg`, `c-level and business owners subscribers`, `head of marketing subscribers`), а листи про «your home». Поле country = GB у всіх 65,548 — проставлено імпортом, географію з нього не визначити.
5. **Угоди приходять не з email:** листопадові кошториси £7–20k — Which?, Google, call centre, Easy PV, рекомендації. Нові inbound-ліди (наприклад, Which? 17–20.11) автоматично потрапляють у масову «for all».
6. **Воронка не ведеться:** 1,317 з 1,353 угод «open», won лише 8, lost майже немає. Багато угод у «Estimate Sent» — найгарячіша аудиторія, окремого follow-up для неї немає.
7. **Битий лінк у старих шаблонах:** `certifiedrenewables.com/contact` → 404. Робоча сторінка: `/contact-renewable-energy-solutions-uk` (у шаблонах #3 Nov вже виправлено).
8. **Теги-дублікати:** `hard bounced` / `hard bouced`, `solar and battery` / `solar and batterty` / `solar pv and  battery`, `camp #1 foe all nov 2026` тощо.

## DNS / доставлюваність

| Домен | SPF | DKIM | DMARC | Інше |
|---|---|---|---|---|
| `send.certifiedflippa.com` (відправка, Mailgun) | ок (leadconnector + mailgun) | `k1`, **1024-bit** | `p=quarantine`, **без rua** | tracking CNAME ок |
| `certifiedflippa.com` | Hostinger | — | `p=quarantine`, без rua | **сайт — паркувальна сторінка Hostinger** |
| `certifiedrenewables.com` | Hostinger | — | `p=quarantine; rua/ruf=support@…` | **запис зіпсований:** перед `adkim=s` і `aspf=s` стоять символи `Â ` (NBSP), ці теги ігноруються |

## Що зробити

### Негайно (перед поточною розсилкою #2 for All)
- [ ] У фільтрі кампанії виключити теги: `hard bounced`, `hard bouced`, `invalid email/bounced`, `bad`.
- [ ] Не слати сегменту non-openers (тег `camp #1 for non-openers nov 2026` / ті, хто не відкривав 90+ днів).
- [ ] Контакти → фільтр за цими 4 тегами → Select all → Bulk action → DND → Email (2,631 контакт).

### Цього тижня
- [ ] Hostinger: `certifiedflippa.com` → 301 на `certifiedrenewables.com` замість parked page.
- [ ] DMARC з `rua` на `send.certifiedflippa.com` і `certifiedflippa.com`; виправити DMARC `certifiedrenewables.com` (прибрати NBSP).
- [ ] DKIM 2048-bit для `send.certifiedflippa.com` (Mailgun → rotate key).
- [ ] Виправити `/contact` у шаблонах, які ще використовуються.

### Коли відкриють Workflow API (або вручну в UI)
- [ ] `CR | Hygiene - Bounce suppression (2 strikes)` — як в AFM/DM.
- [ ] `CR | Validator bad/undeliverable → invalid email/bounced + Email DND`.
- [ ] `CR | Email - Customer replied → Pipeline + task`.
- [ ] Окремий nurture для власних лідів (2.2k) і для угод у «Estimate Sent»; не змішувати їх з `dmcg` cold.
- [ ] Sunset: хто не відкривав/не клікав 90 днів → пауза.
- [ ] Почистити воронку (won/lost) і дублікати тегів.
