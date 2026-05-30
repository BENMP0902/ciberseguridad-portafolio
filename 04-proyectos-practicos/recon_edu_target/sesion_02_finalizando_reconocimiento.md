# Sesión 02 — Finalizando etapa de reconocimiento: target educativo

**Fecha:** Mayo 2026
**Curso:** Ciberseguridad (universitario)
**Autor:** benmp (`BENMP0902`)
**Target oficial:** `target-edu.example`
**Tipo de documento:** Reconnaissance phase report + incident log
**Estado:** Reconocimiento interrumpido por bloqueo de origen
**Sesión anterior:** `sesion_01_reconocimiento_inicial.md` (ICMP recon básico)

> 🛡️ **Nota de sanitización:** las direcciones IP, hostnames y nombres de dominio en este documento han sido sanitizados usando **RFC 5737** (IPv4 documentation: `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`) y **RFC 2606** (`.example` reservado para documentación). Para preservar la estructura analítica, las IPs del bloque masivo del cloud provider (originalmente un `/9` real) se mapean al bloque `198.51.100.0/24` conservando el último octeto del original. La metodología, comandos, errores y análisis técnico son fieles al ejercicio real.

---

## 1. Resumen ejecutivo

Sesión enfocada en cerrar la fase de *reconnaissance* (reconocimiento) sobre `target-edu.example` combinando técnicas pasivas (DNS, RDAP, WHOIS, IP intelligence) con escaneo activo de puertos vía Nmap. Identifiqué **4 IPs edge del CDN provider** en el POP **qro50 (regional)**, lo cual constituye un cambio relevante respecto a la sesión 01 donde reporté edge en **dfw57 (Dallas-Fort Worth)**. Esta variación es comportamiento normal de CDN, no compromiso, pero la registro como baseline.

Durante la fase activa cometí **errores graves de criterio** que terminaron en el bloqueo de mi IP de origen por parte de la infraestructura defensiva del cloud provider. Los errores y su análisis son la parte más valiosa de esta sesión — más que cualquier hallazgo técnico — y los documento en la sección 8.

---

## 2. Alcance y autorización — **lectura crítica obligatoria**

> ⚠️ **Disclaimer profesional:** Este reporte documenta acciones realizadas en contexto académico sobre `target-edu.example`. No obtuve autorización formal por escrito (*Rules of Engagement*) previa a la ejecución, ni se firmó un *Statement of Work* (SoW) con la institución target.

Lo registro como **gap procedural** porque en el mundo real una sesión así, sin autorización documentada, **es una violación legal**:

| Jurisdicción | Marco aplicable | Aplica porque |
|---|---|---|
| México (origen) | Código Penal Federal Art. 211 bis 1–7 (acceso ilícito a sistemas) | Opero desde territorio mexicano |
| EEUU (target) | Computer Fraud and Abuse Act, 18 USC §1030 | Infra cloud en región estadounidense |
| Cloud provider específico | AWS Acceptable Use Policy §3 (Penetration Testing Policy) | Escaneo sin notificación previa al provider |

**Para futuras sesiones**, antes de tocar teclado debo exigir un documento de autorización firmado que especifique:

1. *Targets in scope* (IPs/dominios concretos, NO rangos amplios)
2. *Out of scope* explícitos
3. *Time window* permitida
4. *Methods authorized* (port scan sí/no, brute force sí/no, exploit sí/no)
5. *Emergency contacts* en target
6. *Data handling* (qué se puede ver, qué se debe destruir)

Esto se llama **RoE** (*Rules of Engagement*) y es estándar industrial. Sin RoE firmado, no hay pentest — hay un delito.

---

## 3. Cronología de la sesión

