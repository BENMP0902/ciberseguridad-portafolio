# 🔐 Portafolio de Ciberseguridad

> Repositorio de aprendizaje y proyectos de seguridad ofensiva y defensiva.
> Diario técnico verificable: cada entrada refleja trabajo real ejecutado.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue)](https://www.linkedin.com/in/benjam%C3%ADn-mart%C3%ADnez-p%C3%A9rez-17949434b/)
[![GitHub](https://img.shields.io/badge/GitHub-BENMP0902-181717?logo=github)](https://github.com/BENMP0902)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-benjamin2401128-c5e851?logo=tryhackme)](https://tryhackme.com/p/FATBSTRD9992)

---

## 👤 Sobre mí

Estudiante de **Ingeniería de Software** en Hybridge Education.

Perfil híbrido: 7+ años de experiencia previa en roles de ventas, liderazgo de equipos y gestión operativa, ahora orientado al desarrollo de software con foco emergente en **seguridad ofensiva** y **arquitectura de redes seguras**.

---

## 🎯 Objetivo profesional

- **Horizonte 18–24 meses:** Junior Penetration Tester o Network Security Engineer.
- **Meta de certificación:** OSCP (Offensive Security Certified Professional).
- **Áreas de interés:** Network security, infrastructure pentesting, cloud security (OCI/AWS), red team operations.

---

## 📚 Background técnico previo

Conocimientos consolidados antes de iniciar formación formal en ciberseguridad:

- **Cloud (Oracle Cloud Infrastructure):** VCN, subredes públicas/privadas, NAT Gateway, Bastion Host, Zero Trust, microsegmentación.
- **Backend Development:** Node.js + Express + Sequelize + PostgreSQL (Supabase). API REST con autenticación JWT (Passport.js — LocalStrategy + JwtStrategy).
- **Linux:** Kali (WSL2 y VM), Ubuntu Server, navegación CLI, Bash scripting.
- **Networking fundamentals:** modelo OSI/TCP-IP, RFCs base (791 IPv4, 1918 direccionamiento privado).
- **Automation:** n8n workflows, ETL pipelines.
- **Machine Learning:** TensorFlow/Keras (CIFAR-10, transfer learning con MobileNetV2).

---

## 🛠️ Estado actual del laboratorio

Entorno de práctica montado y operativo en VirtualBox sobre Windows 11:

| VM | Rol | Estado |
|---|---|---|
| Kali Linux 2 | Atacante (offensive) | ✅ Activa |
| Kali-Attack | Atacante secundario / snapshot | ✅ Activa |
| Ubuntu / Ubuntu Server | Víctima Linux | ✅ Activa |
| Ubuntu-SOC | Defensor / Blue team | 🔄 En setup |
| Windows 7 | Víctima legacy (MS17-010, MS08-067) | ✅ Activa |
| Metasploit (Metasploitable) | Víctima vulnerable intencional | ✅ Activa |

**Backup:** Kali en WSL2 sobre Windows 11 host para tareas no dependientes de raw socket.

---

## 📖 En curso ahora — TryHackMe (Bronze League)

Rooms iniciados durante semana 1 del curso:

- 🔄 **Pyramid of Pain** — clasificación de IoCs por dificultad de cambio para el adversario
- 🔄 **Junior Security Analyst Intro** — día en la vida de un SOC analyst
- 🔄 **Putting it all together** — fundamentos de cómo funciona la web
- 🔄 **How Websites Work** — frontend/backend, requests, rendering
- 🔄 **HTTP in Detail** — request/response cycle, métodos, status codes

Evidencia verificable en mi [perfil público de TryHackMe](https://tryhackme.com/p/benjamin2401128).

---

## 📂 Proyectos publicados

| Proyecto | Ubicación | Descripción |
|---|---|---|
| **Auditoría de red doméstica** | [`04-proyectos-practicos/escaneo_red_casera.md`](./04-proyectos-practicos/escaneo_red_casera.md) | Identificación de dispositivos en LAN, hallazgos de seguridad SOHO, recomendaciones priorizadas. Sanitizado con RFC 5737 / RFC 7042. |
| **Reconocimiento — target educativo (sesiones 01–02)** | [`04-proyectos-practicos/recon_edu_target/`](./04-proyectos-practicos/recon_edu_target/) | Reconocimiento pasivo y activo sobre target del ámbito educativo. Incluye incident report por bloqueo de IP tras escaneo masivo accidental. Sanitizado con RFC 5737 / RFC 2606. |

---

## 📁 Estructura del repositorio

```
.
├── 01-fundamentos/         # Notas teóricas: networking, RFCs, OWASP, MITRE
├── 02-reconocimiento/      # Notas y ejercicios de la fase de recon
├── 03-vulnerabilidades/    # Notas y análisis de vulnerabilidades
├── 04-proyectos-practicos/ # Trabajo aplicado completado
│   ├── escaneo_red_casera.md
│   ├── home-network-scan/
│   └── recon_edu_target/
├── 05-writeups/            # Writeups de máquinas RETIRADAS y rooms
│   └── tryhackme/
│       └── hackthebox/     # solo retiradas — política HTB ToS
├── 06-scripts/             # Scripts propios sanitizados
│   ├── bash/
│   └── python/
├── 07-labs/                # Labs prácticos por herramienta
│   ├── nmap/
│   ├── wireshark/
│   └── mestasploit/
├── notas/                  # Notas día a día del proceso
└── recursos/               # Cheatsheets y referencias
```

---

## 📜 Cheatsheets y referencias

- [Git esencial](./recursos/cheatsheet_git_esencial.md)
- [Comandos esenciales para ciberseguridad](./recursos/commands_cheatsheet.md)

---

## 🔄 Política de actualización

Cadencia semanal o tras hito relevante. Cada commit refleja trabajo real.

**No publico writeups de máquinas HTB activas** — política HTB ToS. Sólo cuando son retiradas.

---

## ⚠️ Disclaimer legal y ético

Todo el material aquí publicado se realiza en **entornos de laboratorio aislados** (homelab personal, VPNs autorizadas, plataformas educativas con permiso explícito como HTB y TryHackMe). El contenido es educativo y se rige por principios de **hacking ético**.

Los proyectos sobre infraestructura externa están sanitizados (IPs, hostnames y dominios reemplazados según RFC 5737 y RFC 2606) para evitar identificación de targets reales.

Ningún contenido aquí publicado debe usarse para acceder a sistemas sin autorización explícita del propietario. Auditar sistemas ajenos sin consentimiento es ilegal bajo el **Artículo 211 bis del Código Penal Federal Mexicano** y leyes equivalentes en otras jurisdicciones (ej. *Computer Fraud and Abuse Act* en EE.UU.).
