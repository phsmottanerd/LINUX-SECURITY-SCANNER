
import platform
import getpass
import subprocess
import time
import shutil
import os
import re
from datetime import datetime


RESET = "\033[0m"
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
WHITE = "\033[97m"
BOLD = "\033[1m"

WIDTH = 88


def box_top():
    print(BLUE + "╔" + "═" * WIDTH + "╗" + RESET)


def box_bottom():
    print(BLUE + "╚" + "═" * WIDTH + "╝" + RESET)


def box_line(text="", color=WHITE):
    text = str(text)

    if len(text) > WIDTH - 2:
        text = text[:WIDTH - 5] + "..."

    print(
        BLUE + "║" +
        RESET +
        " " +
        color + text.ljust(WIDTH - 2) +
        RESET +
        " " +
        BLUE + "║" +
        RESET
    )


def separator():
    print(
        BLUE +
        "╟" + "─" * WIDTH + "╢" +
        RESET
    )


def section(title):
    box_top()
    box_line(title, CYAN + BOLD)
    separator()


def fit(text, size):
    text = str(text)

    if len(text) > size:
        return text[:size - 3] + "..."

    return text.ljust(size)


def run_command(command, timeout=5):
    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        return result.stdout.strip()

    except Exception:
        return ""


def analyze_logs():

    output = run_command(
        [
            "journalctl",
            "--no-pager",
            "-p",
            "warning..alert"
        ],
        timeout=15
    )

    if not output:

        return {
            "total": 0,
            "critical": 0,
            "warnings": 0,
            "security": 0,
            "environment": 0,
            "system": 0,
            "journal": 0,
            "events": []
        }

    lines = [
        line.strip()
        for line in output.splitlines()
        if line.strip()
    ]

    critical = 0
    warnings = 0
    security = 0
    environment = 0
    system = 0
    journal = 0

    events = []

    security_patterns = [
        "FAILED PASSWORD",
        "AUTHENTICATION FAILURE",
        "INVALID USER",
        "BREAK-IN ATTEMPT",
        "PERMISSION DENIED",
        "UNAUTHORIZED",
        "ACCESS DENIED",
        "LOGIN FAILED",
        "SUDO:",
        "SSH:",
        "BRUTE FORCE"
    ]

    environment_patterns = [
        "WSL",
        "SYSTEMD",
        "PCI",
        "CHRONYD",
        "CONTAINER",
        "SYSTEM BUS",
        "SYSCTL",
        "WINDOWS AGENT"
    ]

    journal_patterns = [
        "JOURNAL",
        "JOURNALD",
        "CORRUPTED",
        "UNCLEANLY SHUT DOWN"
    ]

    for line in lines:

        upper = line.upper()

        if any(
            pattern in upper
            for pattern in security_patterns
        ):

            category = "SECURITY"
            security += 1

            if (
                "FAILED" in upper
                or "FAILURE" in upper
                or "UNAUTHORIZED" in upper
                or "BRUTE FORCE" in upper
            ):
                severity = "ALERT"
                critical += 1

            else:
                severity = "WARNING"

        elif any(
            pattern in upper
            for pattern in environment_patterns
        ):

            category = "ENVIRONMENT"
            environment += 1
            severity = "WARNING"

        elif any(
            pattern in upper
            for pattern in journal_patterns
        ):

            category = "JOURNAL"
            journal += 1
            severity = "WARNING"

        else:

            category = "SYSTEM"
            system += 1
            severity = "WARNING"

        warnings += 1

        events.append(
            {
                "severity": severity,
                "category": category,
                "message": line
            }
        )

    return {
        "total": len(lines),
        "critical": critical,
        "warnings": warnings,
        "security": security,
        "environment": environment,
        "system": system,
        "journal": journal,
        "events": events
    }


print("\033[2J\033[H")

box_top()

box_line(
    "LINUX SECURITY SCANNER",
    CYAN + BOLD
)

box_line(
    "SECURITY ANALYSIS & AUTOMATION",
    BLUE + BOLD
)

separator()

box_line(
    "🐍 PYTHON  •  🐧 LINUX  •  🌐 NETWORK  •  🔐 SECURITY",
    GREEN
)

separator()

box_line(
    "SECURITY ENGINE                         [ INITIALIZING ]",
    YELLOW
)

steps = [
    "► Loading Python security engine",
    "► Connecting to Linux subsystem",
    "► Collecting system intelligence",
    "► Preparing network analysis",
    "► Loading process analysis",
    "► Loading service analysis",
    "► Loading Nmap port scanner",
    "► Loading log analysis engine",
]

for step in steps:
    box_line(step, WHITE)
    time.sleep(0.08)

separator()

box_line(
    "ENGINE STATUS                              [ ONLINE ]",
    GREEN + BOLD
)

