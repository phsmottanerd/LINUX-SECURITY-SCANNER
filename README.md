
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math, random, textwrap


from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math, random, textwrap

base = Path("/mnt/data/linux-cybersecurity-systems-lab")
assets = base / "assets"
assets.mkdir(parents=True, exist_ok=True)

readme = r'''<div align="center">

<img src="assets/linux-cybersecurity-banner.svg" alt="Linux Cybersecurity Systems Lab" width="100%">

# 🐧 Linux Cybersecurity Systems Lab

### `Administrador Linux` · `Analista de Sistemas` · `SOC Analyst` · `Cybersecurity` · `Automação`

[![Linux](https://img.shields.io/badge/Linux-Engineering-111827?style=for-the-badge&logo=linux&logoColor=white)](#)
[![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Operations-111827?style=for-the-badge&logo=protonvpn&logoColor=white)](#)
[![SOC](https://img.shields.io/badge/SOC-Analyst-111827?style=for-the-badge&logo=securityscorecard&logoColor=white)](#)
[![Python](https://img.shields.io/badge/Python-Automation-111827?style=for-the-badge&logo=python&logoColor=white)](#)
[![Bash](https://img.shields.io/badge/Bash-Scripting-111827?style=for-the-badge&logo=gnubash&logoColor=white)](#)

</div>

---

## ⚡ SYSTEM INITIALIZATION

```text
╔══════════════════════════════════════════════════════════════════════╗
║                 PAULO HENRIQUE SANTANA MOTTA                        ║
║                                                                      ║
║   ADMINISTRADOR LINUX  •  ANALISTA DE SISTEMAS  •  SOC ANALYST      ║
║   CYBERSECURITY  •  AUTOMATION  •  LINUX SYSTEMS ENGINEERING         ║
║                                                                      ║
║   [ONLINE] LINUX      [MONITORED] NETWORK      [ACTIVE] SECURITY    ║
║   [ACTIVE] AUTOMATION [ANALYZING] LOGGING      [READY] RESPONSE     ║
╚══════════════════════════════════════════════════════════════════════╝


<img width="1200" height="190" alt="security-module (1)" src="https://github.com/user-attachments/assets/015a710b-a1a2-4980-acf1-85806e0dd481" />
# 🔐 LINUX SECURITY SCANNER

<div align="center">

## 🟦 `SECURITY ANALYSIS` • 🟨 `AUTOMATION` • 🟥 `LINUX` • 🟩 `PYTHON`

### **Paulo Henrique Santana Motta**

**Linux • Python • Cybersecurity • Security Automation**

---

```text
╔══════════════════════════════════════════════════════════════════════╗
║                  LINUX SECURITY SCANNER                             ║
║              SECURITY ANALYSIS & AUTOMATION                         ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║   🐍 PYTHON        🐧 LINUX        🌐 NETWORK        🔐 SECURITY     ║
║                                                                      ║
║   COLLECT  →  ANALYZE  →  CLASSIFY  →  REPORT                       ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

</div>

---

## 🟦 `01` • SOBRE O PROJETO

O **Linux Security Scanner** é uma ferramenta de **automação de segurança desenvolvida em Python**, criada para coletar informações do ambiente Linux, analisar componentes do sistema e apresentar os resultados em um relatório visual diretamente no terminal.

O projeto foi desenvolvido com foco em uma situação real:

> **automatizar tarefas de coleta e análise que normalmente exigiriam a execução manual de diversos comandos Linux.**

A ferramenta combina **Python + comandos Linux + Nmap + análise de logs**, transformando dados técnicos do sistema em uma visão organizada para análise de segurança.

---

## 🟥 `02` • OBJETIVO

O objetivo do projeto é criar uma base de **Security Automation** capaz de:

```text
┌──────────────────────────────────────────────────────────────┐
│ 🟦 COLLECT                                                   │
│    Coletar informações do sistema                           │
├──────────────────────────────────────────────────────────────┤
│ 🟨 ANALYZE                                                   │
│    Analisar processos, serviços, rede e portas              │
├──────────────────────────────────────────────────────────────┤
│ 🟥 CLASSIFY                                                  │
│    Classificar eventos e informações de logs                │
├──────────────────────────────────────────────────────────────┤
│ 🟩 REPORT                                                    │
│    Apresentar os resultados de forma organizada             │
└──────────────────────────────────────────────────────────────┘
```

---

## 🟨 `03` • PRINCIPAIS MÓDULOS

### 🧠 SYSTEM INTELLIGENCE

Coleta informações fundamentais do ambiente:

* Sistema operacional
* Kernel
* Host
* Usuário
* Arquitetura
* CPU
* Número de cores
* Memória RAM
* Armazenamento
* Espaço livre
* Uptime
* Load Average

---

### 🌐 NETWORK ANALYSIS

Realiza análise das interfaces de rede disponíveis.

Informações coletadas:

* Interfaces
* Estado da interface
* IPv4
* IPv6
* Status operacional

Exemplo:

```text
INTERFACE   STATUS      IPv4
lo          UNKNOWN     127.0.0.1/8
eth0        UP          172.22.20.62/20
```

---

### ⚙️ PROCESS ANALYSIS

Analisa os processos em execução no Linux.

A ferramenta identifica:

* Usuário
* PID
* Consumo de CPU
* Consumo de memória
* Estado do processo
* Nome do processo

Também permite destacar processos com maior utilização de CPU.

---

### 🟩 SERVICE ANALYSIS

Analisa os serviços gerenciados pelo `systemd`.

A ferramenta apresenta:

* Total de serviços
* Serviços em execução
* Serviços com falha
* Estado geral dos serviços

Exemplo:

```text
TOTAL SERVICES       : 31
RUNNING SERVICES     : 13
FAILED SERVICES      : 0
```

---

### 🔎 NMAP PORT SCANNER

Integra o **Nmap diretamente ao Python**.

O scanner realiza:

```text
TARGET
   │
   ▼
127.0.0.1
   │
   ▼
TCP PORT SCAN
   │
   ▼
SERVICE DETECTION
   │
   ▼
PORT ANALYSIS
```

Informações analisadas:

* Status do host
* Portas examinadas
* Portas abertas
* Serviços
* Detecção de versão

---

### 📋 LOG ANALYSIS

Analisa eventos provenientes do `journalctl`.

Em vez de simplesmente contar todos os erros como problemas de segurança, o projeto utiliza **classificação contextual**.

Os eventos são separados em categorias como:

```text
🔐 SECURITY
🌐 ENVIRONMENT
⚙️ SYSTEM
📋 JOURNAL
```

Isso permite diferenciar eventos relacionados ao ambiente WSL/Linux de possíveis eventos de segurança.

---

## 🟦 `04` • ARQUITETURA

```text
                    ┌──────────────────────┐
                    │   LINUX ENVIRONMENT  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       PYTHON         │
                    │   SECURITY ENGINE    │
                    └──────────┬───────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
          ▼                    ▼                    ▼
     SYSTEM DATA          NETWORK DATA         LOG DATA
          │                    │                    │
          └────────────────────┼────────────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       ANALYSIS       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    CLASSIFICATION    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   TERMINAL REPORT    │
                    └──────────────────────┘
```

---

## 🟥 `05` • PIPELINE DE SEGURANÇA

```text
╔══════════╗
║ COLLECT  ║
╚════╤═════╝
     │
     ▼
╔══════════╗
║ ANALYZE  ║
╚════╤═════╝
     │
     ▼
╔══════════╗
║ CLASSIFY ║
╚════╤═════╝
     │
     ▼
╔══════════╗
║  REPORT  ║
╚══════════╝
```

### 🔵 COLLECT

Coleta informações diretamente do Linux.

### 🟡 ANALYZE

Processa os dados coletados.

### 🔴 CLASSIFY

Organiza eventos e informações por contexto.

### 🟢 REPORT

Exibe os resultados em uma interface de terminal estruturada.

---

## 🟨 `06` • TECNOLOGIAS

<div align="center">

| Tecnologia               | Utilização                    |
| ------------------------ | ----------------------------- |
| 🐍 **Python**            | Engine de automação           |
| 🐧 **Linux**             | Ambiente de execução          |
| 🖥️ **WSL2**             | Ambiente Linux no Windows     |
| 🔎 **Nmap**              | Análise de portas e serviços  |
| ⚙️ **systemd**           | Análise de serviços           |
| 📋 **journalctl**        | Análise de logs               |
| 🌐 **Linux Networking**  | Informações de rede           |
| 🧠 **Python Subprocess** | Integração com comandos Linux |

</div>

---

## 🟦 `07` • AMBIENTE DE EXECUÇÃO

```text
HOST
│
└── Windows
     │
     └── WSL2
          │
          └── Ubuntu
               │
               ├── Python 3
               ├── Nmap
               ├── systemd
               ├── journalctl
               └── Linux Security Scanner
```

### Ambiente utilizado

```text
Operating System : Ubuntu
Environment      : WSL2
Architecture     : x86_64
Python           : Python 3
Scanner          : Linux Security Scanner
Network Tool     : Nmap
```

---

## 🟩 `08` • EXECUÇÃO

Entre no diretório do projeto:

```bash
cd "/mnt/c/Users/Henrique/Desktop/Linux Security Scanner"
```

Execute:

```bash
python3 security_scanner.py
```

---

## 🟥 `09` • EXEMPLO DE RESULTADO

```text
╔════════════════════════════════════════════════════════════════════════╗
║ SYSTEM INTELLIGENCE                                                   ║
╟────────────────────────────────────────────────────────────────────────╢
║ Sistema       : Linux                                                 ║
║ Kernel        : 6.18.33.2-microsoft-standard-WSL2                    ║
║ Host          : DESKTOP-G5MHT19                                       ║
║ Arquitetura   : x86_64                                                ║
║ CPU Cores     : 4                                                     ║
║ RAM           : 462Mi used / 3.8Gi total                              ║
║ Disk          : 4.4G used / 1006.9G                                  ║
╚════════════════════════════════════════════════════════════════════════╝
```

```text
╔════════════════════════════════════════════════════════════════════════╗
║ PORT SCANNER                                                           ║
╟────────────────────────────────────────────────────────────────────────╢
║ NMAP ENGINE        [ ONLINE ]                                         ║
║ HOST STATUS        : UP                                               ║
║ PORTS SCANNED      : 1000                                             ║
║ OPEN PORTS         : 0                                                ║
╟────────────────────────────────────────────────────────────────────────╢
║ ✔ NO OPEN TCP PORTS DETECTED                                         ║
╚════════════════════════════════════════════════════════════════════════╝
```

---

## 🟨 `10` • STATUS DOS MÓDULOS

```text
╔══════════════════════════════════════════════════════════════════════╗
║                         SECURITY MODULES                            ║
╟──────────────────────────────────────────────────────────────────────╢
║ ✔ Process Analysis               [ ONLINE ]                         ║
║ ✔ System Intelligence            [ ONLINE ]                         ║
║ ✔ Network Analysis               [ ONLINE ]                         ║
║ ✔ Service Analysis               [ ONLINE ]                         ║
║ ✔ Port Scanner                   [ ONLINE ]                         ║
║ ✔ Log Analysis                   [ ONLINE ]                         ║
║ ○ Firewall Audit                 [ READY ]                          ║
║ ○ User & Permission Audit        [ READY ]                          ║
╚══════════════════════════════════════════════════════════════════════╝
```

### 🚧 Próximas evoluções

```text
V1  ████████████████████  SYSTEM SCANNER
V2  ████████████████████  NETWORK & PORTS
V3  ████████████████████  PROCESS & SERVICES
V4  ████████████████████  LOG CLASSIFICATION
V5  ░░░░░░░░░░░░░░░░░░░░  FIREWALL AUDIT
V6  ░░░░░░░░░░░░░░░░░░░░  USER & PERMISSION AUDIT
V7  ░░░░░░░░░░░░░░░░░░░░  JSON REPORT
V8  ░░░░░░░░░░░░░░░░░░░░  SOC INTEGRATION
```

---

## 🟦 `11` • EVOLUÇÃO FUTURA

O projeto foi estruturado para evoluir de um scanner local para uma ferramenta de **Security Automation** mais completa.

```text
LINUX SECURITY SCANNER
          │
          ▼
   SECURITY DATA
          │
          ▼
       JSON
          │
          ▼
   SECURITY EVENTS
          │
          ▼
   CYBER FORTRESS SOC
```

Possíveis evoluções:

* Firewall Audit
* User & Permission Audit
* Detecção de configurações suspeitas
* Relatórios em TXT
* Relatórios em JSON
* Histórico de scans
* Comparação entre scans
* Alertas
* Integração com SOC
* Automação de resposta

---

## 🟥 `12` • OBJETIVO PROFISSIONAL

Este projeto faz parte de uma linha prática de estudos envolvendo:

```text
🐧 LINUX
   │
   ├── System Administration
   │
   ├── Networking
   │
   ├── Troubleshooting
   │
   └── Security
          │
          ▼
🐍 PYTHON
   │
   ├── Automation
   ├── Data Collection
   ├── Process Execution
   └── Security Tools
          │
          ▼
🔐 CYBERSECURITY
   │
   ├── Reconnaissance
   ├── Analysis
   ├── Classification
   └── Security Operations
```

---

## 🟨 `13` • DESENVOLVEDOR

<div align="center">

# 🟦 PAULO HENRIQUE SANTANA MOTTA

### 🐧 Linux • 🐍 Python • 🔐 Cybersecurity • ⚙️ Automation

**Security Automation • Linux Systems • Cybersecurity Labs**

</div>

---

<div align="center">

```text
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║                  LINUX SECURITY SCANNER                             ║
║                                                                      ║
║              SECURITY ANALYSIS ENGINE                               ║
║                                                                      ║
║                    [ V1.0 ONLINE ]                                  ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

### 🟢 `COLLECT` → 🟡 `ANALYZE` → 🔴 `CLASSIFY` → 🔵 `REPORT`

**Built with Python • Linux • Automation • Security**

</div>
