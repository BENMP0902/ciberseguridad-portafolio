# 🌐 MÓDULO 1: FUNDAMENTOS ABSOLUTOS DE REDES

## 📅 DÍA 8-9: ¿QUÉ ES UNA RED REALMENTE?

### 🎯 Objetivo
Entender redes desde los fundamentos físicos hasta el propósito funcional, con mentalidad de seguridad.

---

## 1.1 - DEFINICIÓN TÉCNICA

### ¿Qué es una red?

> **Definición formal:** Sistema de dispositivos interconectados que pueden intercambiar información usando protocolos estandarizados sobre medios de transmisión específicos.

**Desglosemos esto:**

1. **Dispositivos interconectados** = Hosts (endpoints) + Equipos de red (intermediarios)
2. **Intercambiar información** = Comunicación bidireccional de datos
3. **Protocolos estandarizados** = Reglas que todos entienden (TCP/IP, HTTP, DNS)
4. **Medios de transmisión** = Cable físico, ondas de radio, fibra óptica

---

## 1.2 - LOS 3 NIVELES DE UNA RED

### Nivel 1: FÍSICO (El Hardware)

**¿Qué es?**  
Los componentes tangibles que mueven los bits.

**Componentes:**

```
MEDIOS DE TRANSMISIÓN:
├─ Cable de cobre (Cat5e, Cat6, Cat6a)
│  • Velocidades: 1 Gbps - 10 Gbps
│  • Distancia máxima: 100 metros
│  • Vulnerable a: Interferencia electromagnética, escuchas (wiretapping)
│
├─ Fibra óptica (Single-mode, Multi-mode)
│  • Velocidades: 10 Gbps - 100 Gbps+
│  • Distancia: Kilómetros
│  • Seguridad: Difícil interceptar (luz vs electricidad)
│
└─ Inalámbrico (Wi-Fi, Bluetooth, 5G)
   • Velocidades: Variable (10 Mbps - 10 Gbps)
   • Seguridad: MÁS VULNERABLE (broadcast abierto)
   • Ataques: Rogue APs, Evil Twin, Deauth, WPS bruteforce
```

**Dispositivos Físicos:**

| Dispositivo | Capa OSI | Función | Superficie de Ataque |
|-------------|----------|---------|---------------------|
| **Cable** | Capa 1 | Transmitir señales eléctricas/luz | Wiretapping, corte físico |
| **Hub** | Capa 1 | Repetir señales a TODOS los puertos | Sniffing fácil (broadcast) |
| **Switch** | Capa 2 | Enviar frames solo al destino | MAC flooding, ARP spoofing |
| **Router** | Capa 3 | Conectar redes diferentes | IP spoofing, routing attacks |
| **Firewall** | Capa 3-7 | Filtrar tráfico | Evasión, misconfiguration |

**⚠️ Perspectiva de Seguridad:**

```
CAPA FÍSICA = Primera línea de defensa

Controles físicos:
✓ Acceso restringido a salas de servidores
✓ Cámaras de seguridad
✓ Candados en racks
✓ Detección de corte de cables

Ataques físicos:
✗ Conectar dispositivo rogue (Raspberry Pi con Kali)
✗ Wiretapping (pinzas en cable Ethernet)
✗ Theft de equipos
✗ USB drop attacks
```

---

### Nivel 2: LÓGICO (El Direccionamiento)

**¿Qué es?**  
Sistema de identificación para encontrar dispositivos en la red.

**Dos tipos de direcciones:**

#### **Direcciones MAC (Media Access Control)**
- **Capa:** 2 (Enlace)
- **Formato:** 48 bits = 6 bytes = 12 hex digits
- **Ejemplo:** `00:0C:29:3A:4B:5C`
- **Único por:** Tarjeta de red (NIC)
- **Alcance:** Solo dentro de misma red física (LAN)

```
Estructura MAC Address:
00:0C:29 : 3A:4B:5C
└─OUI──┘ └─NIC ID┘

OUI (Organizationally Unique Identifier) = Fabricante
• 00:0C:29 = VMware
• 08:00:27 = VirtualBox
• DC:A6:32 = Raspberry Pi
```

