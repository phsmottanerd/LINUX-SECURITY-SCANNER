from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math, textwrap

base = Path("/mnt/data/paulo_linux_soc_visual")
assets = base / "assets"
assets.mkdir(parents=True, exist_ok=True)

# ---------- Animated SVG ----------
svg = r'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img" aria-label="Paulo Henrique Santana Motta Linux SOC Cybersecurity Automation banner">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#050914"/><stop offset=".5" stop-color="#071525"/><stop offset="1" stop-color="#02050b"/>
  </linearGradient>
  <linearGradient id="chip" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#092d49"/><stop offset=".5" stop-color="#0b5c75"/><stop offset="1" stop-color="#08243b"/>
  </linearGradient>
  <filter id="glow">
    <feGaussianBlur stdDeviation="4" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0H0V40" fill="none" stroke="#12334a" stroke-width="1" opacity=".45"/>
  </pattern>
  <style>
    .title{font:700 31px 'DejaVu Sans',sans-serif;fill:#fff;letter-spacing:2px}
    .sub{font:600 16px 'DejaVu Sans',sans-serif;fill:#7ee7ff;letter-spacing:1px}
    .node{font:700 13px 'DejaVu Sans',sans-serif;fill:#fff;letter-spacing:1px}
    .small{font:500 11px 'DejaVu Sans',sans-serif;fill:#9bb8c8}
    .trace{fill:none;stroke:#22d3ee;stroke-width:3;stroke-linecap:round;stroke-dasharray:12 12;animation:flow 1.5s linear infinite}
    .trace2{fill:none;stroke:#39ff88;stroke-width:2;stroke-linecap:round;stroke-dasharray:8 12;animation:flow 1.2s linear infinite}
    .pulse{animation:pulse 1.4s ease-in-out infinite}
    @keyframes flow{to{stroke-dashoffset:-48}}
    @keyframes pulse{0%,100%{opacity:.35;transform:scale(.8)}50%{opacity:1;transform:scale(1.15)}}
  </style>
</defs>

<rect width="1200" height="520" rx="28" fill="url(#bg)"/>
<rect x="18" y="18" width="1164" height="484" rx="22" fill="url(#grid)" opacity=".7"/>
<rect x="30" y="30" width="1140" height="460" rx="18" fill="none" stroke="#1a536b" stroke-width="2"/>

<!-- moving circuit traces -->
<path class="trace" d="M65 105H245V150H315"/>
<path class="trace2" d="M65 410H235V365H315"/>
<path class="trace" d="M885 150H955V105H1135"/>
<path class="trace2" d="M885 365H970V410H1135"/>
<path class="trace2" d="M315 95V65H450"/>
<path class="trace" d="M885 95V65H750"/>
<path class="trace2" d="M315 425V455H450"/>
<path class="trace" d="M885 425V455H750"/>

<!-- left/right nodes -->
<g>
  <circle cx="65" cy="105" r="7" fill="#39ff88" filter="url(#glow)" class="pulse"/>
  <circle cx="65" cy="410" r="7" fill="#ffd43b" filter="url(#glow)" class="pulse"/>
  <circle cx="1135" cy="105" r="7" fill="#ff3b5c" filter="url(#glow)" class="pulse"/>
  <circle cx="1135" cy="410" r="7" fill="#39ff88" filter="url(#glow)" class="pulse"/>
</g>

<!-- CPU -->
<g transform="translate(315 90)">
  <rect x="0" y="0" width="570" height="340" rx="28" fill="#03101c" stroke="#20d8ff" stroke-width="3" filter="url(#glow)"/>
  <rect x="35" y="35" width="500" height="270" rx="20" fill="url(#chip)" stroke="#43e8ff" stroke-width="2"/>
  <!-- pins -->
  <g stroke="#39ff88" stroke-width="5" stroke-linecap="round">
    <path d="M55 0V-18M105 0V-28M155 0V-18M205 0V-28M255 0V-18M305 0V-28M355 0V-18M405 0V-28M455 0V-18M505 0V-28"/>
    <path d="M55 340V358M105 340V368M155 340V358M205 340V368M255 340V358M305 340V368M355 340V358M405 340V368M455 340V358M505 340V368"/>
  </g>

  <text x="285" y="82" text-anchor="middle" class="small">SYSTEM CORE</text>
  <text x="285" y="125" text-anchor="middle" class="title">LINUX • SOC • CYBER</text>
  <text x="285" y="151" text-anchor="middle" class="sub">AUTOMATION ENGINE</text>

  <!-- central processor -->
  <rect x="150" y="178" width="270" height="82" rx="12" fill="#04131f" stroke="#7ee7ff" stroke-width="2"/>
  <text x="285" y="207" text-anchor="middle" class="node">PAULO HENRIQUE</text>
  <text x="285" y="229" text-anchor="middle" class="small">SYSTEMS ENGINEERING</text>
  <text x="285" y="248" text-anchor="middle" class="small">SECURITY • MONITORING • AUTOMATION</text>

  <!-- LED row -->
  <g transform="translate(188 278)">
    <circle cx="0" cy="0" r="7" fill="#39ff88" filter="url(#glow)" class="pulse"/>
    <circle cx="45" cy="0" r="7" fill="#22d3ee" filter="url(#glow)" class="pulse"/>
    <circle cx="90" cy="0" r="7" fill="#ffd43b" filter="url(#glow)" class="pulse"/>
    <circle cx="135" cy="0" r="7" fill="#ff3b5c" filter="url(#glow)" class="pulse"/>
    <circle cx="180" cy="0" r="7" fill="#39ff88" filter="url(#glow)" class="pulse"/>
  </g>
</g>

<!-- module labels -->
<g>
  <rect x="72" y="155" width="180" height="55" rx="12" fill="#06121d" stroke="#39ff88"/>
  <text x="162" y="178" text-anchor="middle" class="node">LINUX SYSTEMS</text>
  <text x="162" y="197" text-anchor="middle" class="small">PROCESS • SYSTEMD • LOGS</text>

  <rect x="72" y="310" width="180" height="55" rx="12" fill="#06121d" stroke="#ffd43b"/>
  <text x="162" y="333" text-anchor="middle" class="node">NETWORK</text>
  <text x="162" y="352" text-anchor="middle" class="small">TCP/IP • DNS • DIAGNOSTICS</text>

  <rect x="948" y="155" width="180" height="55" rx="12" fill="#06121d" stroke="#ff3b5c"/>
  <text x="1038" y="178" text-anchor="middle" class="node">SOC OPERATIONS</text>
  <text x="1038" y="197" text-anchor="middle" class="small">DETECTION • EVENTS • RESPONSE</text>

  <rect x="948" y="310" width="180" height="55" rx="12" fill="#06121d" stroke="#39ff88"/>
  <text x="1038" y="333" text-anchor="middle" class="node">AUTOMATION</text>
  <text x="1038" y="352" text-anchor="middle" class="small">BASH • PYTHON • TOOLING</text>
</g>

<text x="600" y="477" text-anchor="middle" class="sub">ADMINISTRADOR LINUX  |  ANALISTA DE SISTEMAS  |  SOC ANALYST  |  CYBERSECURITY  |  AUTOMAÇÃO</text>
</svg>'''
(svg_path := assets / "paulo-linux-soc-banner.svg").write_text(svg, encoding="utf-8")

# ---------- GIF banner ----------
W, H = 1200, 520
frames = []
font_paths = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
]
bold = ImageFont.truetype(font_paths[0], 31)
normal = ImageFont.truetype(font_paths[1], 16)
small = ImageFont.truetype(font_paths[1], 13)

for f in range(36):
    im = Image.new("RGB", (W,H), (3,8,17))
    d = ImageDraw.Draw(im)
    # grid
    for x in range(20,W,40):
        d.line((x,20,x,H-20), fill=(12,36,53), width=1)
    for y in range(20,H,40):
        d.line((20,y,W-20,y), fill=(12,36,53), width=1)
    d.rounded_rectangle((30,30,W-30,H-30), radius=18, outline=(25,83,107), width=2)

    # flowing particles on traces
    offset = (f*16) % 240
    for base_y, color in [(105,(57,255,136)), (410,(34,211,238))]:
        for x in range(65-offset, 250, 48):
            if x >= 65:
                d.ellipse((x-4,base_y-4,x+4,base_y+4), fill=color)
    for base_y, color in [(105,(255,59,92)), (410,(57,255,136))]:
        for x in range(950+offset, 1140, 48):
            if x <= 1135:
                d.ellipse((x-4,base_y-4,x+4,base_y+4), fill=color)

    # CPU
    d.rounded_rectangle((315,90,885,430), radius=28, fill=(3,16,28), outline=(32,216,255), width=3)
    d.rounded_rectangle((350,125,850,395), radius=20, fill=(7,55,72), outline=(67,232,255), width=2)
    d.text((600,165), "SYSTEM CORE", font=small, fill=(155,184,200), anchor="mm")
    d.text((600,207), "LINUX • SOC • CYBER", font=bold, fill=(255,255,255), anchor="mm")
    d.text((600,238), "AUTOMATION ENGINE", font=normal, fill=(126,231,255), anchor="mm")
    d.rounded_rectangle((465,268,735,350), radius=12, fill=(4,19,31), outline=(126,231,255), width=2)
    d.text((600,292), "PAULO HENRIQUE", font=normal, fill=(255,255,255), anchor="mm")
    d.text((600,317), "SYSTEMS ENGINEERING", font=small, fill=(155,184,200), anchor="mm")
    # LED pulsing
    led_colors=[(57,255,136),(34,211,238),(255,212,59),(255,59,92),(57,255,136)]
    for i,c in enumerate(led_colors):
        r=5 + int(3*(1+math.sin((f+i)*0.45)))
        x=540+i*30
        d.ellipse((x-r,365-r,x+r,365+r), fill=c)
    # labels
    boxes=[
        (72,155,252,210,"LINUX SYSTEMS",(57,255,136),"PROCESS • SYSTEMD • LOGS"),
        (72,310,252,365,"NETWORK",(255,212,59),"TCP/IP • DNS • DIAGNOSTICS"),
        (948,155,1128,210,"SOC OPERATIONS",(255,59,92),"DETECTION • EVENTS • RESPONSE"),
        (948,310,1128,365,"AUTOMATION",(57,255,136),"BASH • PYTHON • TOOLING"),
    ]
    for x1,y1,x2,y2,t,c,s in boxes:
        d.rounded_rectangle((x1,y1,x2,y2), radius=12, fill=(6,18,29), outline=c, width=2)
        d.text(((x1+x2)//2,y1+21),t,font=small,fill=(255,255,255),anchor="mm")
        d.text(((x1+x2)//2,y1+41),s,font=ImageFont.truetype(font_paths[1],10),fill=(155,184,200),anchor="mm")
    footer="ADMINISTRADOR LINUX  |  ANALISTA DE SISTEMAS  |  SOC ANALYST  |  CYBERSECURITY  |  AUTOMAÇÃO"
    d.text((600,477),footer,font=ImageFont.truetype(font_paths[1],12),fill=(126,231,255),anchor="mm")
    frames.append(im)

gif_path = assets / "paulo-linux-soc-banner.gif"
frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=90, loop=0, optimize=True)

# ---------- README ----------
readme = r'''<div align="center">

<img src="assets/paulo-linux-soc-banner.svg" alt="Paulo Henrique Santana Motta - Linux SOC Cybersecurity Automation" width="100%">

<br>

<img src="assets/paulo-linux-soc-banner.gif" alt="Animated Linux SOC Cybersecurity Automation banner" width="100%">

</div>

# ⚡ Paulo Henrique Santana Motta

**Administrador Linux | Analista de Sistemas | SOC Analyst | Cybersecurity | Automação**

Este repositório reúne um laboratório prático voltado para **Linux, administração de sistemas, redes, monitoramento, segurança e automação**.

---

## 🧠 Arquitetura do laboratório

```text
                         ┌─────────────────────────┐
                         │       SYSTEM CORE        │
                         │                           │
                         │   LINUX • SOC • CYBER    │
                         │       AUTOMATION         │
                         └────────────┬──────────────┘
                                      │
              ┌───────────────────────┼───────────────────────┐
              │                       │                       │
              ▼                       ▼                       ▼
       ┌──────────────┐       ┌──────────────┐       ┌──────────────┐
       │ LINUX SYSTEM │       │ SOC / SECURITY│       │  AUTOMATION  │
       │              │       │              │       │              │
       │ processes    │       │ logs         │       │ Bash         │
       │ systemd      │       │ events       │       │ Python       │
       │ filesystem   │       │ monitoring   │       │ scripts      │
       │ networking   │       │ detection    │       │ tooling      │
       └──────────────┘       └──────────────┘       └──────────────┘




<div align="center">

# 🟦⚡ PAULO HENRIQUE SANTANA MOTTA ⚡🟦

### `Administrador Linux`  |  `Analista de Sistemas`  |  `SOC Analyst`

### `Cybersecurity`  |  `Automação`  |  `Linux Engineering`

<br>

```text
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║        ██████╗  █████╗ ██╗   ██╗██╗      ██████╗                  ║
║        ██╔══██╗██╔══██╗██║   ██║██║     ██╔═══██╗                 ║
║        ██████╔╝███████║██║   ██║██║     ██║   ██║                 ║
║        ██╔═══╝ ██╔══██║██║   ██║██║     ██║   ██║                 ║
║        ██║     ██║  ██║╚██████╔╝███████╗╚██████╔╝                 ║
║        ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝                  ║
║                                                                      ║
║                  LINUX • SECURITY • AUTOMATION                      ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

<br>

🟢━━━━━━━━━━━━━━━━━━━━━━━🟡━━━━━━━━━━━━━━━━━━━━━━━🔴
**SYSTEM INITIALIZATION**
🔴━━━━━━━━━━━━━━━━━━━━━━━🟡━━━━━━━━━━━━━━━━━━━━━━━🟢

</div>

---

# 🧠 SYSTEM CORE

```text
                         ┌──────────────────────┐
                         │     SYSTEM CORE      │
                         │                      │
                         │   LINUX ENGINEERING  │
                         │   CYBERSECURITY      │
                         │   AUTOMATION         │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                    ▼               ▼               ▼
             ┌────────────┐  ┌────────────┐  ┌────────────┐
             │   LINUX    │  │    SOC     │  │ AUTOMATION │
             │  SYSTEMS   │  │ SECURITY   │  │   TOOLS    │
             └─────┬──────┘  └─────┬──────┘  └─────┬──────┘
                   │               │               │
                   └───────────────┼───────────────┘
                                   ▼
                         ┌──────────────────┐
                         │   OPERATIONS     │
                         │   & MONITORING   │
                         └──────────────────┘
```

---

<div align="center">

## 🚦 SYSTEM STATUS

🟢 **LINUX**    🟢 **NETWORK**    🟢 **SECURITY**
🟢 **AUTOMATION**    🟡 **MONITORING**    🟢 **LAB ONLINE**

</div>

---

# ⚙️ PROCESSOR ARCHITECTURE

```text
                         ╔══════════════════════╗
                         ║      CPU CORE       ║
                         ║                      ║
                         ║   ████████████████   ║
                         ║   █  SYSTEM OPS  █   ║
                         ║   ████████████████   ║
                         ╚══════════╤═══════════╝
                                    │
             ┌──────────────────────┼──────────────────────┐
             │                      │                      │
             ▼                      ▼                      ▼

       ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
       │   PROCESS    │      │   NETWORK    │      │   SECURITY   │
       │   CONTROL    │      │   ANALYSIS   │      │   MONITORING │
       └──────┬───────┘      └──────┬───────┘      └──────┬───────┘
              │                     │                     │
              ▼                     ▼                     ▼
       🟢 Processes           🟢 TCP/IP              🟢 Logs
       🟢 Services            🟢 DNS                  🟢 Events
       🟢 Signals             🟢 Routing              🟢 Detection
       🟢 Resources           🟢 Interfaces           🟢 Response

             │                     │                     │
             └─────────────────────┼─────────────────────┘
                                   ▼
                         ╔════════════════════╗
                         ║  SECURITY ENGINE   ║
                         ║                    ║
                         ║  LINUX + SOC +    ║
                         ║  AUTOMATION        ║
                         ╚════════════════════╝
```

---

# 🔵 PROJECT OVERVIEW

Este laboratório representa uma **infraestrutura prática de estudos e engenharia de sistemas Linux**, construída para desenvolver conhecimentos aplicáveis a:

```text
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  🐧 LINUX ADMINISTRATION                                    │
│                                                             │
│  🖥️ SYSTEM ENGINEERING                                      │
│                                                             │
│  🛡️ CYBERSECURITY                                           │
│                                                             │
│  🚨 SOC OPERATIONS                                          │
│                                                             │
│  🌐 NETWORKING                                              │
│                                                             │
│  ⚙️ AUTOMATION                                              │
│                                                             │
│  🔎 TROUBLESHOOTING                                         │
│                                                             │
│  📊 MONITORING                                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

# 🔥 SYSTEM PIPELINE

```text
       ┌──────────┐
       │   USER   │
       └────┬─────┘
            │
            ▼
      ╭──────────────╮
      │   REQUEST    │
      ╰──────┬───────╯
             │
             ▼
       ┌───────────┐
       │   LINUX   │
       │   KERNEL  │
       └─────┬─────┘
             │
     ┌───────┼────────┐
     │       │        │
     ▼       ▼        ▼
  PROCESS  NETWORK   FILESYSTEM
     │       │        │
     └───────┼────────┘
             │
             ▼
      ┌──────────────┐
      │  MONITORING  │
      └──────┬───────┘
             │
             ▼
       ┌────────────┐
       │   LOGS     │
       └─────┬──────┘
             │
             ▼
       ┌────────────┐
       │   ALERT    │
       └─────┬──────┘
             │
             ▼
      ┌───────────────┐
      │ SOC ANALYSIS  │
      └───────┬───────┘
              │
              ▼
        🟢 RESPONSE
```

---

# 🟢 LINUX ENGINEERING

```text
                    ┌───────────────────┐
                    │    LINUX HOST     │
                    └─────────┬─────────┘
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
        ┌─────────┐      ┌─────────┐      ┌─────────┐
        │PROCESS  │      │ STORAGE │      │ NETWORK │
        └────┬────┘      └────┬────┘      └────┬────┘
             │                │                │
             ▼                ▼                ▼
        ps / top          df / du          ip / ss
        systemctl         mount            ping
        systemd           lsblk            DNS
        journalctl        filesystem       routing
```

---

# 🛡️ CYBERSECURITY PIPELINE

```text
             ┌───────────────────────┐
             │      ENVIRONMENT       │
             └───────────┬───────────┘
                         │
                         ▼
                  🔎 RECONNAISSANCE
                         │
                         ▼
                  🌐 NETWORK ANALYSIS
                         │
                         ▼
                  🧪 SECURITY TESTS
                         │
                         ▼
                  📜 LOG ANALYSIS
                         │
                         ▼
                  🚨 DETECTION
                         │
                         ▼
                  🛡️ RESPONSE
                         │
                         ▼
                  📊 REPORTING
```

---

# 🚦 SECURITY STATUS BOARD

```text
╔════════════════════════════════════════════════════════════╗
║                    SECURITY CONTROL                       ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║   🟢 SYSTEM        [ ONLINE ]                              ║
║                                                            ║
║   🟢 NETWORK       [ MONITORED ]                           ║
║                                                            ║
║   🟡 LOGGING       [ ANALYZING ]                           ║
║                                                            ║
║   🟢 SERVICES      [ RUNNING ]                            ║
║                                                            ║
║   🟢 AUTOMATION    [ ACTIVE ]                             ║
║                                                            ║
║   🔴 INCIDENT      [ 0 ACTIVE ]                           ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

---

# ⚡ AUTOMATION ENGINE

```text
             INPUT
               │
               ▼
       ┌───────────────┐
       │ SHELL SCRIPT  │
       └───────┬───────┘
               │
               ▼
       ┌───────────────┐
       │     PYTHON    │
       └───────┬───────┘
               │
               ▼
       ┌───────────────┐
       │ SYSTEM COMMAND │
       └───────┬───────┘
               │
               ▼
       ┌───────────────┐
       │   ANALYSIS    │
       └───────┬───────┘
               │
               ▼
       ┌───────────────┐
       │    REPORT     │
       └───────────────┘

     ⚡ AUTOMATE → ANALYZE → DETECT → RESPOND
```

---

# 🔬 LAB MODULES

| Módulo                | Área                             | Status |
| --------------------- | -------------------------------- | ------ |
| 🐧 Linux Systems      | Administração Linux              | 🟢     |
| ⚙️ Process Management | Processos e recursos             | 🟢     |
| 💾 Storage            | Filesystems e armazenamento      | 🟢     |
| 🌐 Networking         | TCP/IP, interfaces e diagnóstico | 🟢     |
| 📜 Logging            | journalctl / logs                | 🟢     |
| 🔧 systemd            | Serviços e inicialização         | 🟢     |
| 🛡️ Security          | Hardening e análise              | 🟢     |
| 🚨 SOC                | Detecção e monitoramento         | 🟡     |
| 🐍 Python             | Automação                        | 🟢     |
| 💻 Shell              | Automação Linux                  | 🟢     |
| 🔎 Troubleshooting    | Diagnóstico                      | 🟢     |

---

# 🧩 TECHNOLOGY STACK

```text
╔══════════════════════════════════════════════════════════╗
║                    TECHNOLOGY STACK                     ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  🐧 Linux                                                ║
║  🐚 Bash                                                 ║
║  🐍 Python                                               ║
║  🌐 TCP/IP                                               ║
║  🔐 Cybersecurity                                        ║
║  🚨 SOC Operations                                       ║
║  📊 Monitoring                                           ║
║  📝 System Logging                                       ║
║  ⚙️ systemd                                              ║
║  🐳 Docker                                               ║
║  🔎 Network Security                                     ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

---

# 🔴 TROUBLESHOOTING FLOW

```text
                  ┌──────────────┐
                  │    ALERT     │
                  └──────┬───────┘
                         │
                         ▼
                  🔎 IDENTIFY
                         │
                         ▼
                  📊 COLLECT
                         │
                         ▼
                  🧠 ANALYZE
                         │
                         ▼
                  🔧 CORRECT
                         │
                         ▼
                  🧪 VALIDATE
                         │
                         ▼
                  📝 DOCUMENT
                         │
                         ▼
                  🟢 RESOLVED
```

---

# 💻 TERMINAL IDENTITY

```bash
┌──[PAULO@LINUX-SOC]─[~/security-lab]
└─$ systemctl status security-monitor

● security-monitor.service
   Loaded: loaded
   Active: active (running)

[🟢] SYSTEM      ONLINE
[🟢] NETWORK     MONITORED
[🟢] LOGGING     ACTIVE
[🟢] SECURITY    ACTIVE
[🟢] AUTOMATION  ACTIVE

┌──[PAULO@LINUX-SOC]─[~/security-lab]
└─$ _
```

---

# 🧠 ENGINEERING MINDSET

```text
        OBSERVE
           │
           ▼
        ANALYZE
           │
           ▼
        UNDERSTAND
           │
           ▼
        AUTOMATE
           │
           ▼
        SECURE
           │
           ▼
        MONITOR
           │
           ▼
        IMPROVE
           │
           └───────────────► 🔄
```

---

# 📡 PROJECT OBJECTIVES

### 🟢 Administração Linux

* Processos e recursos
* Usuários e permissões
* Filesystems
* Serviços
* systemd
* Logs
* Networking
* Diagnóstico do sistema

### 🔵 Cybersecurity

* Segurança de sistemas Linux
* Network security
* Análise de logs
* Reconhecimento de ambientes
* Monitoramento
* Troubleshooting
* Hardening

### 🔴 SOC Operations

* Eventos de segurança
* Identificação de anomalias
* Análise de logs
* Investigação
* Monitoramento
* Resposta operacional

### 🟡 Automação

* Bash
* Python
* Scripts administrativos
* Coleta de informações
* Relatórios
* Rotinas automatizadas

---

# 🚀 ROADMAP

```text
                         PROJECT ROADMAP

             ┌───────────────┐
             │   LINUX CORE  │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │   NETWORKING  │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │  MONITORING   │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │ CYBERSECURITY │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │      SOC      │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │  AUTOMATION   │
             └───────┬───────┘
                     │
                     ▼
             ┌────────────────┐
             │   ENGINEERING  │
             └────────────────┘
```

---

<div align="center">

# ⚡ PAULO HENRIQUE SANTANA MOTTA ⚡

### `Administrador Linux`

### `Analista de Sistemas`

### `SOC Analyst`

### `Cybersecurity`

### `Automação`

<br>

🟢━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🟢

### 🐧 LINUX • 🛡️ SECURITY • 🚨 SOC • ⚙️ AUTOMATION

🟢━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🟢

```text
SYSTEM STATUS: OPERATIONAL
SECURITY STATUS: MONITORED
AUTOMATION STATUS: ACTIVE
```

<br>

**BUILD • ANALYZE • AUTOMATE • SECURE**

</div>
