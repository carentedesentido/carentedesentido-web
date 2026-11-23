# -*- coding: utf-8 -*-
# Genera /paulina/index.html y las versiones /en/, /fr/, /pt/ a partir de content.py
import os, sys, urllib.parse
sys.path.insert(0, os.path.dirname(__file__))
from content import T

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SITE = "https://carentedesentido.com.ar"
ORDER = ["es", "en", "fr", "pt"]

CSS = """*{box-sizing:border-box}
body{margin:0;background:#F5F4F0;color:#1E1F23;font-family:'Poppins',sans-serif;font-size:17px;line-height:1.6}
a{color:#1E1F23}a:hover{opacity:.88}
html{scroll-behavior:smooth}
img{max-width:100%;display:block}
a:focus-visible{outline:3px solid #E8A9C4;outline-offset:3px}
.wrap{max-width:1120px;margin:0 auto;padding:0 24px}
.eyebrow{margin:0 0 14px;font-size:14px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:#5A5B60}
.dark .eyebrow{color:#E8A9C4}
h2{margin:0;font-size:clamp(30px,3.6vw,46px);line-height:1.12;font-weight:700;letter-spacing:-1px}
h2 em{font-family:'Fraunces',serif;font-weight:400}
.sec{padding:96px 0}
.dark{background:#1E1F23;color:#F5F4F0}
.white{background:#FFFFFF}
.muted{color:#4A4B50}
.dark .muted{color:#D9D8D3}
.grid2{display:flex;flex-wrap:wrap;gap:40px 56px}
.grid2>*{flex:1 1 420px;min-width:0}
.cards{display:flex;flex-wrap:wrap;gap:20px}
.card{flex:1 1 300px;min-width:0;padding:30px;display:flex;flex-direction:column;gap:12px}
.card h3{margin:0;font-size:20px;font-weight:600;line-height:1.3}
.card p{margin:0}
.icon{width:52px;height:52px;background:#E8A9C4;color:#1E1F23;display:flex;align-items:center;justify-content:center}
.timeline{list-style:none;margin:0;padding:0;display:flex;flex-direction:column}
.timeline li{display:flex;gap:20px;padding:22px 0;border-top:1px solid #C9C7BF}
.timeline li:last-child{border-bottom:1px solid #C9C7BF}
.timeline .tag{flex:0 0 120px;font-size:13px;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:#5A5B60;padding-top:3px}
.timeline h3{margin:0 0 4px;font-size:19px;font-weight:600}
.timeline p{margin:0;font-size:15px;color:#4A4B50}
.btn{display:inline-flex;align-items:center;gap:10px;text-decoration:none;font-weight:600;padding:16px 26px;font-size:16px}
.btn.pink{background:#E8A9C4;color:#1E1F23}
.btn.line{border:1.5px solid currentColor;font-weight:500}
.langs{display:flex;gap:2px;font-size:13px;font-weight:600;letter-spacing:1px}
.langs a{color:#D9D8D3;text-decoration:none;padding:8px 9px;border:1px solid transparent}
.langs a[aria-current]{color:#1E1F23;background:#E8A9C4}
.num{font-family:'Fraunces',serif;font-style:italic;font-size:30px;line-height:1;color:#C9779C}
.dark .num{color:#E8A9C4}
.pitch{margin:0;padding:14px 0 14px 20px;border-left:3px solid #E8A9C4;font-family:'Fraunces',serif;font-style:italic;font-size:clamp(19px,2vw,23px);line-height:1.45;color:#F5F4F0;max-width:640px}
.chips{display:flex;flex-wrap:wrap;gap:10px}
.chips span{border:1px solid #C9C7BF;padding:8px 14px;font-size:15px;background:#fff}
.chips b{font-weight:600}
@media (max-width:600px){.timeline li{flex-direction:column;gap:4px}.timeline .tag{flex:none}.sec{padding:72px 0}}
"""

ICONS = [
    '<circle cx="12" cy="12" r="9"></circle><path d="M3 12h18"></path><path d="M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"></path>',
    '<path d="M3 18c3-6 6-6 9-6s6 0 9 6"></path><path d="M3 18h18"></path><path d="M7 12V8M17 12V8M12 12V6"></path>',
    '<circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="5"></circle><circle cx="12" cy="12" r="1"></circle>',
    '<rect x="3" y="4" width="18" height="17" rx="2"></rect><path d="M3 9h18M8 2v4M16 2v4M7 13h4M7 17h7"></path>',
]
SVG = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{}</svg>'
DL = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12M7 10l5 5 5-5M4 20h16"></path></svg>'
CV_ES = "/paulina/CV_Paulina_Cugini_ES.pdf"
CV_EN = "/paulina/CV_Paulina_Cugini_EN.pdf"