| Hora (relativa) | Fase | Acción |
|---|---|---|
| T+00:00 | Pasiva | DNS resolution (`dig`) |
| T+00:00 | Pasiva | WHOIS attempt (con typo) |
| T+00:01 | Pasiva | RDAP query (post-error WHOIS) |
| T+00:01 | Pasiva | ARIN WHOIS sobre IP edge |
| T+00:02 | Pasiva | `curl ipinfo.io` sobre cada IP edge |
| T+05:50 | Pasiva | Comparativa DNS (typosquatting research) |
| T+06:15 | Activa | LAN sweep `nmap -sn 192.168.0.0/24` |
| T+06:30 | Activa | **Escaneo masivo `/9` (error crítico)** |
| T+06:42 | Activa | Cancelación manual del escaneo `/9` |
| T+06:49 | Activa | SYN scan dirigido a IP edge específica |
| T+06:50+ | Incidente | **Bloqueo de origen detectado por el cloud provider** |

---

## 4. Fase pasiva — *Passive reconnaissance*

### 4.1 Resolución DNS — `ping` y `dig`

```bash
ping target-edu.example            # ICMP con resolución implícita, sin cuenta
ping -c 3 target-edu.example       # Limita a 3 paquetes (recon "limpio")
dig target-edu.example             # Resolución DNS verbose
dig +short target-edu.example      # Solo registros A, output minimalista
```

**Hallazgo: rotación de IPs por petición**

| Comando | IP resuelta |
|---|---|
| `ping` (primer intento) | `203.0.113.27` |
| `ping -c 3` (segundo intento) | `203.0.113.106` |
| `dig` (respuesta completa) | `.71`, `.106`, `.27`, `.8` (4 IPs) |

**Lectura técnica:** El DNS de `target-edu.example` devuelve 4 registros A con **TTL=30 segundos**. Esto es DNS round-robin con TTL agresivamente bajo, típico de arquitecturas detrás de un **CDN comercial** (AWS CloudFront en este caso). El cliente recibe la respuesta, el resolver la cachea solo 30s, y la siguiente consulta puede regresar otro orden o subset. Esto es *intencional*: distribuye carga, facilita failover, dificulta el caching prolongado por atacantes.

**Implicación de pentest:** No debo fijar una IP como "la IP de target-edu.example". El target es el conjunto, no un elemento.

### 4.2 Comparativa de edge POPs entre sesiones

| Sesión | IP edge resuelta | POP CDN | Distancia geográfica |
|---|---|---|---|
| 01 | `192.0.2.95` | **dfw57** (Dallas-Fort Worth, TX) | ~1,150 km de ubicación local |
| 02 | `203.0.113.x` (cuatro IPs) | **qro50** (regional) | ~0 km — local |
| 02 (TTL) | n/a | `ttl=247` (vs 243 en sesión 01) | Hops disminuidos de 12 a 8 |

**Análisis:** El CDN provider introdujo (o se hizo enrutable) un POP regional entre la sesión 01 y la sesión 02. El cliente está siendo servido desde un edge ~1,150 km más cercano. RTT bajó de **29 ms** (sesión 01) a **16–19 ms** (sesión 02), consistente con la reducción de hops.

> 🔗 **Conexión técnica registrada:** Lo observado aquí es **anycast routing en acción**. En anycast, múltiples nodos físicos comparten la misma IP (o pool de IPs en un mismo bloque CIDR), y el BGP del proveedor enruta al nodo más cercano por número de saltos. CloudFront opera así globalmente. Importa documentarlo porque demuestra que dos sesiones de recon contra el mismo dominio pueden devolver infraestructuras físicamente distintas — información de valor que solo aparece comparando entre sesiones.

### 4.3 WHOIS, error, y transición a RDAP

```bash
whois targe-edu.example            # ERROR: typo en el dominio
# → "TLD is not supported."

rdap target-edu.example            # Comando alternativo, este sí funcionó
```

**Análisis del error:**

El primer error fue un **typo de mi parte** (`targe-edu` en lugar de `target-edu`), no una falla de la herramienta. Pero la respuesta del servidor WHOIS es engañosa: dice `"TLD is not supported"`, no `"domain not found"`. Esto pasa porque algunos clientes `whois` intentan adivinar el servidor por TLD; si no reconoce el TLD, responde con ese mensaje en lugar de hacer la query y devolver "no encontrado".

