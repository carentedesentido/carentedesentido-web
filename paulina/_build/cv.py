# -*- coding: utf-8 -*-
# Genera los CV en PDF (ES y EN):  python3 paulina/_build/cv.py
import os
from playwright.sync_api import sync_playwright

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOGO = "file://" + os.path.join(ROOT, "img", "logo.png")

CV = {
"es": dict(
    role="Relaciones Internacionales · Comunicación internacional · Estrategia digital",
    contact_h="Contacto", web="Web", phone="WhatsApp",
    profile_h="Perfil",
    profile="Estudiante avanzada de Relaciones Internacionales (UNR) y especialista en marketing digital. Fundadora de la agencia Carente de Sentido. Cruzo la lectura del sistema internacional con la comunicación estratégica para que cada mensaje tenga contexto. Me interesa acercar la diplomacia a las nuevas generaciones y a la ciudadanía a través de las redes.",
    goal="Busco sumarme a equipos de comunicación de representaciones argentinas en el exterior o de Cancillería.",
    exp_h="Experiencia",
    exp=[
        ("Fundadora y directora", "Carente de Sentido · Agencia de comunicación", [
            "Gestión de 12 cuentas de Instagram como Community Manager, Social Media Manager, especialista en Paid Media y Project Manager.",
            "Campañas para lanzar productos, viajes y carreras; gestión de proyectos de personas con reconocimiento público en redes.",
            "Caso Recanto Turismo: de 11.641 a 28.559 seguidores (+145%) e interacciones ×12; hoy es la agencia de turismo más seguida de Santa Fe.",
            "Redacción de artículos de divulgación en Gaceta de Sentido y LinkedIn.",
        ]),
        ("Voluntaria · Área de comunicación", "Youth Diplomats (parte de Kairos)", [
            "Guiones, grabación y edición de reels sobre diplomacia y relaciones internacionales para público joven.",
        ]),
    ],
    edu_h="Formación",
    edu=[
        ("Licenciatura en Relaciones Internacionales", "Estudiante avanzada · Fac. de Ciencia Política y RR. II., Universidad Nacional de Rosario"),
        ("Diplomatura en Comunicación Política", "Fac. de Ciencia Política y RR. II., Universidad Nacional de Rosario"),
        ("Curso de Paid Media", "Universidad de Buenos Aires"),
        ("Marketing Digital, Social Media y Community Management", "Coderhouse"),
        ("Bachiller en Economía y Administración", "Educación secundaria"),
    ],
    act_h="Actividades y participación",
    acts=["Modelo de Naciones Unidas", "Congreso de Política Exterior · UNSAM", "Congreso de la Democracia · UNR", "Observatorio de Política Exterior · 2022", "Eventos académicos de Relaciones Internacionales"],
    lang_h="Idiomas",
    langs=[("Español", "Nativo"), ("Inglés", "Avanzado"), ("Portugués", "Básico"), ("Francés", "Básico")],
    skills_h="Habilidades",
    skills=["Comunicación estratégica", "Gestión de redes sociales", "Guion y edición de video", "Campañas pagas (Paid Media)", "Medición y reportes", "Gestión de proyectos", "Redacción"],
    refs="Referencias disponibles a pedido.",
    loc="Santa Fe, Argentina", loc_h="Ubicación",
),
"en": dict(
    role="International Relations · International communication · Digital strategy",
    contact_h="Contact", web="Web", phone="WhatsApp",
    profile_h="Profile",
    profile="Advanced International Relations student (National University of Rosario, Argentina) and digital marketing specialist. Founder of the communication agency Carente de Sentido. I combine an understanding of the international system with strategic communication, so that every message has context. I'm committed to bringing diplomacy closer to new generations and to citizens through social media.",
    goal="I'm looking to join the communication teams of Argentina's missions abroad or of the Ministry of Foreign Affairs.",
    exp_h="Experience",
    exp=[
        ("Founder and Director", "Carente de Sentido · Communication agency", [
            "Management of 12 Instagram accounts as Community Manager, Social Media Manager, Paid Media specialist and Project Manager.",
            "Campaigns to launch products, trips and degree programmes; project management for public figures on social media.",
            "Recanto Turismo case: from 11,641 to 28,559 followers (+145%) and 12× engagement; now the most-followed travel agency in Santa Fe.",
            "Explanatory articles published on Gaceta de Sentido and LinkedIn.",
        ]),
        ("Volunteer · Communication team", "Youth Diplomats (part of Kairos)", [
            "Scripting, filming and editing reels on diplomacy and international relations for young audiences.",
        ]),
    ],
    edu_h="Education",
    edu=[
        ("B.A. in International Relations", "Advanced student · School of Political Science and IR, National University of Rosario"),
        ("Diploma in Political Communication", "School of Political Science and IR, National University of Rosario"),
        ("Paid Media course", "University of Buenos Aires"),
        ("Digital Marketing, Social Media and Community Management", "Coderhouse"),
        ("High school diploma in Economics and Business Administration", ""),
    ],
    act_h="Activities and involvement",
    acts=["Model United Nations", "Foreign Policy Congress · UNSAM", "Congress on Democracy · UNR", "Foreign Policy Observatory · 2022", "Academic events in International Relations"],
    lang_h="Languages",
    langs=[("Spanish", "Native"), ("English", "Advanced"), ("Portuguese", "Basic"), ("French", "Basic")],
    skills_h="Skills",
    skills=["Strategic communication", "Social media management", "Video scripting and editing", "Paid campaigns (Paid Media)", "Analytics and reporting", "Project management", "Writing"],
    refs="References available on request.",
    loc="Santa Fe, Argentina", loc_h="Location",
),
}


