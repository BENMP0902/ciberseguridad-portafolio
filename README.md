# 🔐 Portafolio de Ciberseguridad — Benjamín Martínez Pérez

> Repositorio de aprendizaje y proyectos de seguridad ofensiva y defensiva.
> Diario técnico verificable: cada entrada refleja trabajo real ejecutado.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue)](https://www.linkedin.com/in/benjam%C3%ADn-mart%C3%ADnez-p%C3%A9rez-17949434b/)
[![GitHub](https://img.shields.io/badge/GitHub-BENMP0902-181717?logo=github)](https://github.com/BENMP0902)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-benjamin2401128-c5e851?logo=tryhackme)](https://tryhackme.com/p/FATBSTRD9992)

---

## 👤 Sobre mí

Estudiante de **Ingeniería de Software** Hybridge Education

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

## 🛠️ Estado actual del laboratorio (Mayo 2026)

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

## 📅 Roadmap del semestre — Ciberseguridad y Hacking Ético

Materia inicia: **4 mayo 2026** | Universidad: Hybridge Education

- [x] Setup del laboratorio (VirtualBox + Kali + Ubuntu + Windows 7 + Metasploitable)
- [x] Cuentas creadas: TryHackMe, HackTheBox, PicoCTF, PortSwigger Academy
- [x] Configuración de Git, gitleaks pre-commit hook, .gitignore robusto
- [ ] Completar TryHackMe — Pre-Security Path
- [ ] Completar TryHackMe — Cyber Security 101 / SOC Level 1
- [ ] Resolver primera máquina HTB **retirada** con writeup formal estilo OSCP
- [ ] Estudio aplicado de OWASP Top 10 (2021)
- [ ] Estudio aplicado de MITRE ATT&CK Framework
- [ ] Implementar primer script propio (port scanner en Bash → Python)
- [ ] Documentar metodología de pentest según PTES

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

## 📁 Estructura del repositorio

```
.
├── 01-fundamentos/        # Notas teóricas: networking, RFCs, OWASP, MITRE
├── 02-laboratorio/        # Documentación del homelab y topología
├── 03-writeups/           # Writeups de máquinas RETIRADAS (HTB) y rooms (TryHackMe)
│   ├── tryhackme/
│   └── hackthebox/        # solo retiradas — política HTB ToS
├── 04-scripts/            # Scripts propios sanitizados
│   ├── bash/
│   └── python/
├── 05-cheatsheets/        # Referencias rápidas personales
└── 06-recursos/           # Links curados, RFCs, papers
```

---

## 📜 Cheatsheets y referencias

- [Git esencial](./05-cheatsheets/cheatsheet_git_esencial.md)
- [RFCs de networking](./06-recursos/links.md)

---

## 🔄 Política de actualización

Cadencia semanal o tras hito relevante. Cada commit refleja trabajo real.

**No publico writeups de máquinas HTB activas** — política HTB ToS. Sólo cuando son retiradas.

---

## ⚠️ Disclaimer legal y ético

Todo el material aquí publicado se realiza en **entornos de laboratorio aislados** (homelab personal, VPNs autorizadas, plataformas educativas con permiso explícito como HTB y TryHackMe). El contenido es educativo y se rige por principios de **hacking ético**.

Ningún contenido aquí publicado debe usarse para acceder a sistemas sin autorización explícita del propietario. Auditar sistemas ajenos sin consentimiento es ilegal bajo el **Artículo 211 bis del Código Penal Federal Mexicano** y leyes equivalentes en otras jurisdicciones (ej. *Computer Fraud and Abuse Act* en EE.UU.).

---

*Última actualización: 4 de mayo de 2026*