> ⚠️ **Aprendizaje registrado:** Los mensajes de error de herramientas viejas como `whois` no son siempre semánticamente precisos. Antes de asumir que el TLD no está soportado, debo verificar el comando.

**Por qué RDAP funcionó donde WHOIS falló (más allá del typo):**

RDAP (*Registration Data Access Protocol*) es el **reemplazo moderno** de WHOIS, formalizado en RFC 7480–7484. Mientras WHOIS responde en texto plano sin estructura por TCP/43, RDAP responde JSON estructurado sobre HTTPS. Post-GDPR (2018), ICANN mandató RDAP como protocolo preferente porque permite:

1. **Redacción granular de datos** (campo por campo) — se ve la estructura `redacted:` en la salida
2. **Autenticación diferenciada** (acceso público vs acceso autorizado a datos no-públicos)
3. **Bootstrapping vía IANA** — el cliente RDAP descubre automáticamente qué servidor consultar
4. **Internacionalización** (Unicode nativo, multi-idioma)

**Datos extraídos del RDAP de `target-edu.example`:**

| Campo | Valor | Lectura |
|---|---|---|
| Registrar | Registrador comercial estándar | Registrador estadounidense estándar |
| Created | ~5 años antes de la sesión | Dominio relativamente nuevo |
| Expires | Próxima fecha de renovación a ~2 meses vista | Próximo a renovación — vector de **typosquatting** post-expiración si no se renueva |
| DNSSEC | Delegation Signed: **false** | ❌ DNSSEC NO está habilitado — vulnerable a DNS cache poisoning |
| Nameservers | 4 NS del cloud provider (Route 53 / AWS DNS managed) | DNS managed en el cloud provider |
| Status codes | `client*Prohibited` (delete/renew/transfer/update) | Locks habilitados — buena práctica contra domain hijacking |

> 🚨 **Vector defensivo identificado:** DNSSEC desactivado. Para un dominio educativo este es un gap notable. Un atacante en posición de envenenamiento de caché DNS podría redirigir tráfico hacia infraestructura controlada. Es información a reportar a la organización en un *findings report*.

### 4.4 WHOIS sobre IP — atribución de propietario

```bash
whois 203.0.113.106
```

Aquí WHOIS sí funciona porque consulta a ARIN (*American Registry for Internet Numbers*) directamente, no a un registro de TLD.

**Hallazgos clave de ARIN:**

| Campo | Valor |
|---|---|
| NetRange amplio del cloud provider | `<bloque /9 del provider>` (*Direct Allocation*) |
| NetRange específico del CDN | `<bloque /14 del CDN>` |
| Organización | Amazon Technologies Inc. + Amazon.com, Inc. |
| Abuse contact | `trustandsafety@<provider>` |
| NOC contact | `<noc-contact>@<provider>` |

**Por qué esto importa para pentest:** El target es realmente infraestructura del cloud provider. Cualquier acción agresiva no la registra "el target educativo" — la registra **Trust & Safety del cloud provider**, y reportan al ISP de origen.

### 4.5 IP intelligence con `ipinfo.io`

```bash
curl https://ipinfo.io                    # Geolocaliza la IP propia
curl https://ipinfo.io/<IP>               # Geolocaliza IP arbitraria
```

| IP consultada | Hostname | ASN | Ubicación |
|---|---|---|---|
| **192.0.2.50** (propia) | `customer-XXX-cgn.example-isp.net` | AS<XXXX> ISP residencial | ciudad regional |
| 203.0.113.71 | `edge-203-0-113-71.qro50.r.cdn.example` | AS16509 Amazon | ciudad regional (POP) |
| 203.0.113.106 | (mismo patrón) | AS16509 Amazon | ciudad regional |
| 203.0.113.27 | (mismo patrón) | AS16509 Amazon | ciudad regional |
| 203.0.113.8 | (mismo patrón) | AS16509 Amazon | ciudad regional |

