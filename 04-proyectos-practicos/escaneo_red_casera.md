# 🏠 Auditoría de Red Doméstica — Reporte de Hallazgos

> **Nota de privacidad:** las direcciones IP y MAC en este documento están sanitizadas
> usando rangos reservados para documentación: **RFC 5737** (IPv4 documentation) y
> **RFC 7042** (MAC documentation, bloque `00:00:5E:00:53:XX`). Los hallazgos describen
> patrones reales encontrados en mi propia red doméstica, redactados para publicación responsable.

---

## 🎯 Objetivo

Identificar dispositivos conectados a la red doméstica, evaluar postura de seguridad y proponer remediaciones aplicables a un entorno SOHO (Small Office / Home Office).

## 🛠️ Herramientas utilizadas

- **Nmap** 7.94 — host discovery, port scanning
- **Wireshark** 4.x — validación de tráfico
- **Kali Linux 2024.x** — estación de auditoría

## 📋 Metodología

Aplicada según fase de **Intelligence Gathering** del PTES *(Penetration Testing Execution Standard)* y técnica **T1046** *(Network Service Discovery)* de MITRE ATT&CK.

### Paso 1 — Identificación de la red local

```bash
ip addr show
# Interfaz activa: wlan0
# IP local: 192.0.2.100/24      ← RFC 5737 (rango documentación)
# Gateway:  192.0.2.1
```

### Paso 2 — Host discovery (sweep ARP)

```bash
# -sn = no port scan, sólo descubrimiento
sudo nmap -sn 192.0.2.0/24 -oN scan_discovery.txt
```

> 💡 En LAN, `nmap -sn` usa **ARP requests** por defecto — más rápido y silencioso que ICMP, porque ARP no se filtra dentro del segmento Layer 2.

### Paso 3 — Service enumeration en hosts identificados

```bash
# -sV = service version detection
# -O  = OS fingerprinting
# --top-ports 100 = puertos más comunes (balance velocidad/cobertura)
sudo nmap -sV -O --top-ports 100 192.0.2.50 -oN scan_services_smarttv.txt
```

---

## 📊 Resultados (sanitizados)

| IP (RFC 5737) | MAC (RFC 7042) | Tipo de dispositivo |
|---|---|---|
| 192.0.2.1   | 00:00:5E:00:53:01 | Router / Gateway |
| 192.0.2.50  | 00:00:5E:00:53:02 | Smart TV |
| 192.0.2.100 | 00:00:5E:00:53:03 | Estación de auditoría (laptop) |
| 192.0.2.105 | 00:00:5E:00:53:04 | Smartphone |
| 192.0.2.120 | 00:00:5E:00:53:05 | Dispositivo IoT (asistente de voz) |

---

## ⚠️ Hallazgos de seguridad

### Hallazgo 1 — Router con credenciales por defecto
- **Severidad:** Alta (CVSS estimado: 8.8)
- **Descripción:** panel de administración accesible con credenciales de fábrica.
- **CWE:** CWE-798 — *Use of Hard-coded Credentials*.
- **Referencia:** OWASP IoT Top 10 — I1: *Weak, Guessable, or Hardcoded Passwords*.

### Hallazgo 2 — Telnet (puerto 23) abierto en Smart TV
- **Severidad:** Media (CVSS estimado: 6.5)
- **Descripción:** Servicio Telnet activo. Telnet transmite en texto claro (no cifra credenciales ni payload).
- **CWE:** CWE-319 — *Cleartext Transmission of Sensitive Information*.
- **MITRE ATT&CK:** T1040 (*Network Sniffing*) sería trivial frente a este servicio.

### Hallazgo 3 — Ausencia de segmentación de red
- **Severidad:** Media (CVSS estimado: 5.4)
- **Descripción:** todos los dispositivos (incluyendo IoT y de uso personal) en el mismo *broadcast domain*.
- **Implicación:** un dispositivo IoT comprometido tiene visibilidad de red completa sobre dispositivos críticos. Violación del principio de **least privilege** a nivel de red. Antítesis del modelo Zero Trust.

---

## ✅ Recomendaciones priorizadas

| # | Acción | Esfuerzo | Impacto |
|---|---|---|---|
| 1 | Cambiar contraseña del router por una de ≥16 caracteres con generador | Bajo | Alto |
| 2 | Deshabilitar Telnet en Smart TV; usar SSH si se requiere mgmt remoto | Bajo | Alto |
| 3 | Configurar VLAN o red de invitados separada para dispositivos IoT | Medio | Alto |
| 4 | Habilitar WPA3 (o WPA2-AES si WPA3 no disponible) | Bajo | Medio |
| 5 | Actualizar firmware del router a última versión estable | Bajo | Medio |
| 6 | Deshabilitar UPnP en router (vector común de exposición no intencional) | Bajo | Medio |

---

## 🧠 Lecciones técnicas

- **ARP discovery es Layer 2:** rápido y silencioso dentro de la LAN, pero invisible más allá del primer router. No funciona para descubrir hosts en otra subred.
- **La segmentación de red no es opcional** en redes con dispositivos IoT. El principio aplicado proviene del modelo **Zero Trust** ("never trust, always verify"), incluso dentro de la red doméstica.
- **Default credentials siguen siendo el #1 vector de compromiso de IoT** según múltiples reportes (ej. Shodan, Censys, OWASP IoT Top 10). No es un problema "viejo" — es un problema **persistente**.

---

*Trabajo realizado en mi propia red bajo principios de hacking ético. Datos sanitizados para publicación responsable según RFC 5737 y RFC 7042.*

*Fecha: Mayo 2026*