def page(code):
    t = T[code]
    ids = ["sobre-mi", "diplomacia-digital", "embajada", "trayectoria", "contacto"]
    nav = "".join(f'<a href="#{i}" style="color:#F5F4F0;text-decoration:none;padding:10px 0">{n}</a>' for i, n in zip(ids, t["nav"]))
    langs = "".join(
        f'<a href="{T[c]["path"]}" hreflang="{c}" lang="{c}"' + (' aria-current="page"' if c == code else "") + f'>{c.upper()}</a>'
        for c in ORDER)
    alts = "\n".join(f'<link rel="alternate" hreflang="{c}" href="{SITE}{T[c]["path"]}">' for c in ORDER)
    cv_main = CV_ES if code == "es" else CV_EN
    wa = "https://wa.me/5493425476902?text=" + urllib.parse.quote(t["wa_text"])

    view_cards = "".join(
        f'<div class="card" style="background:#27282D;border:1px solid #3A3B40"><h3>{h}</h3><p class="muted">{p}</p></div>'
        for h, p in t["view_cards"])
    dd_points = "".join(
        f'<div class="card white" style="flex-basis:300px"><span class="num">0{i+1}</span><h3>{h}</h3><p class="muted">{p}</p></div>'
        for i, (h, p) in enumerate(t["dd_points"]))
    case_stats = "".join(
        f'<div style="padding:clamp(18px,2.4vw,28px);display:flex;flex-direction:column;gap:8px;background:#1E1F23">'
        f'<span style="font-family:\'Fraunces\',serif;font-size:clamp(26px,3vw,38px);line-height:1.05;color:#E8A9C4">{a}</span>'
        f'<span style="font-size:14px;color:#D9D8D3">{b}</span></div>' for a, b in t["case_stats"])
    aporte = "".join(
        f'<div class="card" style="flex-basis:440px;background:#F5F4F0"><span class="icon" aria-hidden="true">{SVG.format(ICONS[i])}</span><h3>{h}</h3><p class="muted">{p}</p></div>'
        for i, (h, p) in enumerate(t["aporte_cards"]))
    emb = "".join(
        f'<div class="card" style="flex-basis:440px;background:#27282D;border:1px solid #3A3B40;flex-direction:row;gap:20px;align-items:flex-start">'
        f'<span class="num" style="flex:0 0 44px">{i+1:02d}</span><div style="display:flex;flex-direction:column;gap:8px"><h3>{h}</h3><p class="muted">{p}</p></div></div>'
        for i, (h, p) in enumerate(t["emb_items"]))
    stats = "".join(
        f'<div class="dark" style="padding:clamp(18px,2.6vw,32px);display:flex;flex-direction:column;gap:8px">'
        f'<span style="font-family:\'Fraunces\',serif;font-size:clamp(34px,4.4vw,56px);line-height:1;color:#E8A9C4">{a}</span>'
        f'<span style="font-size:15px;color:#D9D8D3">{b}</span></div>' for a, b in t["stats"])
    acts = "".join(
        f'<div class="card white" style="flex-basis:320px;padding:26px;border-top:3px solid #E8A9C4"><h3 style="font-size:18px">{h}</h3><p class="muted" style="font-size:15px">{p}</p></div>'
        for h, p in t["acts"])
    tl = "".join(f'<li><span class="tag">{a}</span><div><h3>{b}</h3><p>{c}</p></div></li>' for a, b, c in t["timeline"])
    chips = "".join(f'<span><b>{a}</b> · {b}</span>' for a, b in t["langs"])
    arts = "".join(
        f'<a href="https://carentedesentido.substack.com/p/{slug}" target="_blank" rel="noopener" lang="es" style="flex:1 1 380px;min-width:0;background:#F6F1E4;border:1px solid #1E1F23;padding:32px;text-decoration:none;display:flex;flex-direction:column;gap:12px">'
        f'<span lang="{code}" style="font-family:\'Poppins\',sans-serif;font-size:12px;letter-spacing:2px;text-transform:uppercase;color:#5A5B60">{tag}</span>'
        f'<span style="font-family:\'Fraunces\',serif;font-style:italic;font-weight:600;font-size:clamp(26px,2.6vw,34px);line-height:1.1">{title}</span>'
        f'<span lang="{code}" style="font-style:italic;color:#3A3B40">{sub}</span>'
        f'<span lang="{code}" style="font-family:\'Fraunces\',serif;font-style:italic;font-size:19px;margin-top:auto">{t["read"]}</span></a>'
        for slug, tag, title, sub in t["arts"])
    about_r = "".join(f'<p style="margin:0">{p}</p>' for p in t["about_r"])
    wr_note = f'<p style="margin:0;font-family:\'Poppins\',sans-serif;font-size:14px;color:#5A5B60">{t["wr_note"]}</p>' if t["wr_note"] else ""

    return f"""<!doctype html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<link rel="canonical" href="{SITE}{t['path']}">
{alts}
<link rel="alternate" hreflang="x-default" href="{SITE}/paulina/">
<meta property="og:type" content="profile">
<meta property="og:title" content="Paulina Cugini — {t['h1a']} {t['h1b']}">
<meta property="og:description" content="{t['eyebrow']}">
<meta property="og:url" content="{SITE}{t['path']}">
<meta property="og:image" content="{SITE}/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/img/favicon.png">
<link rel="apple-touch-icon" href="/img/favicon.png">
<meta name="theme-color" content="#1E1F23">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400;1,9..144,600&family=Lora:ital,wght@0,400;0,500;1,400;1,500&display=swap">
<!-- Generado con paulina/_build/build.py: editar los textos en content.py -->
<style>
{CSS}</style>
</head>
<body>

<header class="dark">
<div class="wrap" style="padding-top:14px;padding-bottom:14px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px">
<a href="#inicio" style="display:flex;align-items:center;gap:12px;text-decoration:none;color:#F5F4F0">
<img src="/img/logo.png" alt="" style="width:36px;height:36px;object-fit:contain">
<span style="font-weight:600;font-size:15px;letter-spacing:.4px">PAULINA CUGINI</span>
</a>
<div style="display:flex;flex-wrap:wrap;align-items:center;gap:8px 28px">
<nav aria-label="Principal" style="display:flex;flex-wrap:wrap;gap:4px 22px;font-size:14px">{nav}</nav>
<nav aria-label="Idioma / Language" class="langs">{langs}</nav>
</div>
</div>
</header>

<main>

<section id="inicio" class="dark">
<div class="wrap" style="padding-top:88px;padding-bottom:104px;display:flex;flex-wrap:wrap;align-items:center;gap:48px 64px">
<div style="flex:1 1 520px;min-width:0;display:flex;flex-direction:column;gap:26px">
<p class="eyebrow" style="margin:0">{t['eyebrow']}</p>
<h1 style="margin:0;font-size:clamp(42px,6.4vw,84px);line-height:1.02;font-weight:700;letter-spacing:-2px">{t['h1a']} <em style="font-family:'Fraunces',serif;font-weight:400;color:#E8A9C4">{t['h1b']}</em></h1>
<p style="margin:0;font-size:clamp(18px,2vw,21px);line-height:1.55;color:#D9D8D3;max-width:640px">{t['intro']}</p>
<div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:6px">
<a class="btn pink" href="#contacto">{t['b_contact']}</a>
<a class="btn line" href="{cv_main}" download style="color:#F5F4F0">{DL}{t['b_cv']}</a>
</div>
</div>
<div style="flex:0 1 360px;min-width:0;margin:0 auto">
<img src="/img/paulina.jpg" alt="{t['photo_alt']}" width="1080" height="1350" fetchpriority="high" style="aspect-ratio:4/5;width:100%;max-width:360px;height:auto;object-fit:cover;border:1.5px solid #E8A9C4">
</div>
</div>
</section>

<section id="sobre-mi" class="sec">
<div class="wrap grid2">
<div style="display:flex;flex-direction:column;gap:18px">
<p class="eyebrow">{t['about_eb']}</p>
<h2>{t['about_h2a']} <em>{t['about_h2b']}</em></h2>
<p class="muted" style="margin:0">{t['about_l']}</p>
</div>
<div style="display:flex;flex-direction:column;gap:18px">{about_r}</div>
</div>
</section>

<section aria-label="{t['view_eb']}" class="sec dark">
<div class="wrap" style="display:flex;flex-direction:column;gap:48px">
<div style="max-width:820px">
<p class="eyebrow">{t['view_eb']}</p>
<h2>{t['view_h2']}</h2>
</div>
<div class="cards">{view_cards}</div>
</div>
</section>

<section id="diplomacia-digital" class="sec">
<div class="wrap" style="display:flex;flex-direction:column;gap:48px">
<div class="grid2" style="align-items:flex-end">
<div>
<p class="eyebrow">{t['dd_eb']}</p>
<h2>{t['dd_h2a']} <em>{t['dd_h2b']}</em></h2>
</div>
<p class="muted" style="margin:0">{t['dd_lead']}</p>
</div>
<div class="cards">{dd_points}</div>
<div class="dark" style="padding:clamp(26px,4vw,52px);display:flex;flex-direction:column;gap:26px">
<div style="display:flex;flex-direction:column;gap:14px;max-width:820px">
<p class="eyebrow" style="margin:0">{t['case_eb']}</p>
<h3 style="margin:0;font-size:clamp(23px,2.6vw,32px);line-height:1.2;font-weight:600">{t['case_h3']}</h3>
<p class="muted" style="margin:0">{t['case_p']}</p>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:2px;background:#3A3B40;border:1px solid #3A3B40">{case_stats}</div>
<p style="margin:0;padding-left:18px;border-left:3px solid #E8A9C4;font-family:'Fraunces',serif;font-style:italic;font-size:clamp(18px,1.9vw,21px);line-height:1.5;max-width:820px">{t['case_note']}</p>
<p style="margin:0;font-size:13px;color:#9C9B97">{t['case_src']}</p>
</div>
</div>
</section>

<section id="aporte" class="sec white">
<div class="wrap" style="display:flex;flex-direction:column;gap:48px">
<div class="grid2" style="align-items:flex-end">
<div>
<p class="eyebrow">{t['aporte_eb']}</p>
<h2>{t['aporte_h2']}</h2>
</div>
<p class="muted" style="margin:0">{t['aporte_lead']}</p>
</div>
<div class="cards">{aporte}</div>
</div>
</section>

<section id="embajada" class="sec dark">
<div class="wrap" style="display:flex;flex-direction:column;gap:48px">
<div style="max-width:820px">
<p class="eyebrow">{t['emb_eb']}</p>
<h2>{t['emb_h2a']} <em>{t['emb_h2b']}</em></h2>
</div>
<div class="cards">{emb}</div>
</div>
</section>

<section id="trayectoria" class="sec white">
<div class="wrap" style="display:flex;flex-direction:column;gap:48px">
<div class="grid2" style="align-items:flex-end">
<div>
<p class="eyebrow">{t['exp_eb']}</p>
<h2>{t['exp_h2']}</h2>
</div>
<p class="muted" style="margin:0">{t['exp_lead']}</p>
</div>
<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:2px;background:#3A3B40">{stats}</div>
<div style="background:#F5F4F0;border-left:4px solid #E8A9C4;padding:clamp(22px,3vw,36px);display:flex;flex-direction:column;gap:10px">
<span style="font-size:13px;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;color:#5A5B60">{t['yd_tag']}</span>
<h3 style="margin:0;font-size:24px;font-weight:600">{t['yd_h3']}</h3>
<p class="muted" style="margin:0;max-width:820px">{t['yd_p']}</p>
</div>
<div class="grid2" style="align-items:center">
<div style="display:flex;flex-direction:column;gap:14px">
<h3 style="margin:0;font-size:24px;font-weight:600">{t['rec_h3']}</h3>
<p class="muted" style="margin:0">{t['rec_p']}</p>
<blockquote style="margin:6px 0 0;padding-left:18px;border-left:3px solid #E8A9C4;font-family:'Fraunces',serif;font-style:italic;font-size:19px;line-height:1.45">{t['rec_q']}<footer style="font-family:'Poppins',sans-serif;font-style:normal;font-size:14px;color:#5A5B60;margin-top:8px">{t['rec_who']}</footer></blockquote>
<p class="muted" style="margin:6px 0 0;font-size:15px">{t['refs']}</p>
</div>
<div style="display:flex;gap:16px;justify-content:center">
<img loading="lazy" src="/img/recanto-antes.jpg" alt="{t['img_before']}" style="width:44%;max-width:220px;height:auto;border:1px solid #E6E4DD">
<img loading="lazy" src="/img/recanto-despues.jpg" alt="{t['img_after']}" style="width:44%;max-width:220px;height:auto;border:1px solid #E6E4DD">
</div>
</div>
</div>
</section>

<section id="actividades" class="sec">
<div class="wrap" style="display:flex;flex-direction:column;gap:48px">
<div style="max-width:820px">
<p class="eyebrow">{t['act_eb']}</p>
<h2>{t['act_h2a']} <em>{t['act_h2b']}</em></h2>
</div>
<div class="cards">{acts}</div>
</div>
</section>

<section id="formacion" class="sec" style="padding-top:0">
<div class="wrap grid2">
<div style="display:flex;flex-direction:column;gap:18px">
<p class="eyebrow">{t['form_eb']}</p>
<h2>{t['form_h2a']} <em>{t['form_h2b']}</em></h2>
<p class="muted" style="margin:0">{t['form_lead']}</p>
<h3 style="margin:18px 0 0;font-size:19px;font-weight:600">{t['lang_h3']}</h3>
<div class="chips">{chips}</div>
</div>
<ul class="timeline">{tl}</ul>
</div>
</section>

<section id="cv" class="white" style="border-top:1px solid #E6E4DD">
<div class="wrap" style="padding-top:64px;padding-bottom:64px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:28px">
<div style="display:flex;flex-direction:column;gap:10px;flex:1 1 420px;min-width:0">
<p class="eyebrow" style="margin:0">{t['cv_eb']}</p>
<h2>{t['cv_h2']}</h2>
<p class="muted" style="margin:0">{t['cv_p']}</p>
</div>
<div style="display:flex;flex-wrap:wrap;gap:14px">
<a class="btn pink" href="{CV_ES}" download>{DL}{t['cv_es']}</a>
<a class="btn line" href="{CV_EN}" download>{DL}{t['cv_en']}</a>
</div>
</div>
</section>

<section id="escritos" style="background:#ECE5D3;font-family:'Lora',serif;border-top:6px double #1E1F23;border-bottom:6px double #1E1F23">
<div class="wrap" style="padding-top:88px;padding-bottom:88px;display:flex;flex-direction:column;gap:40px">
<div class="grid2" style="align-items:flex-end">
<div>
<p class="eyebrow" style="font-family:'Poppins',sans-serif">{t['wr_eb']}</p>
<h2 style="font-family:'Fraunces',serif;font-style:italic;font-weight:600">{t['wr_h2']}</h2>
</div>
<div style="display:flex;flex-direction:column;gap:10px"><p style="margin:0;font-style:italic;font-size:18px;line-height:1.7;color:#3A3B40">{t['wr_p']}</p>{wr_note}</div>
</div>
<div style="display:flex;flex-wrap:wrap;gap:24px">{arts}</div>
<a href="https://carentedesentido.substack.com/archive" target="_blank" rel="noopener" style="align-self:center;background:#1E1F23;color:#ECE5D3;font-family:'Fraunces',serif;font-style:italic;font-size:19px;text-decoration:none;padding:14px 28px">{t['all_arts']}</a>
</div>
</section>

<section id="contacto" class="sec dark">
<div class="wrap" style="display:flex;flex-direction:column;align-items:flex-start;gap:24px">
<h2 style="font-size:clamp(36px,5.4vw,68px);letter-spacing:-2px">{t['ct_h2']}</h2>
<p class="muted" style="margin:0;font-size:19px;max-width:640px">{t['ct_p']}</p>
<div style="display:flex;flex-wrap:wrap;gap:14px">
<a class="btn pink" href="https://www.linkedin.com/in/paulina-cugini-752393206/" target="_blank" rel="noopener"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2"></rect><path d="M8 10v7M8 7v.01M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"></path></svg>LinkedIn</a>
<a class="btn line" style="color:#F5F4F0" href="{wa}" target="_blank" rel="noopener">WhatsApp</a>
<a class="btn line" style="color:#F5F4F0" href="{cv_main}" download>{DL}CV</a>
<a class="btn line" style="color:#F5F4F0" href="/">{t['ct_cds']}</a>
</div>
</div>
</section>

</main>

<footer style="background:#141518;color:#B9B8B3;font-size:14px">
<div class="wrap" style="padding-top:32px;padding-bottom:32px;display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px">
<span style="color:#F5F4F0;font-weight:600;letter-spacing:.4px">PAULINA CUGINI</span>
<span>{t['foot']}</span>
</div>
</footer>

</body>
</html>
"""


for c in ORDER:
    out = os.path.join(ROOT, T[c]["path"].strip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(page(c))
    print("ok", out)