> ⚠️ **Información sensible expuesta sobre el operador:**
> - **Mi IP pública**
> - **Hostname con identificador interno:** incluye `cgn` (*Carrier-Grade NAT*), identificador del cliente y región
> - **ISP residencial**
> - **Coordenadas aproximadas** (centro de ciudad regional)
>
> Cuando el cloud provider detecte los escaneos masivos, **esta es la IP que reportará**. El ISP puede recibir requerimientos formales por parte de Trust & Safety del cloud con esa IP, ese timestamp, y el log de paquetes.

### 4.6 Análisis comparativo — typosquatting research

```bash
dig example-domain-a.example           # 203.0.113.200
dig example-domain-b.example           # 203.0.113.245
curl https://ipinfo.io/203.0.113.245
```

| Dominio | IP | Hosting | País |
|---|---|---|---|
| `example-domain-a.example` | 203.0.113.200 | (provider no resuelto en sesión) | n/a |
| `example-domain-b.example` | 203.0.113.245 | Google Cloud (AS43515 Google Ireland) | Council Bluffs, Iowa, US |

**Observación:** La diferencia ortográfica de unas letras corresponde a infraestructuras completamente distintas. Esto es **typosquatting research** — verificar si nombres similares al target están registrados, potencialmente para campañas de phishing.

> 🔗 **Conexión técnica registrada:** El concepto de *typosquatting* aplica también al periodo de expiración visto en el RDAP. Cuando un dominio expira sin renovarse, suele ser registrado en horas por bots que esperan justo eso. El status `clientTransferProhibited` que tiene `target-edu.example` mitiga parte del riesgo durante la vida del dominio, pero NO mitiga el riesgo de expiración. Si el target dejara expirar el dominio, podría ser registrado por un tercero ese mismo día.

---

## 5. Fase activa — *Active reconnaissance*

### 5.1 LAN sweep — `nmap -sn 192.168.0.0/24`

```bash
nmap -sn 192.168.0.0/24
```

**Desglose del comando:**
- `-sn` → *Ping scan* (antes `-sP`): solo descubrimiento de hosts, **NO** escanea puertos. Envía combinación de ICMP echo, TCP SYN/80, TCP ACK/443, ICMP timestamp.
- `192.168.0.0/24` → 256 IPs (192.168.0.0–192.168.0.255). Subnet privada típica de redes domésticas.

**Resultado:** 9 hosts activos en LAN local. Útiles como sanity check del entorno, no como recon de target externo. Tiempo: 23.12s.

**Por qué incluí esto:** confirma que la herramienta funciona, la subnet local responde, y permite identificar dispositivos propios (router, equipos, IoT) antes de ir al target externo.

### 5.2 ⚠️ Escaneo masivo `/9` — *el error crítico de la sesión*

```bash
nmap -vvv 198.51.100.0/9
```

**Esto NO debí ejecutarlo. Análisis del error de criterio:**

| Aspecto | Realidad |
|---|---|
| Tamaño del rango `/9` | **8,388,608 IPs** (2^23) |
| Propietario del rango | Cloud provider (Amazon Technologies Inc.) |
| Relación con target real | El target real está en un `/14` del CDN. El `/9` incluye decenas de miles de servidores ajenos. |
| Tiempo estimado para completar | Semanas a meses, dependiendo de paralelismo y rate-limiting |
| Probabilidad de bloqueo | ~100% en las primeras horas |
| Autorización para escanear esos hosts | **Cero.** |

**Lo que el comando estaba realmente haciendo:**

1. **Ping Scan inicial** (4 puertos por host): 4,096 hosts probados en el primer batch (limitado por paralelismo de Nmap)
2. De esos 4,096, **64 hosts respondieron** como `up`
3. **SYN Stealth Scan** sobre esos 64 hosts: 1,000 puertos cada uno = 64,000 puertos escaneados
4. Cuando lo cancelé, estaba a `5.59% done` de la **siguiente** batch de 64 hosts

