# 🎯 Reconocimiento — Target educativo

Carpeta del proyecto de reconocimiento sobre un target del ámbito educativo, ejercicio realizado en contexto de la materia de Ciberseguridad.

> 🛡️ **Sanitización aplicada:** todos los datos identificables (IPs reales, hostnames, ISP, ubicación específica, nombre del target) han sido reemplazados según **RFC 5737** (IPv4 documentation) y **RFC 2606** (`.example` reservado). La metodología, errores y análisis técnico se conservan tal cual fueron ejecutados.

---

## 📁 Contenido

| Archivo | Descripción |
|---|---|
| `sesion_01_reconocimiento_inicial.md` | Setup del entorno, reconocimiento ICMP pasivo, análisis de TTL, fingerprinting básico del CDN. |
| `sesion_02_finalizando_reconocimiento.md` | Reconocimiento pasivo extendido (DNS, RDAP, WHOIS, IP intelligence), fase activa con Nmap, **incidente de bloqueo de IP** por escaneo masivo accidental. |
| `README.md` | Este archivo. |

---

## 📋 Resumen de cada sesión

### Sesión 01 — Reconocimiento inicial
- Setup paralelo Kali en WSL2 y VirtualBox para comparar entornos.
- Estructura de directorios de trabajo y archivo `proyecto_0` con el objetivo de la práctica.
- `ping` al target, lectura forense del hostname resuelto (POP CDN `dfw57`, Dallas-Fort Worth).
- Análisis de TTL (`243`) → identificación de stack BSD-derived, ~12 hops desde origen.
- ICMP Echo habilitado en el edge → implicación para uso futuro de `nmap` sin `-Pn`.

### Sesión 02 — Finalizando reconocimiento
- **Fase pasiva:**
  - DNS round-robin con 4 IPs y TTL=30s (patrón CDN).
  - Comparativa con sesión 01: el CDN sirve ahora desde POP regional `qro50` (RTT 16–19 ms vs 29 ms anterior) — observación de anycast routing.
  - WHOIS falló por typo de operador → transición a RDAP (estándar post-GDPR).
  - RDAP: hallazgo defensivo — **DNSSEC desactivado** en el target.
  - WHOIS sobre IP (ARIN) → atribución al cloud provider.
  - `ipinfo.io` para IP intelligence sobre target y origen.
  - Typosquatting research: dominios similares apuntando a infraestructura distinta.
- **Fase activa:**
  - LAN sweep sanity check (`nmap -sn` sobre `/24` local).
  - **Error crítico:** ejecución de `nmap -vvv` sobre un bloque `/9` del cloud provider (~8.3M IPs) por confusión entre rango del propietario y rango del target real (`/14`).
  - Cancelación manual tras observar comportamiento defensivo (delays automáticos, hosts dropeando paquetes).
  - SYN scan dirigido a una IP edge: dos puertos abiertos (80, 443) como se esperaba.
- **Incidente:** bloqueo de IP de origen aplicado por el cloud provider tras los escaneos. Documentado con análisis de causa raíz y mitigación.

---

## 🧠 Lecciones técnicas clave

1. **Calcular magnitud antes de ejecutar.** Para cualquier CIDR en `nmap`, aplicar mentalmente `2^(32-prefix)` antes de presionar Enter. `/24` = 256 OK; `/9` = 8.3M nunca desde IP doméstica.
2. **El bloque del propietario ≠ el rango del target.** El cloud provider tiene asignado el `/9` completo, pero el servicio específico (CDN) ocupa solo un `/14` dentro de él. Confundirlos es un error de scope con consecuencias legales y operativas.
3. **RDAP es el reemplazo de WHOIS post-GDPR** (RFC 7480–7484). Más estructurado, soporta redacción granular y se descubre vía IANA.
4. **DNSSEC desactivado en un dominio educativo es un hallazgo reportable.** Expone al target a cache poisoning.
5. **Sin RoE firmado, no hay pentest — hay un delito.** Marco legal aplicable (México: Art. 211 bis CPF; EEUU: CFAA 18 USC §1030) cubre el caso.
6. **Anycast routing en CDN** explica por qué dos sesiones de recon al mismo dominio pueden devolver infraestructura física distinta.
7. **Documentar errores propios honestamente** es lo que diferencia un junior con criterio de uno sin él. Las secciones 8 y 9 de la sesión 02 son post-mortem accountable.

---

## ⚖️ Disclaimer ético

El ejercicio fue realizado en contexto académico. La sesión 02 documenta explícitamente la **ausencia de Rules of Engagement firmadas** previas a la ejecución — un gap procedural que no debe replicarse en futuras prácticas y que aquí queda registrado como aprendizaje, no como justificación.

Cualquier replicación de las técnicas descritas debe contar con autorización explícita por escrito del propietario del sistema objetivo. La sanitización aplicada en estos documentos previene la identificación del target real, pero no exime al lector de su responsabilidad ética y legal.
