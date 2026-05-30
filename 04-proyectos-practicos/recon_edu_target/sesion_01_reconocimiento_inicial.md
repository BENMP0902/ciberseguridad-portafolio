# Sesión 01 — Reconocimiento inicial: target educativo

**Fecha:** Mayo 2026
**Curso:** Ciberseguridad (universitario)
**Autor:** benmp (`BENMP0902`)
**Target oficial:** `http://www.target-edu.example`
**Duración efectiva:** sesión corta — principalmente setup y reconocimiento ICMP.

> 🛡️ **Nota de sanitización:** las direcciones IP, hostnames y nombres de dominio en este documento han sido sanitizados usando **RFC 5737** (IPv4 documentation: `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`) y **RFC 2606** (`.example` reservado para documentación). La metodología, comandos y análisis técnico son fieles al ejercicio real realizado bajo contexto académico.

---

## 1. Objetivo de la práctica

Documentado en `~/proyectos/ciberseguridad/proyecto_0`:

> Para esta práctica estaremos buscando servicios y tecnologías vulnerables en la página oficial del target educativo.
>
> Objetivo: `http://www.target-edu.example`

Esta sesión cubre **únicamente la fase de preparación + recon ICMP básico**. Las herramientas planificadas para la clase (`nmap`, `whatweb`) **no se ejecutaron** y quedan pendientes para la siguiente sesión.

---

## 2. Entorno de trabajo

Setup en paralelo sobre dos plataformas Kali para comparación de rendimiento:

| Plataforma           | Rol                          | Shell           |
|----------------------|------------------------------|-----------------|
| Kali en WSL (Win 11) | Terminal superior            | Zsh             |
| Kali en VirtualBox   | Terminal inferior            | Bash (default)  |

**Por qué importa la comparación:** WSL2 comparte kernel con Windows y usa networking NAT del host; la VM tiene kernel aislado y NIC virtualizada por VirtualBox. Esa diferencia se vuelve relevante cuando entren `nmap -sS` (raw sockets), `openvpn` (TUN device) y captura con Wireshark — el rendimiento y los privilegios cambian entre ambos entornos.

---

## 3. Estructura de directorios

```bash
mkdir ciberseguridad           # Crea el directorio de trabajo del curso
cd ciberseguridad              # Entra al directorio recién creado
touch proyecto_0               # Crea archivo vacío (timestamp + inode, sin contenido)
nano proyecto_0                # Editor para escribir el objetivo de la práctica
ls -la                         # Lista contenido con detalles + ocultos
```

Explicación de banderas:

- `mkdir <dir>`: crea directorio. Sin `-p`, falla si el padre no existe.
- `cd`: change directory, builtin del shell.
- `touch <file>`: crea archivo vacío si no existe; si existe, actualiza `atime`/`mtime`. Útil como placeholder antes de editar.
- `nano <file>`: editor de texto interactivo. Ctrl+O escribe, Ctrl+X sale.
- `ls -l`: formato largo (permisos, owner, size, fecha). `-a`: incluye archivos ocultos (`.` y `..`). `-la` combina ambas.

**Resultado verificado:**

```
drwxr-xr-x benmp benmp 4.0 KB  .
drwxrwx--- root  devs  4.0 KB  ..
.rw-r--r-- benmp benmp 149 B   proyecto_0
```

---

## 4. Reconocimiento ICMP — `ping`

```bash
ping target-edu.example
```

- `ping`: envía paquetes ICMP Echo Request (Type 8) y espera Echo Reply (Type 0).
- Sin flags adicionales, en Linux corre indefinidamente hasta `Ctrl+C` (a diferencia de Windows que envía 4 por default).

### 4.1 Resolución DNS

`target-edu.example` → `192.0.2.95` → `edge-192-0-2-95.dfw57.r.cdn.example`

**Lectura forense del nombre:**

- `dfw57` indica edge location **Dallas-Fort Worth, EEUU**, POP número 57 del CDN provider.
- El subdominio del CDN provider confirma que **el sitio está detrás de un CDN comercial** (en este caso AWS CloudFront). No estamos pingeando el origin server real — estamos pegándole al edge node más cercano.

**Implicación de pentest:** un buen porcentaje de los recon hits van contra infraestructura del CDN provider, no contra el target real. Lo que `nmap` reporte de aquí en adelante refleja la postura de seguridad del **CDN edge**, no necesariamente del backend del target. Para auditar el origin real necesitas técnicas adicionales (subdomain enumeration, headers leak, certificados SAN, históricos en Censys/Shodan).