**Comportamiento de defensa observado durante el escaneo:**

```
Increasing send delay for 198.51.100.25 from 0 to 5 due to max_successful_tryno increase to 4
Increasing send delay for 198.51.100.37 from 5 to 10 due to max_successful_tryno increase to 5
Increasing send delay for 198.51.100.37 from 10 to 20 due to max_successful_tryno increase to 6
[...]
Increasing send delay for 198.51.100.37 from 160 to 320 due to 11 out of 18 dropped probes since last increase.
```

**Lectura:** Algunos hosts (notablemente `198.51.100.25`, `198.51.100.32`, `198.51.100.37`) empezaron a **dropear paquetes activamente** después del ramp-up del scan. Nmap automáticamente ajustó la velocidad. Esto es comportamiento típico de:
- **AWS Shield Standard** (DDoS protection por defecto en CloudFront/ALB)
- **Security Groups con conntrack limits**
- **IDS/IPS** (probable GuardDuty u otro sistema de detección)

**Hosts notables detectados en los 64 que respondieron:**

| IP | Puertos abiertos | Lectura |
|---|---|---|
| **198.51.100.32** | 80, 110, 135, 139, 143, 443, 445, 587, 1099, 3306, 3389, 5985 | Windows server con SMB, RDP, MySQL, IMAP, POP3, WinRM, RMI. **Patrón clásico de honeypot o servidor severamente mal configurado.** En producción real, exponer todo esto junto es indefendible. |
| 198.51.100.35 | 80, 81, 83, 443, 1433, 8000, 8001 | Servidor Windows + MS-SQL. También sospechoso. |
| 198.51.100.52 | 80, 88, 443, 808, 8088 | Puerto 88 (Kerberos) → posible Domain Controller. |
| 198.51.100.227 | 22, 80, 443, 7777, 7778 | SSH + servicios custom en puertos altos. |

> ⚠️ **Hipótesis: estos hosts son honeypots de seguridad operados por el cloud provider o terceros.** Los honeypots están diseñados precisamente para atraer escaneos como el que ejecuté y capturar las IPs origen. Si `198.51.100.32` es un honeypot, mi IP ya está en una lista de origen sospechoso.

### 5.3 SYN scan dirigido — `sudo nmap -sS -Pn -vvv 203.0.113.71`

```bash
sudo nmap -sS -Pn -vvv 203.0.113.71
```

**Desglose:**
- `sudo` → necesario para SYN scan crudo (raw sockets, requiere CAP_NET_RAW)
- `-sS` → *SYN scan* (half-open scan): envía SYN, espera SYN-ACK, no completa con ACK. Históricamente "stealth" porque no aparecía en logs de aplicación, pero IDS modernos lo detectan trivialmente.
- `-Pn` → *No ping*: asume que el host está up sin probarlo. Útil cuando ICMP está filtrado. **Aquí innecesario** porque sabía que el CDN responde a ICMP (lección de sesión 01).
- `-vvv` → verbose máximo

**Resultado:**

```
PORT    STATE SERVICE REASON
80/tcp  open  http    syn-ack ttl 247
443/tcp open  https   syn-ack ttl 247
```

- Solo dos puertos abiertos: 80 y 443. **Esperado** en un CDN edge — CloudFront expone únicamente HTTP/HTTPS.
- `ttl 247` → consistente con stack BSD-derived (TTL inicial 255, 8 hops).
- 998 puertos en estado `filtered (no-response)` → AWS Shield está activamente dropeando, no contestando con RST.
- Tiempo: 6.50s, 2000 paquetes enviados, 4 respuestas recibidas.

**Lectura:** Este escaneo es defendible. Un solo host, dos servicios públicos detectados, no agresivo. Pero ya viene "marcado" por el escaneo anterior.

---

## 6. Mapa visual del flujo de reconocimiento

