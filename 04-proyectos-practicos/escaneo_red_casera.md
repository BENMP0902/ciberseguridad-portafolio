# 🏠 Escaneo de Red Casera
## Objetivo
Identificar todos los dispositivos en mi red doméstica y documentar hallazgos.
## Herramientas
- Nmap 7.94
- Kali Linux 2024
## Metodología
### 1. Identificar mi red
\`\`\`bash
ip addr show
# Mi IP: 192.168.1.100/24
# Gateway: 192.168.1.1
\`\`\`
### 2. Escaneo de descubrimiento
\`\`\`bash
nmap -sn 192.168.1.0/24 > scan_results.txt
\`\`\`
## Resultados
| IP | MAC | Fabricante | Dispositivo |
|----|-----|------------|-------------|
| 192.168.1.1 | AA:BB:CC:DD:EE:FF | TP-Link | Router |
| 192.168.1.50 | 11:22:33:44:55:66 | Samsung | Smart TV |
| 192.168.1.100 | ... | Intel | Mi laptop |
## Hallazgos de Seguridad
⚠ **Vulnerabilidades encontradas:**
1. Router con credenciales default (admin/admin)
2. Smart TV con puerto 23 (Telnet) abierto
3. Sin segmentación de red (todo en misma VLAN)
## Recomendaciones
1. Cambiar password del router
2. Deshabilitar Telnet en Smart TV
3. Crear VLAN para dispositivos IoT
---
*Fecha: 3 Enero 2025*