### 4.2 Estadísticas

```
42 packets transmitted, 42 received, 0% packet loss, time 41069ms
rtt min/avg/max/mdev = 27.102/29.241/46.539/3.399 ms
```

| Métrica         | Valor       | Lectura                                     |
|-----------------|-------------|---------------------------------------------|
| Packet loss     | 0%          | Conexión limpia, ruta estable               |
| RTT promedio    | 29.241 ms   | Coherente con edge en Dallas desde ubicación local |
| RTT max         | 46.539 ms   | Picos aislados, posible jitter intermedio   |
| Mean deviation  | 3.399 ms    | Variabilidad baja → ruta consistente        |

### 4.3 Análisis del TTL

Todos los replies con `ttl=243`. Esto es información de recon real, no decoración:

- **TTL inicial estándar por OS:**
  - Linux/Unix: `64`
  - Windows: `128`
  - BSD/Cisco/Solaris/equipos de red: `255`
- TTL recibido = TTL inicial − hops atravesados.
- `255 − 243 = 12 hops` desde la ubicación local hasta el edge del CDN.
- TTL inicial 255 sugiere **stack BSD-derived o appliance de red**, consistente con la infraestructura edge del CDN provider (CloudFront corre sobre stack propio basado en kernel custom).

> **Nota:** este truco del TTL es OS fingerprinting pasivo, mismo principio que usa `nmap -O` activamente. Es la primera capa de inteligencia que sacas antes de tocar puertos.

### 4.4 Hallazgo defensivo

**ICMP Echo está habilitado** en el edge. Eso significa:

- Recon trivial para el atacante (puedes enumerar disponibilidad sin tocar TCP).
- En pentest interno se considera mala práctica; en CDN público es decisión consciente del provider por monitoreo y debugging.
- Para uso de `nmap`, esto implica que **`-Pn` no será necesario** — el host responde a ping y nmap lo marcará como "up" sin discusión.

---

## 5. Trabajo pendiente para sesión 02

| Herramienta | Comando previsto                                         | Propósito                                                      |
|-------------|----------------------------------------------------------|----------------------------------------------------------------|
| `nmap`      | `sudo nmap -sV -sC -p- www.target-edu.example`           | Port scan + service version + scripts default                 |
| `whatweb`   | `whatweb -v http://www.target-edu.example`               | Fingerprint del stack web (CMS, framework, headers, plugins)  |

**Antes de ejecutarlos, vale la pena considerar:**

1. Validar **autorización explícita** del target educativo para escanear sus dominios. Un `nmap -p-` contra infra ajena sin permiso por escrito es legalmente cuestionable en México (Ley Federal de Protección de Datos Personales + Código Penal Federal Art. 211 bis). En curso oficial probablemente hay scope autorizado — confirmarlo antes.
2. El CDN provider **rate-limita y banea IPs agresivas**. Un scan completo `-p-` de 65535 puertos puede dispararte un block temporal del edge. Considerar `-T2` (polite) o `--max-rate` para mantenerse bajo el radar.
3. WhatWeb sobre HTTP (no HTTPS) puede no obtener todo — el sitio probablemente redirige 301 a HTTPS. Hacerlo también contra `https://www.target-edu.example`.

---

## 6. Notas técnicas misceláneas

- **Bug en comando de verificación previo:** el pipeline `ls /usr/share/seclists/ | head -n 5 || echo "no instalado"` no detecta correctamente la ausencia del directorio porque `head` enmascara el exit code. Solución: `set -o pipefail` o `[ -d /usr/share/seclists ]`. Este patrón se replica idénticamente en pipelines de CI/CD — referencia para futuras prácticas.
- **OpenVPN instalado es 2.7_rc4** (release candidate, no stable). Funcional para labs (HTB/THM), pero a tener presente si surge comportamiento extraño.

---

## 7. Glosario rápido (terminología bilingüe)

| Español                  | Inglés / técnico              |
|--------------------------|--------------------------------|
| Reconocimiento           | Reconnaissance / recon         |
| Edge / nodo de borde     | Edge node / PoP (Point of Presence) |
| Origen / servidor real   | Origin server                  |
| Huella digital del SO    | OS fingerprinting              |
| Salto de red             | Hop                            |
| Tiempo ida y vuelta      | Round-Trip Time (RTT)          |
| Limitación de tasa       | Rate limiting                  |

---

**Fin de sesión 01.**