```
[INTERNET]
    │
    ├── Fase pasiva (sin tocar al target)
    │     ├── DNS: dig +short → 4 IPs
    │     ├── RDAP: target-edu.example → metadata dominio
    │     ├── WHOIS sobre IP → ARIN → cloud provider CDN
    │     └── ipinfo.io → confirmación geolocalización
    │
    └── Fase activa (paquetes al target)
          ├── nmap -sn (LAN)              ✓ OK
          ├── nmap -vvv /9 (ERROR)        ✗ Bloqueado, cancelado
          └── nmap -sS -Pn (single IP)    ✓ OK pero tardío

[OPERADOR: 192.0.2.50 — ISP residencial]
    ↑
    └── Trust & Safety del cloud provider registra origen
```

---

## 7. Comparativa de comandos ejecutados

| Comando | Categoría | Riesgo de detección | Valor | ¿Volver a usar? |
|---|---|---|---|---|
| `ping`, `dig` | Pasiva | Nulo | Alto (base) | Sí, siempre |
| `rdap` | Pasiva | Nulo | Alto | Sí, preferir sobre `whois` |
| `whois` (dominio) | Pasiva | Nulo | Medio (post-GDPR) | Solo si falla RDAP |
| `whois <IP>` (ARIN) | Pasiva | Nulo | Alto | Sí |
| `curl ipinfo.io` | Pasiva | Bajo (deja log en ipinfo.io) | Alto | Sí |
| `nmap -sn /24` (LAN) | Activa | Nulo (propia red) | Alto (sanity check) | Sí |
| `nmap -vvv /9` (target ajeno) | Activa-masiva | **Crítico** | Nulo | **NUNCA** |
| `nmap -sS -Pn` (single IP) | Activa-dirigida | Medio | Alto | Sí, con autorización |

---

## 8. Errores cometidos y aprendizajes

Esta es la sección más valiosa del documento. La sesión produjo más errores que hallazgos, lo cual es **didácticamente útil** si los internalizo.

### 8.1 Typo `targe-edu.example` en `whois`
**Severidad:** Baja. Solo perdí 30 segundos.
**Aprendizaje:** Validar el comando antes de ejecutar. En sesiones reales, automatizar con variables: `TARGET="target-edu.example"; whois "$TARGET"`.

### 8.2 Ejecución de `nmap -vvv 198.51.100.0/9`
**Severidad:** **Crítica.** Combinación de:

1. **Falta de cálculo de magnitud antes de ejecutar.** `/9` = 8.3M IPs. Tres segundos de aritmética antes de presionar Enter habrían evitado el problema.
2. **Confusión entre el rango del propietario y el rango del target.** WHOIS mostró que ARIN asignó el `/9` al cloud provider. Eso NO significa que sea el target — significa que es el bloque madre del cual el provider sub-asigna pedazos pequeños a CDN, compute, etc. El target real (CDN) está en un `/14`, **mucho más pequeño**.
3. **Ausencia de filtro defensivo en el comando.** Sin `-T2` (polite), sin `--max-rate`, sin `--randomize-hosts`, sin `--scan-delay`.
4. **Ejecución sin `sudo`** en el primer intento → Nmap cae a TCP connect() scan (`-sT`), que es 3x más ruidoso que `-sS`.

**Aprendizaje (regla mental):** Antes de cualquier `nmap` con CIDR, calcular `2^(32-prefix)` mentalmente:
- `/24` → 256 hosts → OK
- `/16` → 65,536 hosts → cuestionable, requiere `-T2` y justificación
- `/12` → 1M hosts → no, salvo proyecto formal con autorización explícita
- `/9` → 8.3M hosts → **NO** bajo ninguna circunstancia desde una IP doméstica

### 8.3 Uso de `-Pn` sin necesidad