**Implicaciones de seguridad:**
```
✓ MAC filtering en Wi-Fi (débil, se puede spoof)
✗ MAC spoofing: cambiar tu MAC para bypass controles
✗ MAC address tracking (privacy concern)
✗ Identificar fabricante = fingerprinting
```

#### **Direcciones IP (Internet Protocol)**
- **Capa:** 3 (Red)
- **Formato IPv4:** 32 bits = 4 octetos
- **Ejemplo:** `192.168.1.100`
- **Alcance:** Global (con ruteo)

```
Tipos de IPs:

PÚBLICAS (Internet):
• Asignadas por ISP
• Únicas globalmente
• Rutables en Internet
• Ejemplo: 8.8.8.8 (Google DNS)

PRIVADAS (RFC 1918):
• 10.0.0.0/8       (10.0.0.0 - 10.255.255.255)
• 172.16.0.0/12    (172.16.0.0 - 172.31.255.255)
• 192.168.0.0/16   (192.168.0.0 - 192.168.255.255)
• NO rutables en Internet
• NAT para salir a Internet
```

**Relación MAC ↔ IP:**
```
IP dice DÓNDE (dirección lógica)
MAC dice QUIÉN (dirección física)

Protocolo ARP (Address Resolution Protocol):
Pregunta: "¿Quién tiene IP 192.168.1.1? Dime tu MAC"
Respuesta: "Soy yo, mi MAC es AA:BB:CC:DD:EE:FF"
```

---

### Nivel 3: FUNCIONAL (El Propósito)

**¿Para qué existen las redes?**

1. **Compartir recursos**
   - Archivos (File servers)
   - Impresoras
   - Bases de datos
   - Aplicaciones

2. **Comunicación**
   - Email
   - Mensajería instantánea
   - VoIP
   - Video conferencia

3. **Acceso a servicios**
   - Internet
   - Cloud computing
   - APIs
   - Streaming

4. **Centralización**
   - Administración remota
   - Backups centralizados
   - Políticas de seguridad
   - Monitoreo

---

## 1.3 - TIPOS DE REDES POR ALCANCE

### Tabla Comparativa

| Tipo | Nombre | Alcance | Ejemplo | Velocidad típica | Uso en Seguridad |
|------|--------|---------|---------|------------------|------------------|
| **PAN** | Personal Area Network | 1-10 metros | Bluetooth, USB | 1-100 Mbps | BadUSB, Evil Maid |
| **LAN** | Local Area Network | Edificio | Ethernet empresarial | 1-10 Gbps | Segmentación VLAN, MITM |
| **WLAN** | Wireless LAN | 50-100 metros | Wi-Fi corporativo | 100-1000 Mbps | WPA cracking, Rogue AP |
| **MAN** | Metropolitan Area Network | Ciudad | Red gobierno | 100 Mbps - 10 Gbps | Interconexión segura |
| **WAN** | Wide Area Network | País/Continente | Internet, MPLS | Variable | VPN, inspección borde |

---

### LAN (Local Area Network) - PROFUNDO

**Características:**
```
✓ Alta velocidad (1-10 Gbps)
✓ Baja latencia (<1 ms)
✓ Bajo costo operativo
✓ Control total del administrador
✓ Broadcast domain único (sin segmentación)
```

**Componentes típicos:**
```
Internet
   |
[Router/Firewall] ← Punto de entrada/salida
   |
[Core Switch] ← Distribución principal
   |
   ├─[Switch 1]─[PCs]
   ├─[Switch 2]─[Servidores]
   └─[Access Point]─[Dispositivos Wi-Fi]
```

**Problemas de seguridad en LAN tradicional:**

❌ **Flat network (sin segmentación)**
```
Impresora → Puede ver servidor de base de datos
Usuario guest → Puede escanear toda la red
Dispositivo IoT comprometido → Acceso a TODA la LAN
```

✅ **Solución: Segmentación con VLANs**
```
VLAN 10: Usuarios
VLAN 20: Servidores
VLAN 30: Invitados
VLAN 40: IoT/Impresoras
VLAN 99: Administración

Firewall entre VLANs controla quién habla con quién
```

---

### WAN (Wide Area Network) - PROFUNDO

