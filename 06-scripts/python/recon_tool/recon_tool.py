"""
Herramienta básica de reconocimiento pasivo (DNS, WHOIS, IP intelligence).

Origen: material del curso de Ciberseguridad, Hybridge Education.
Uso académico. Requiere ping, dig, whois, curl en el PATH del sistema.
"""

import argparse
import subprocess
import platform
from urllib.parse import urlparse
from datetime import datetime
from pathlib import Path


class CommandRunner:

    def run(self, command, timeout=15):
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=timeout
            )

            return {
                "command": " ".join(command),
                "success": result.returncode == 0,
                "stdout": result.stdout.strip(),
                "stderr": result.stderr.strip(),
                "returncode": result.returncode
            }

        except subprocess.TimeoutExpired:
            return {
                "command": " ".join(command),
                "success": False,
                "stdout": "",
                "stderr": "Timeout expired",
                "returncode": -1
            }

        except Exception as error:
            return {
                "command": " ".join(command),
                "success": False,
                "stdout": "",
                "stderr": str(error),
                "returncode": -1
            }


class Target:

    def __init__(self, url):
        self.original_url = url
        self.domain = self.extract_domain(url)

    def extract_domain(self, url):
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url

        parsed_url = urlparse(url)
        return parsed_url.netloc

    def __str__(self):
        return self.domain


class PingScanner:

    def __init__(self, runner):
        self.runner = runner

    def scan(self, target):
        system = platform.system().lower()

        if system == "windows":
            command = ["ping", "-n", "1", target.domain]
        else:
            command = ["ping", "-c", "1", target.domain]

        return self.runner.run(command)


class DigScanner:

    def __init__(self, runner):
        self.runner = runner

    def scan(self, target):
        command = ["dig", "+short", target.domain]
        return self.runner.run(command)

    def extract_ips(self, dig_result):
        ips = []

        if not dig_result["stdout"]:
            return ips

        for line in dig_result["stdout"].splitlines():
            line = line.strip()

            if self.looks_like_ip(line):
                ips.append(line)

        return ips

    def looks_like_ip(self, value):
        parts = value.split(".")

        if len(parts) != 4:
            return False

        for part in parts:
            if not part.isdigit():
                return False

            number = int(part)

            if number < 0 or number > 255:
                return False

        return True


class WhoisScanner:

    def __init__(self, runner):
        self.runner = runner

    def scan(self, target):
        command = ["whois", target.domain]
        return self.runner.run(command, timeout=20)

    def scan_ip(self, ip):
        command = ["whois", ip]
        return self.runner.run(command, timeout=20)


class IPInfoScanner:

    def __init__(self, runner):
        self.runner = runner

    def scan(self, ip):
        url = f"https://ipinfo.io/{ip}"
        command = ["curl", "-s", url]
        return self.runner.run(command, timeout=15)


class MarkdownReport:

    def __init__(self, target):
        self.target = target
        self.sections = []

    def add_header(self):
        content = f"""# Reporte de reconocimiento

## Objetivo

- URL original: `{self.target.original_url}`
- Dominio analizado: `{self.target.domain}`
- Fecha de ejecucion: `{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}`

"""
        self.sections.append(content)

    def add_command_section(self, title, result):
        content = f"""## {title}

### Comando ejecutado

```bash
{result["command"]}
```

### Estado

- Exito: `{result["success"]}`
- Codigo de salida: `{result["returncode"]}`

### Salida

```text
{result["stdout"] if result["stdout"] else "Sin salida"}
```

"""

        if result["stderr"]:
            content += f"""### Errores

```text
{result["stderr"]}
```

"""

        self.sections.append(content)

    def add_ipinfo_section(self, ip, result):
        content = f"""## IP Info para `{ip}`

### Comando ejecutado

```bash
{result["command"]}
```

### Estado

- Exito: `{result["success"]}`
- Codigo de salida: `{result["returncode"]}`

### Salida

```json
{result["stdout"] if result["stdout"] else "Sin salida"}
```

"""

        if result["stderr"]:
            content += f"""### Errores

```text
{result["stderr"]}
```

"""

        self.sections.append(content)

    def save(self, output_path):
        report_content = "\n".join(self.sections)

        path = Path(output_path)
        path.write_text(report_content, encoding="utf-8")

        return path


class ReconTool:

    def __init__(self, url, output):
        self.target = Target(url)
        self.output = output
        self.runner = CommandRunner()

        self.ping_scanner = PingScanner(self.runner)
        self.dig_scanner = DigScanner(self.runner)
        self.whois_scanner = WhoisScanner(self.runner)
        self.ipinfo_scanner = IPInfoScanner(self.runner)

        self.report = MarkdownReport(self.target)

    def run(self):
        print(f"[+] Analizando objetivo: {self.target.domain}")

        self.report.add_header()

        print("[+] Ejecutando ping...")
        ping_result = self.ping_scanner.scan(self.target)
        self.report.add_command_section("Ping", ping_result)

        print("[+] Ejecutando dig +short...")
        dig_result = self.dig_scanner.scan(self.target)
        self.report.add_command_section("DNS - dig +short", dig_result)

        ips = self.dig_scanner.extract_ips(dig_result)

        print("[+] Ejecutando whois...")
        whois_result = self.whois_scanner.scan(self.target)
        self.report.add_command_section("WHOIS", whois_result)

        if ips:
            print(f"[+] IPs encontradas: {', '.join(ips)}")

            for ip in ips:
                print(f"[+] Ejecutando whois para {ip}...")
                whois_ip_result = self.whois_scanner.scan_ip(ip)
                self.report.add_command_section(f"WHOIS - {ip}", whois_ip_result)

                print(f"[+] Consultando ipinfo.io para {ip}...")
                ipinfo_result = self.ipinfo_scanner.scan(ip)
                self.report.add_ipinfo_section(ip, ipinfo_result)
        else:
            print("[!] No se encontraron IPs IPv4 directas con dig +short.")

        saved_path = self.report.save(self.output)

        print(f"[+] Reporte generado: {saved_path}")



def main():
    parser = argparse.ArgumentParser(
        description="Herramienta básica de reconocimiento pasivo con reporte Markdown"
    )
    parser.add_argument("-u", "--url", required=True,
                        help="URL o dominio objetivo. Ejemplo: https://example.com")
    parser.add_argument("-o", "--output", default="reporte.md",
                        help="Nombre del archivo de salida Markdown. Default: reporte.md")
    args = parser.parse_args()

    recon_tool = ReconTool(url=args.url, output=args.output)
    recon_tool.run()


if __name__ == "__main__":
    main()