En `sudo nmap -sS -Pn -vvv 203.0.113.71` usé `-Pn` (skip host discovery). Pero ya sabía por sesión 01 que el CDN responde a ICMP. `-Pn` solo se justifica cuando el host filtra ping y quiero forzar el scan. Usarlo sin necesidad es ineficiente y deja huella reconocible (Nmap envía un patrón específico de paquetes en modo `-Pn`).

### 8.4 Mismas dos IPs del target en distintos rangos CIDR

Subtileza: en la sesión 01 vi `192.0.2.95` (Dallas), en la sesión 02 vi `203.0.113.x` (regional). Ambos son del mismo CDN provider pero en bloques CIDR distintos del mismo proveedor.

**Aprendizaje:** No basta con anotar la IP. Debo anotar el bloque CIDR y el nombre asignado por el RIR (Regional Internet Registry). Eso da inteligencia sobre qué tipo de servicio del cloud provider estoy tocando.

---

## 9. Incidente: bloqueo de IP origen

### 9.1 Hechos

Tras la cancelación manual del `nmap -vvv 198.51.100.0/9` (que alcanzó a transmitir miles de paquetes hacia 64 hosts activos del rango del cloud provider) y la ejecución posterior del `nmap -sS -Pn` contra `203.0.113.71`, **el servidor de origen bloqueó mi IP**, impidiendo continuar con la fase de reconocimiento dirigida al target.

### 9.2 Análisis de causa raíz

La defensa del cloud provider aplicó **rate-limiting / IP block** sobre mi origen como respuesta agresiva al escaneo masivo del `/9`. Los mecanismos probables involucrados:

1. **AWS Shield Standard** — protección DDoS gratuita en todos los recursos AWS. Detecta patrones de scan a escala y aplica mitigaciones automáticas.
2. **GuardDuty** (si está habilitado en cuentas afectadas) — detecta `Recon:EC2/PortProbeUnprotectedPort` y eventos similares, alerta y puede automatizar respuesta vía EventBridge.
3. **WAF rules** en CloudFront — limita conexiones por IP por minuto.
4. **Honeypot networks** — algunos de los hosts detectados (especialmente `198.51.100.32`) probablemente son trampas que capturan IPs origen y las propagan a listas de bloqueo.

### 9.3 Lo que esto implica operativamente

| Consecuencia | Probabilidad | Plazo |
|---|---|---|
| Bloqueo temporal de mi IP contra el CDN/edge del provider | **Confirmada** | Activa ahora, duración 24h–7d típica |
| Notificación de Trust & Safety del provider al ISP | Media | 24–72h |
| Inclusión de la IP en listas de threat intelligence (AbuseIPDB, AlienVault OTX) | Alta | Días |
| Acción legal | Muy baja (target académico, sin daño) | n/a |

### 9.4 Mitigación inmediata

1. **No reintentaré** desde la misma IP en las próximas 24–48h.
2. **No usaré VPN ni Tor para "evitar" el bloqueo.** Hacerlo elevaría la severidad del incidente — pasaría de "scanner inexperto" a "atacante intencional ocultando origen". Acepto el bloqueo como consecuencia natural y espero.
3. **Documentar el incidente** (este reporte cumple esa función).
4. Si la sesión académica requiere continuar contra el target, **solicitar a la institución que provea un entorno aislado** (red dedicada, target dentro de un VPC controlado) en lugar de escanear la web pública.

### 9.5 Comunicación profesional del incidente

Si esto ocurriera en un contexto laboral real, el reporte al supervisor sería en estos términos:

> *English production practice:*
>
> > **Incident report — recon phase blocked**
> >
> > "During the active reconnaissance phase against `target-edu.example`, a wide-range port scan was executed against the parent CIDR block (`/9`) instead of the actual target subnet (`/14`). The scan triggered defensive measures at the cloud provider level, resulting in an IP block of the source address. The scan was manually cancelled upon detection of the issue.
> >
> > **Root cause:** insufficient scope definition before execution.
> > **Impact:** loss of reconnaissance capability from primary source IP for an estimated 24–72 hours.
> > **Next steps:** pause active recon until block expires; use this time to deepen passive intelligence gathering."