**¿Qué es?**  
Red que conecta LANs geográficamente distantes.

**Tecnologías comunes:**

1. **Internet (Public WAN)**
   - Más barato
   - Menos seguro (tráfico público)
   - Requiere VPN para proteger datos

2. **MPLS (Multiprotocol Label Switching)**
   - Circuito privado
   - Más caro
   - Más seguro (ISP garantiza privacidad)
   - QoS garantizado

3. **SD-WAN (Software-Defined WAN)**
   - Moderno, flexible
   - Múltiples links (Internet + MPLS)
   - Encriptación automática

**Ejemplo corporativo:**
```
[Oficina México DF]
        |
    Internet + MPLS
        |
[Oficina Monterrey]
        |
    VPN Tunnel
        |
[Oficina remota Querétaro]
```

**Controles de seguridad en WAN:**
```
✓ VPN (IPsec o SSL)
✓ Firewall en cada sitio
✓ IDS/IPS en borde
✓ Encriptación end-to-end
✓ Autenticación fuerte (MFA)
```

---

## 1.4 - TOPOLOGÍAS DE RED

### Topología Física vs Lógica

**Topología FÍSICA** = Cómo están conectados los cables  
**Topología LÓGICA** = Cómo fluyen los datos

Pueden ser diferentes. Ejemplo:
- Físicamente: Estrella (todos conectados a switch central)
- Lógicamente: Bus (switch simula broadcast)

---

### Tipos de Topologías

#### 1. **BUS (Obsoleta)**

```
[PC]---[PC]---[PC]---[PC]---[PC]
       |
   Cable coaxial
```

**Características:**
- Un solo cable compartido
- Todos los dispositivos ven todo el tráfico (broadcast)
- Colisiones frecuentes (CSMA/CD)

**Seguridad:**
❌ TERRIBLE: Cualquier dispositivo puede sniffar todo el tráfico  
❌ Un fallo en cable = toda la red cae

**Ya no se usa** (reemplazada por Ethernet switched)

---

#### 2. **ESTRELLA (Más común hoy)**

```
        [Switch]
       /  |  |  \
     /    |  |    \
  [PC] [PC][Server][PC]
```

**Características:**
- Todos conectados a dispositivo central (switch/router)
- Tráfico solo va al destino (no broadcast)
- Fallo de un cable no afecta a otros

**Seguridad:**
✓ Mejor que bus (switch filtra)  
✓ Fácil de monitorear (puerto de spanning)  
⚠️ Switch es punto único de fallo (single point of failure)

---

#### 3. **MALLA (Mesh)**

```
[Router A]───[Router B]
    │    ╲  ╱    │
    │     ╳      │
    │    ╱  ╲    │
[Router C]───[Router D]
```

**Características:**
- Múltiples rutas entre nodos
- Redundancia alta
- Costosa (muchos cables/links)

**Tipos:**
- **Full Mesh:** Todos conectados con todos (n*(n-1)/2 conexiones)
- **Partial Mesh:** Solo conexiones críticas

**Seguridad:**
✓ Alta disponibilidad (DDoS resistance)  
✓ Si un link cae, tráfico se re-rutea  
⚠️ Más compleja de asegurar (múltiples paths)

**Uso:** ISPs, data centers, redes críticas

---

#### 4. **ANILLO (Ring)**

```
[PC1] → [PC2] → [PC3]
  ↑                 ↓
[PC6] ← [PC5] ← [PC4]
```

**Características:**
- Datos viajan en una dirección
- Token passing (un solo token circula)

**Seguridad:**
⚠️ Un corte = toda la red cae (a menos que sea dual ring)

**Uso:** FDDI, SONET (telecomunicaciones legacy)

---

## 1.5 - DOMINIO DE BROADCAST Y COLISIÓN

### Dominio de Colisión

**Definición:**  
Área donde dos dispositivos pueden transmitir simultáneamente y causar colisión.