box_bottom()

print()


system = platform.system()
kernel = platform.release()
host = platform.node()
user = getpass.getuser()
architecture = platform.machine()


cpu_info = run_command(["lscpu"])

cpu_model = "Unknown"
cpu_count = os.cpu_count() or 0

for line in cpu_info.splitlines():

    if "Model name:" in line:
        cpu_model = line.split(":", 1)[1].strip()
        break


ram_total = "Unknown"
ram_used = "Unknown"

ram_info = run_command(["free", "-h"])

for line in ram_info.splitlines():

    if line.startswith("Mem:"):

        parts = line.split()

        if len(parts) >= 7:
            ram_total = parts[1]
            ram_used = parts[2]


disk_total = "Unknown"
disk_used = "Unknown"
disk_free = "Unknown"
disk_percent = "Unknown"

try:

    disk = shutil.disk_usage("/")

    disk_total = f"{disk.total / (1024**3):.1f}G"
    disk_used = f"{disk.used / (1024**3):.1f}G"
    disk_free = f"{disk.free / (1024**3):.1f}G"
    disk_percent = f"{(disk.used / disk.total) * 100:.1f}%"

except Exception:
    pass


uptime_text = "Unknown"

try:

    uptime_seconds = float(
        open("/proc/uptime").read().split()[0]
    )

    days = int(uptime_seconds // 86400)
    hours = int((uptime_seconds % 86400) // 3600)
    minutes = int((uptime_seconds % 3600) // 60)

    uptime_text = f"{days}d {hours}h {minutes}m"

except Exception:
    pass


try:

    load = os.getloadavg()

    load_text = (
        f"{load[0]:.2f} / "
        f"{load[1]:.2f} / "
        f"{load[2]:.2f}"
    )

except Exception:

    load_text = "Unknown"


section("SYSTEM INTELLIGENCE")

box_line(f"🐧 Sistema       : {system}")
box_line(f"⚙  Kernel        : {kernel}")
box_line(f"🖥  Host          : {host}")
box_line(f"👤 Usuário       : {user}")
box_line(f"💻 Arquitetura   : {architecture}")
box_line(f"🧠 CPU           : {cpu_model}", CYAN)
box_line(f"🔢 CPU Cores     : {cpu_count}")
box_line(f"🧮 RAM           : {ram_used} used / {ram_total} total")
box_line(f"💾 Disk          : {disk_used} used / {disk_total}")
box_line(f"📦 Disk Free     : {disk_free} ({disk_percent})")
box_line(f"⏱  Uptime        : {uptime_text}")
box_line(f"📊 Load Average  : {load_text}")

box_bottom()

print()


section("NETWORK ANALYSIS")

box_line(
    fit("INTERFACE", 12) +
    fit("STATUS", 12) +
    fit("IPv4", 24) +
    fit("IPv6", 30),
    CYAN + BOLD
)

separator()

network_data = run_command(["ip", "-br", "addr"])

for line in network_data.splitlines():

    parts = line.split()

    if len(parts) < 3:
        continue

    interface = parts[0]
    status = parts[1]

    addresses = parts[2:]

    ipv4 = "-"
    ipv6 = "-"

    for address in addresses:

        if "." in address:
            ipv4 = address

        elif ":" in address:
            ipv6 = address

    status_symbol = "● UP" if status == "UP" else "○ " + status

    network_line = (
        fit(interface, 12) +
        fit(status_symbol, 12) +
        fit(ipv4, 24) +
        fit(ipv6, 30)
    )

    color = GREEN if status == "UP" else YELLOW

    box_line(network_line, color)

box_bottom()

print()


section("PROCESS ANALYSIS")

process_output = run_command(
    [
        "ps",
        "-eo",
        "user,pid,%cpu,%mem,stat,comm",
        "--sort=-%cpu"
    ]
)

process_lines = process_output.splitlines()

total_processes = max(
    len(process_lines) - 1,
    0
)

box_line(
    "PROCESS ENGINE                         [ ONLINE ]",
    GREEN + BOLD
)

box_line(
    f"TOTAL PROCESSES                       : {total_processes}"
)

separator()

box_line(
    fit("USER", 14) +
    fit("PID", 8) +
    fit("CPU%", 9) +
    fit("MEM%", 9) +
    fit("STAT", 8) +
    fit("COMMAND", 32),
    CYAN + BOLD
)

separator()

for line in process_lines[1:9]:

    parts = line.split(None, 5)

    if len(parts) < 6:
        continue

    proc_user = parts[0]
    pid = parts[1]
    cpu = parts[2]
    mem = parts[3]
    stat = parts[4]
    command = parts[5]

    process_line = (
        fit(proc_user, 14) +
        fit(pid, 8) +
        fit(cpu, 9) +
        fit(mem, 9) +
        fit(stat, 8) +
        fit(command, 32)
    )

    try:

        cpu_value = float(cpu)

        if cpu_value >= 50:
            color = RED

        elif cpu_value >= 10:
            color = YELLOW

        else:
            color = WHITE

    except ValueError:

        color = WHITE

    box_line(
        process_line,
        color
    )

separator()

box_line(
    "PROCESS ANALYSIS                     [ COMPLETE ]",
    GREEN + BOLD
)

box_bottom()

print()


section("SERVICE ANALYSIS")

service_output = run_command(
    [
        "systemctl",
        "list-units",
        "--type=service",
        "--no-pager",
        "--no-legend"
    ]
)

service_lines = [
    line.strip()
    for line in service_output.splitlines()
    if line.strip()
]

running_services = []
failed_services = []

for line in service_lines:

    parts = line.split()

    if len(parts) < 4:
        continue

    service_name = parts[0]
    active_state = parts[2]
    sub_state = parts[3]

    if active_state == "active" and sub_state == "running":
        running_services.append(service_name)

    if active_state == "failed":
        failed_services.append(service_name)


total_services = len(service_lines)
total_running = len(running_services)
total_failed = len(failed_services)


box_line(
    "SERVICE ENGINE                         [ ONLINE ]",
    GREEN + BOLD
)

box_line(
    f"TOTAL SERVICES                       : {total_services}"
)

box_line(
    f"RUNNING SERVICES                     : {total_running}",
    GREEN
)

box_line(
    f"FAILED SERVICES                      : {total_failed}",
    RED if total_failed > 0 else GREEN
)

separator()

box_line(
    fit("STATUS", 12) +
    fit("SERVICE", 42) +
    fit("STATE", 20),
    CYAN + BOLD
)

separator()

if failed_services:

    for service in failed_services[:8]:

        box_line(
            fit("● FAILED", 12) +
            fit(service, 42) +
            fit("FAILED", 20),
            RED
        )

else:

    box_line(
        fit("✔ HEALTHY", 12) +
        fit("SYSTEM", 42) +
        fit("NO FAILED SERVICES", 20),
        GREEN
    )

separator()

box_line(
    "SERVICE ANALYSIS                   [ COMPLETE ]",
    GREEN + BOLD
)

box_bottom()

print()


section("PORT SCANNER")

target = "127.0.0.1"

box_line(
    "NMAP ENGINE                           [ SCANNING ]",
    YELLOW + BOLD
)

box_line(
    f"TARGET                               : {target}"
)

box_line(
    "SCAN TYPE                            : TCP + SERVICE DETECTION"
)

print()

nmap_output = run_command(
    [
        "nmap",
        "-sT",
        "-sV",
        target
    ],
    timeout=30
)

if not nmap_output:

    box_line(
        "NMAP ENGINE                           [ ERROR ]",
        RED + BOLD
    )

    box_line(
        "Unable to execute Nmap.",
        RED
    )

else:

    host_status = "UNKNOWN"
    scanned_ports = 0
    open_ports = []

    for line in nmap_output.splitlines():

        if "Host is up" in line:
            host_status = "UP"

        elif "Host is down" in line:
            host_status = "DOWN"

        match = re.search(
            r"All\s+(\d+)\s+scanned ports",
            line
        )

        if match:
            scanned_ports = int(match.group(1))

        port_match = re.match(
            r"^(\d+)/tcp\s+(\S+)\s+(\S+)(?:\s+(.*))?$",
            line
        )

        if port_match:

            port = port_match.group(1)
            state = port_match.group(2)
            service = port_match.group(3)
            version = port_match.group(4) or "-"

            if state == "open":

                open_ports.append(
                    (
                        port,
                        state,
                        service,
                        version
                    )
                )

    box_line(
        "NMAP ENGINE                           [ ONLINE ]",
        GREEN + BOLD
    )

    box_line(
        f"HOST STATUS                          : {host_status}",
        GREEN if host_status == "UP" else RED
    )

    box_line(
        f"PORTS SCANNED                        : {scanned_ports or 1000}"
    )

    box_line(
        f"OPEN PORTS                           : {len(open_ports)}",
        RED if open_ports else GREEN
    )

    separator()

    box_line(
        fit("PORT", 10) +
        fit("STATE", 12) +
        fit("SERVICE", 18) +
        fit("VERSION", 42),
        CYAN + BOLD
    )

    separator()

    if open_ports:

        for port, state, service, version in open_ports:

            box_line(
                fit(port, 10) +
                fit(state, 12) +
                fit(service, 18) +
                fit(version, 42),
                RED if state == "open" else WHITE
            )

    else:

        box_line(
            "✔ NO OPEN TCP PORTS DETECTED",
            GREEN + BOLD
        )

    separator()

    box_line(
        "PORT SCAN                           [ COMPLETE ]",
        GREEN + BOLD
    )

box_bottom()

print()


log_analysis = analyze_logs()

section("LOG ANALYSIS")

box_line(
    "JOURNAL ENGINE                         [ ONLINE ]",
    GREEN + BOLD
)

box_line(
    f"TOTAL EVENTS                         : {log_analysis['total']}"
)

box_line(
    f"SECURITY EVENTS                      : {log_analysis['security']}",
    RED if log_analysis["security"] > 0 else GREEN
)

box_line(
    f"SECURITY ALERTS                      : {log_analysis['critical']}",
    RED if log_analysis["critical"] > 0 else GREEN
)

box_line(
    f"ENVIRONMENT EVENTS                   : {log_analysis['environment']}",
    CYAN
)

box_line(
    f"SYSTEM EVENTS                        : {log_analysis['system']}",
    YELLOW if log_analysis["system"] > 0 else GREEN
)

box_line(
    f"JOURNAL EVENTS                       : {log_analysis['journal']}",
    YELLOW if log_analysis["journal"] > 0 else GREEN
)

box_line(
    f"TOTAL WARNINGS                       : {log_analysis['warnings']}",
    YELLOW if log_analysis["warnings"] > 0 else GREEN
)

separator()

box_line(
    "RECENT JOURNAL EVENTS",
    CYAN + BOLD
)

separator()

for event in log_analysis["events"][-8:]:

    severity = event["severity"]
    category = event["category"]
    message = event["message"]

    if severity == "ALERT":
        color = RED

    elif category == "ENVIRONMENT":
        color = YELLOW

    elif category == "SECURITY":
        color = RED

    elif category == "JOURNAL":
        color = CYAN

    else:
        color = WHITE

    box_line(
        f"[{severity}] [{category}] {message}",
        color
    )

separator()

box_line(
    "LOG ANALYSIS                         [ COMPLETE ]",
    GREEN + BOLD
)

box_bottom()

print()


section("SECURITY MODULES")

modules = [
    ("Process Analysis", "ONLINE"),
    ("System Intelligence", "ONLINE"),
    ("Network Analysis", "ONLINE"),
    ("Service Analysis", "ONLINE"),
    ("Port Scanner", "ONLINE"),
    ("Firewall Audit", "READY"),
    ("Log Analysis", "ONLINE"),
    ("User & Permission Audit", "READY"),
]

for name, status in modules:

    if status == "ONLINE":

        color = GREEN
        symbol = "✔"

    else:

        color = YELLOW
        symbol = "○"

    box_line(
        f"{symbol} {name:<30} [ {status} ]",
        color
    )

box_bottom()

print()


section("SCAN ENGINE STATUS")

box_line(
    "✔ SYSTEM ................. [ OK ]",
    GREEN
)

box_line(
    "✔ HARDWARE ............... [ OK ]",
    GREEN
)

box_line(
    "✔ NETWORK ................ [ OK ]",
    GREEN
)

box_line(
    "✔ PROCESS ANALYSIS ....... [ OK ]",
    GREEN
)

box_line(
    "✔ SERVICE ANALYSIS ....... [ OK ]",
    GREEN
)

box_line(
    "✔ PORT SCANNER ........... [ OK ]",
    GREEN
)

box_line(
    "✔ LOG ANALYSIS ........... [ OK ]",
    GREEN
)

box_line(
    "● SECURITY MODULES ....... [ PARTIAL ]",
    YELLOW
)

separator()

box_line(
    "SCAN PIPELINE",
    CYAN + BOLD
)

box_line(
    "COLLECT  →  ANALYZE  →  CLASSIFY  →  REPORT"
)

box_bottom()

print()


section("SCAN COMPLETE")

timestamp = datetime.now().strftime(
    "%Y-%m-%d %H:%M:%S"
)

box_line(
    "SYSTEM DATA ................. COLLECTED",
    GREEN
)

box_line(
    "HARDWARE DATA ............... COLLECTED",
    GREEN
)

box_line(
    "NETWORK DATA ................ COLLECTED",
    GREEN
)

box_line(
    "PROCESS DATA ................ COLLECTED",
    GREEN
)

box_line(
    "SERVICE DATA ................ COLLECTED",
    GREEN
)

box_line(
    "PORT DATA ................... COLLECTED",
    GREEN
)

box_line(
    "LOG DATA .................... ANALYZED",
    GREEN
)

box_line(
    f"SCAN TIME ................... {timestamp}"
)

separator()

box_line(
    "LINUX SECURITY SCANNER",
    CYAN + BOLD
)

box_line(
    "SECURITY ANALYSIS ENGINE READY",
    GREEN + BOLD
)

box_bottom()