---

## 10. Recomendaciones para próxima sesión

1. **Antes de continuar:** confirmar autorización formal con el responsable académico para escanear los subdominios del target. Documentar por escrito (correo electrónico mínimo).
2. **Definir scope estricto:** lista explícita de IPs o subdominios autorizados (NO rangos CIDR del cloud provider).
3. **Cuando el bloqueo expire**, retomar con escaneos dirigidos:
   ```bash
   # Subdomain enumeration pasiva primero
   sudo nmap -sS -p- --min-rate 100 -T2 target-edu.example

   # WhatWeb sobre HTTPS (corrección del plan de sesión 01)
   whatweb -v https://www.target-edu.example

   # Headers HTTP para fingerprinting de stack
   curl -I https://target-edu.example
   ```
4. **Considerar herramientas de subdomain discovery pasivo** (no tocan al target):
   - `subfinder`, `amass` (consulta a APIs públicas y certificados SAN)
   - `crt.sh` (transparencia de certificados — gratis, sin tocar al target)
5. **Mejorar el script de cobertura:** `set -o pipefail` en cualquier pipeline shell (referencia a sesión 01).
6. **Para la siguiente sesión, agendar 1 hora de teoría sobre RoE y aspectos legales antes de tocar herramientas.** Lo técnico no compensa la negligencia de scope.

---

## 11. Glosario terminológico (bilingüe)

| Español | Inglés / técnico | Definición breve |
|---|---|---|
| Reglas de enfrentamiento | Rules of Engagement (RoE) | Contrato técnico-legal que define scope, métodos, ventana temporal de un pentest |
| Reconocimiento pasivo | Passive reconnaissance | Inteligencia sin enviar paquetes al target (DNS, RDAP, OSINT) |
| Reconocimiento activo | Active reconnaissance | Envío directo de paquetes al target (ping, port scan) |
| Escaneo SYN sigiloso | SYN stealth scan | Half-open scan: SYN → espera SYN-ACK → no completa con ACK |
| Limitación de tasa | Rate limiting | Bloqueo temporal por exceder umbrales de tráfico |
| Punto de presencia | Point of Presence (PoP) | Nodo físico de una CDN o ISP en una ubicación geográfica |
| Salto de red | Hop | Cada router intermedio que atraviesa un paquete |
| Tiempo de vida | Time To Live (TTL) | Contador IP decrementado en cada hop; previene loops |
| Tabla de tabla regional | Regional Internet Registry (RIR) | ARIN, RIPE, LACNIC, AFRINIC, APNIC — asignan rangos IP |
| Sistema autónomo | Autonomous System (AS) | Bloque de IPs administrado por una entidad con política de ruteo única |
| Encolamiento de paquetes | Packet dropping | Defensa: descartar paquetes en lugar de responderlos |
| Trampa de bajo interés | Honeypot | Servidor diseñado para atraer atacantes y registrar sus acciones |
| Sistema de prevención de intrusos | Intrusion Prevention System (IPS) | Detecta y bloquea automáticamente comportamiento malicioso |
| Listas de reputación | Threat intelligence feeds | Bases de datos de IPs/dominios con historial malicioso |

---

## 12. Estado de cierre

| Item | Estado |
|---|---|
| Fase pasiva completada | ✅ Sí |
| Fase activa contra target oficial | ⚠️ Parcial (solo 1 IP escaneada con éxito) |
| Bloqueo de IP origen | ❌ Activo (impide continuar) |
| Hallazgos defensivos reportables a la institución | DNSSEC desactivado, expiración cercana del dominio |
| Lecciones procedurales documentadas | ✅ Sí (secciones 2 y 8) |
| Siguiente sesión | Pendiente — sujeta a expiración del bloqueo + obtención de RoE formal |

---

**Fin de sesión 02.**

*Reporte sanitizado para publicación responsable. Datos identificables reemplazados según RFC 5737 y RFC 2606.*