```
CON HUB (Capa 1):
[PC1]─┐
      ├─[HUB]─[PC4]
[PC2]─┤
[PC3]─┘

Si PC1 y PC2 transmiten al mismo tiempo → COLISIÓN
Todos los puertos son 1 dominio de colisión

CON SWITCH (Capa 2):
[PC1]─┐
      ├─[SWITCH]─[PC4]
[PC2]─┤
[PC3]─┘

Cada puerto es su propio dominio de colisión
PC1 y PC2 pueden transmitir simultáneamente SIN colisión
```

**Regla:**
- **Hub:** 1 dominio de colisión para todos los puertos
- **Switch:** 1 dominio de colisión POR PUERTO

---

### Dominio de Broadcast

**Definición:**  
Área donde un broadcast (FF:FF:FF:FF:FF:FF) llega a todos.

```
SIN SEGMENTACIÓN:
[PC1]─┐
      ├─[SWITCH 1]─[SWITCH 2]─[PC5]
[PC2]─┤              │
[PC3]─┘          [PC4]

Broadcast de PC1 llega a PC2, PC3, PC4, PC5
= 1 dominio de broadcast

CON ROUTER:
[PC1]─[SWITCH]─[ROUTER]─[SWITCH]─[PC5]
[PC2]─┘          192.168.1.1     └─[PC6]
                 192.168.2.1

Broadcast de PC1 NO llega a PC5/PC6
Router rompe dominios de broadcast
```

**Regla:**
- **Switch:** NO rompe dominio de broadcast
- **Router:** SÍ rompe dominio de broadcast
- **VLAN:** SÍ rompe dominio de broadcast (lógicamente)

**Implicaciones de seguridad:**
```
Dominio de broadcast grande = Riesgo alto

Ataques que usan broadcast:
• ARP spoofing (envía ARP reply broadcast)
• DHCP spoofing (rogue DHCP server)
• NetBIOS scanning
• mDNS/LLMNR poisoning

Mitigación:
✓ Segmentar con VLANs
✓ Límites en storm control
✓ Port security en switches
```

---

## 1.6 - DISPOSITIVOS DE RED: ANÁLISIS PROFUNDO

### HUB (Obsoleto - Solo historia)

**¿Qué hace?**  
Repite señales eléctricas a TODOS los puertos.

```
Flujo:
PC1 envía frame a PC3
  ↓
Hub recibe en puerto 1
  ↓
Hub TRANSMITE A TODOS LOS PUERTOS (1, 2, 3, 4)
  ↓
PC2, PC3, PC4 reciben (aunque solo era para PC3)
```

**Problemas:**
❌ Colisiones constantes  
❌ Ancho de banda compartido  
❌ Sniffing trivial (Wireshark ve TODO)  
❌ Half-duplex (no puede TX y RX simultáneamente)

**Ya NADIE los usa** (reemplazados por switches económicos)

---

### SWITCH (Capa 2 - Fundamental)

**¿Qué hace?**  
Aprende direcciones MAC y envía frames solo al puerto destino.

#### **Funcionamiento interno:**

```
1. APRENDIZAJE (Learning):
   
   PC1 (MAC: AA:AA) conectado a puerto 1
   Envía frame:
   
   [Src MAC: AA:AA | Dst MAC: BB:BB | Data]
   
   Switch aprende:
   Puerto 1 → MAC AA:AA
   
   CAM Table (Content Addressable Memory):
   ┌──────────┬─────────┐
   │ MAC Addr │ Port    │
   ├──────────┼─────────┤
   │ AA:AA    │ 1       │
   └──────────┴─────────┘

2. FORWARDING:
   
   Si switch conoce MAC destino:
   → Envía SOLO a ese puerto (unicast)
   
   Si NO conoce MAC destino:
   → Envía a TODOS los puertos (flooding)
   
   Si es broadcast (FF:FF:FF:FF:FF:FF):
   → Envía a TODOS los puertos (menos origen)

3. AGING:
   
   Entradas en CAM table expiran después de 300 segundos
   (configurable)
```

#### **Ataques contra Switches:**

**1. MAC Flooding**

```bash
# Llenar la CAM table con MACs falsas
# Herramienta: macof (dsniff)

sudo macof -i eth0

# Switch se satura:
# CAM table llena → Switch actúa como HUB
# Todos los frames se broadcast
# Atacante puede sniffar todo
```