def html(c):
    exp = "".join(
        f'<div class="item"><div class="ih">{a}</div><div class="is">{b}</div><ul>' + "".join(f"<li>{x}</li>" for x in li) + "</ul></div>"
        for a, b, li in c["exp"])
    edu = "".join(f'<div class="item"><div class="ih">{a}</div>' + (f'<div class="is">{b}</div>' if b else "") + "</div>" for a, b in c["edu"])
    acts = "".join(f"<li>{a}</li>" for a in c["acts"])
    langs = "".join(f'<div class="kv"><b>{a}</b><span>{b}</span></div>' for a, b in c["langs"])
    skills = "".join(f"<li>{s}</li>" for s in c["skills"])
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Fraunces:ital,opsz,wght@0,9..144,400;1,9..144,400&display=swap">
<style>
@page{{size:A4;margin:0}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:'Poppins',sans-serif;color:#1E1F23;font-size:9pt;line-height:1.4;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:210mm;height:296mm;overflow:hidden;display:flex;flex-direction:column}}
.top{{background:#1E1F23;color:#F5F4F0;padding:10mm 15mm 8mm;display:flex;gap:9mm;align-items:center}}
.top img{{width:17mm;height:17mm;object-fit:contain}}
h1{{margin:0;font-size:25pt;letter-spacing:-.5pt;line-height:1.05}}
h1 em{{font-family:'Fraunces','Lora',serif;font-weight:400;color:#E8A9C4}}
.role{{margin-top:2mm;font-size:8.6pt;letter-spacing:1.2pt;text-transform:uppercase;color:#E8A9C4;font-weight:600}}
.goal{{background:#E8A9C4;padding:3.2mm 15mm;font-family:'Fraunces','Lora',serif;font-style:italic;font-size:11pt}}
.cols{{display:flex;flex:1}}
.side{{width:66mm;background:#F5F4F0;padding:8mm 7mm 8mm 15mm}}
.main{{flex:1;padding:8mm 15mm 8mm 9mm}}
h2{{margin:0 0 2.6mm;font-size:8.6pt;letter-spacing:1.6pt;text-transform:uppercase;color:#5A5B60;border-bottom:1.2pt solid #E8A9C4;padding-bottom:1.2mm}}
.block{{margin-bottom:5mm}}
.item{{margin-bottom:2.4mm}}
.ih{{font-weight:600;font-size:10pt}}
.is{{color:#5A5B60;font-size:8.8pt}}
ul{{margin:1.4mm 0 0;padding-left:4mm}} li{{margin-bottom:1mm}}
.side ul{{padding-left:3.6mm}}
.kv{{display:flex;justify-content:space-between;margin-bottom:1.2mm}} .kv span{{color:#5A5B60}}
.ct div{{margin-bottom:1.8mm}} .ct b{{display:block;font-size:7.8pt;letter-spacing:1pt;text-transform:uppercase;color:#5A5B60;font-weight:600}}
.ct a{{color:#1E1F23;text-decoration:none;font-size:8pt;overflow-wrap:anywhere}}
.two{{columns:2;column-gap:6mm}}
.refs{{font-size:8.6pt;color:#5A5B60;font-style:italic}}
</style></head><body><div class="page">
<div class="top"><img src="{LOGO}"><div><h1>Paulina <em>Cugini</em></h1><div class="role">{c['role']}</div></div></div>
<div class="goal">{c['goal']}</div>
<div class="cols">
<div class="side">
<div class="block ct"><h2>{c['contact_h']}</h2>
<div><b>LinkedIn</b><a href="https://www.linkedin.com/in/paulina-cugini-752393206/">linkedin.com/in/paulina-cugini-752393206</a></div>
<div><b>{c['phone']}</b><a href="https://wa.me/5493425476902">+54 9 342 547-6902</a></div>
<div><b>{c['web']}</b><a href="https://carentedesentido.com.ar/paulina/">carentedesentido.com.ar/paulina</a></div>
<div><b>{c['loc_h']}</b>{c['loc']}</div></div>
<div class="block"><h2>{c['lang_h']}</h2>{langs}</div>
<div class="block"><h2>{c['skills_h']}</h2><ul>{skills}</ul></div>
<div class="refs">{c['refs']}</div>
</div>
<div class="main">
<div class="block"><h2>{c['profile_h']}</h2><div>{c['profile']}</div></div>
<div class="block"><h2>{c['exp_h']}</h2>{exp}</div>
<div class="block"><h2>{c['edu_h']}</h2>{edu}</div>
<div class="block"><h2>{c['act_h']}</h2><ul class="two">{acts}</ul></div>
</div></div></div></body></html>"""


with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    for code, c in CV.items():
        tmp = os.path.join(os.path.dirname(__file__), f"_cv_{code}.html")
        open(tmp, "w", encoding="utf-8").write(html(c))
        pg.goto("file://" + tmp)
        pg.wait_for_timeout(1500)
        out = os.path.join(ROOT, "paulina", f"CV_Paulina_Cugini_{code.upper()}.pdf")
        pg.pdf(path=out, format="A4", print_background=True, margin=dict(top="0", bottom="0", left="0", right="0"))
        os.remove(tmp)
        print("ok", out)
    b.close()