**Mitigación:**
```
✓ Port Security (limitar MACs por puerto)
✓ Dynamic ARP Inspection (DAI)
✓ Storm Control
```

**2. VLAN Hopping**

```
Atacante en VLAN 10 quiere acceder a VLAN 20

Técnica: Double Tagging
1. Envía frame con 2 tags VLAN:
   [Ethernet | 802.1Q Tag1: VLAN 10 | 802.1Q Tag2: VLAN 20 | Data]

2. Primer switch quita Tag1 (cree que es para VLAN 10)
3. Frame con Tag2 llega a segundo switch
4. Segundo switch procesa Tag2 → Frame entra a VLAN 20

Atacante saltó entre VLANs
```

**Mitigación:**
```
✓ NO usar VLAN 1 (native VLAN default)
✓ Deshabilitar DTP (Dynamic Trunking Protocol)
✓ Configurar trunk ports manualmente
```

---

### ROUTER (Capa 3 - Conexión de Redes)

**¿Qué hace?**  
Conecta diferentes redes (diferentes subnets) y decide mejor ruta.

#### **Funcionamiento:**

```
Routing Table:

┌─────────────────┬──────────┬──────────┬────────┐
│ Destination     │ Mask     │ Gateway  │ Iface  │
├─────────────────┼──────────┼──────────┼────────┤
│ 192.168.1.0     │ /24      │ 0.0.0.0  │ eth0   │ ← Directly connected
│ 192.168.2.0     │ /24      │ 0.0.0.0  │ eth1   │ ← Directly connected
│ 10.0.0.0        │ /8       │ 1.2.3.4  │ eth2   │ ← Via otro router
│ 0.0.0.0         │ /0       │ 8.8.8.8  │ eth2   │ ← Default route
└─────────────────┴──────────┴──────────┴────────┘

Proceso:
1. Paquete llega: Dst IP = 192.168.2.50
2. Router consulta tabla
3. Match: 192.168.2.0/24 → eth1
4. Router envía paquete por eth1
```

#### **Tipos de Rutas:**

**1. Rutas Directamente Conectadas**
```
Router tiene IP en esa red
No necesita gateway
```

**2. Rutas Estáticas**
```
Configuradas manualmente por admin
ip route 10.0.0.0/8 via 1.2.3.4

Ventajas: Control total, predecible
Desventajas: No se adapta a cambios
```

**3. Rutas Dinámicas (Protocolos de Routing)**
```
RIP (Routing Information Protocol)
OSPF (Open Shortest Path First)
BGP (Border Gateway Protocol) ← Internet usa esto

Routers se comunican y comparten rutas
Se adaptan automáticamente a fallos
```

#### **Ataques contra Routers:**

**1. IP Spoofing**

```bash
# Enviar paquete con IP origen falsa
sudo hping3 -a 8.8.8.8 -S -p 80 192.168.1.1

# -a = spoof source IP
# Respuesta irá a 8.8.8.8 (no a atacante)
```

**Mitigación:**
```
✓ Ingress filtering (RFC 2827)
✓ uRPF (Unicast Reverse Path Forwarding)
✓ ACLs en interfaces
```

**2. BGP Hijacking (Nivel ISP)**

```
ISP malicioso anuncia que tiene mejor ruta a IP X
Tráfico global se desvía hacia él
Puede interceptar, modificar, dropar tráfico

Ejemplo real: 
• YouTube hijack (2008, Pakistán)
• Amazon Route 53 hijack (2018)
```

**Mitigación:**
```
✓ RPKI (Resource Public Key Infrastructure)
✓ BGP route filtering
✓ Peering agreements con validación
```

---

### FIREWALL (Capa 3-7 - Seguridad)

**¿Qué hace?**  
Filtra tráfico basándose en reglas de seguridad.

#### **Tipos de Firewall:**

**1. Packet Filter (Stateless)**

```
Inspecciona cada paquete individualmente
NO recuerda sesiones

Ejemplo de regla:
ALLOW TCP from 192.168.1.0/24 to ANY port 80

Problema:
No detecta si paquete es parte de sesión legítima
```

**2. Stateful Firewall**

```
Mantiene tabla de conexiones (state table)

┌────────┬──────────┬──────────┬────────┬──────────┐
│ Src IP │ Src Port │ Dst IP   │ Dst Pt │ State    │
├────────┼──────────┼──────────┼────────┼──────────┤
│ 1.2.3.4│ 54321    │ 5.6.7.8  │ 80     │ ESTAB    │
│ 2.3.4.5│ 12345    │ 6.7.8.9  │ 443    │ SYN_SENT │
└────────┴──────────┴──────────┴────────┴──────────┘

Solo permite paquetes que pertenecen a sesión conocida
```

**3. Next-Generation Firewall (NGFW)**

```
Stateful + Inspección profunda de paquetes (DPI)

Características:
✓ Application awareness (identifica apps)
✓ Intrusion Prevention System (IPS)
✓ SSL/TLS inspection
✓ User-based policies
✓ Threat intelligence integration

Ejemplo: Palo Alto, Fortinet, Cisco Firepower
```

#### **Reglas de Firewall (Ejemplo):**

```
# Formato típico:
[Action] [Protocol] [Source] [Destination] [Port] [State]

Ejemplos:

1. ALLOW TCP from 192.168.1.0/24 to ANY port 80,443
   → Usuarios internos pueden navegar web

2. DENY TCP from ANY to 192.168.1.10 port 3389
   → Bloquear RDP desde Internet

3. ALLOW TCP from 10.0.0.5 to 192.168.1.100 port 22 state NEW,ESTABLISHED
   → Admin puede SSH a servidor

4. DROP ALL from ANY to ANY
   → Default deny (mejor práctica)
```

**Orden de evaluación:**
```
CRÍTICO: Reglas se evalúan de arriba a abajo
Primera regla que hace match se aplica
Resto se ignoran

Ejemplo:
Rule 1: ALLOW TCP from ANY to ANY port 80
Rule 2: DENY TCP from 192.168.1.50 to ANY port 80

192.168.1.50 PUEDE acceder puerto 80
(Rule 1 hace match primero)

CORRECTO:
Rule 1: DENY TCP from 192.168.1.50 to ANY port 80
Rule 2: ALLOW TCP from ANY to ANY port 80
```

---

## 1.7 - EJERCICIO PRÁCTICO: IDENTIFICAR TU RED

### Lab 1: Mapear tu Red Casera

**Objetivo:** Documentar tu red doméstica.

**Pasos:**

```bash
# 1. Identificar tu configuración IP
ip addr show  # Linux
ipconfig /all  # Windows

# Anota:
# - Tu IP: _________________
# - Máscara: _______________
# - Gateway: _______________
# - DNS: ___________________

# 2. Identificar otros dispositivos
nmap -sn 192.168.1.0/24

# 3. Dibujar topología
# Usa papel o herramienta online: draw.io

Ejemplo:
     [Internet]
         |
    [Router ISP] 192.168.1.1
         |
    ┌────┴────┬──────────┬─────────┐
[Tu PC]   [Smart TV]  [Celular]  [Laptop]
.100       .150        .151      .152
```

**Entregable:**
- Diagrama de tu red
- Lista de dispositivos con IPs
- Identificación de vulnerabilidades (ej: router con admin/admin)

**Documenta en GitHub:**
```bash
cd ~/ciberseguridad-portfolio/01-fundamentos
mkdir red-casera
nano red-casera/README.md
# Incluir diagrama y análisis
```

---

## ✅ CHECKPOINT DÍA 8-9

### Puedes responder sin ayuda:

- [ ] ¿Qué es una red en términos técnicos?
- [ ] ¿Diferencia entre dirección MAC e IP?
- [ ] ¿Qué es un dominio de broadcast?
- [ ] ¿Hub vs Switch vs Router?
- [ ] ¿Qué topología usa tu casa/trabajo?
- [ ] ¿Qué es un firewall stateful?

### Habilidades prácticas:

- [ ] Identificar dispositivos de tu red con `nmap`
- [ ] Ver tabla CAM de un switch (si tienes acceso)
- [ ] Dibujar topología de red conocida

### Errores comunes para evitar:

❌ "Switch es como un hub más rápido"  
✅ Switch es inteligente (aprende MACs,