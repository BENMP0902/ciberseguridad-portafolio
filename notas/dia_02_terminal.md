# 📅 DÍA 2: DOMINIO DE TERMINAL LINUX

## 🎯 OBJETIVO
Pasar de nivel 2 (básico) a nivel 5 (competente) en línea de comandos.

---

## PARTE 2: NAVEGACIÓN ESENCIAL

### 1. `pwd` - Print Working Directory

**¿Qué hace?**  
Te dice DÓNDE estás en el sistema de archivos.

```bash
pwd
# Output: /home/kali

# Siempre ejecuta pwd si te pierdes
```

**Estructura de directorios Linux:**

```
/                           ← Raíz (root)
├── home/                   ← Directorios de usuarios
│   ├── kali/              ← Tu carpeta personal
│   └── otheruser/
├── root/                   ← Home del usuario root
├── etc/                    ← Archivos de configuración
├── var/                    ← Logs, bases de datos variables
│   └── log/               ← LOGS (importante en seguridad)
├── tmp/                    ← Archivos temporales (se borran)
├── opt/                    ← Software opcional
├── usr/                    ← Programas de usuario
│   ├── bin/               ← Binarios (programas)
│   └── share/             ← Datos compartidos
└── bin/                    ← Binarios esenciales del sistema
```

**Atajos importantes:**
```
~     = Tu home (/home/kali)
/     = Raíz del sistema
.     = Directorio actual
..    = Directorio padre (un nivel arriba)
-     = Directorio anterior (último donde estuviste)
```

---

### 2. `ls` - List

**¿Qué hace?**  
Lista archivos y directorios.

#### **Uso básico:**

```bash
# Listar contenido
ls

# Listar con detalles (long format)
ls -l

# Listar TODO (incluyendo ocultos)
ls -a

# Listar con tamaños legibles
ls -lh

# COMBINACIÓN PERFECTA (la usarás TODO el tiempo)
ls -lah
```

#### **Entendiendo el output de `ls -l`:**

```bash
ls -l /home/kali/script.sh

-rwxr-xr-x 1 kali kali 2048 Jan 15 14:30 script.sh
│   │  │  │ │    │    │    │            │
│   │  │  │ │    │    │    │            └─ Nombre
│   │  │  │ │    │    │    └─ Fecha de modificación
│   │  │  │ │    │    └─ Tamaño (bytes)
│   │  │  │ │    └─ Grupo dueño
│   │  │  │ └─ Usuario dueño
│   │  │  └─ # de hard links
│   │  └─ Permisos para "otros"
│   └─ Permisos para "grupo"
└─ Tipo y permisos para "dueño"
```

**Desglose de permisos:**

```
-rwxr-xr-x
│││││││││└─ Execute (otros)
││││││││└─ Write (otros)
│││││││└─ Read (otros)
││││││└─ Execute (grupo)
│││││└─ Write (grupo)
││││└─ Read (grupo)
│││└─ Execute (dueño)
││└─ Write (dueño)
│└─ Read (dueño)
└─ Tipo: - = archivo, d = directorio, l = link

rwx = 7 (binario 111)
r-x = 5 (binario 101)
r-- = 4 (binario 100)
--- = 0 (binario 000)

Entonces: -rwxr-xr-x = 755
```

#### **Opciones útiles:**

```bash
# Ordenar por fecha (más reciente primero)
ls -lt

# Ordenar por tamaño
ls -lS

# Recursivo (mostrar subdirectorios)
ls -R

# Solo directorios
ls -d */

# Con colores (normalmente ya está por defecto en Kali)
ls --color=auto
```

#### **Archivos ocultos:**

```bash
# Archivos que empiezan con . están ocultos
ls
# Output: Documents Downloads script.sh

ls -a
# Output: . .. .bashrc .profile Documents Downloads script.sh
#         ↑ ↑  ↑────── Archivos ocultos
#         │ └─ Directorio padre
#         └─ Directorio actual
```

---

### 3. `cd` - Change Directory

**¿Qué hace?**  
Te mueve entre directorios.

```bash
# Ir a un directorio específico
cd /home/kali/Documents

# Ir a home
cd ~
# O simplemente:
cd

# Subir un nivel
cd ..

# Subir dos niveles
cd ../..

# Ir al directorio anterior
cd -

# Ir a raíz
cd /
```

#### **Rutas Absolutas vs Relativas:**

```bash
# RUTA ABSOLUTA (empieza con /)
cd /home/kali/Documents/proyectos
# Funciona desde CUALQUIER lugar

# RUTA RELATIVA (NO empieza con /)
# Estás en: /home/kali
cd Documents/proyectos
# Solo funciona si estás en /home/kali

# Ejemplo práctico:
pwd
# /home/kali/Documents

cd ../Downloads
# Subes a /home/kali, luego entras a Downloads
# Ahora estás en: /home/kali/Downloads
```

#### **Ejercicio de navegación:**

```bash
# 1. Ve a tu home
cd ~

# 2. Crea estructura de práctica
mkdir -p practica/nivel1/nivel2/nivel3

# 3. Ve al nivel más profundo
cd practica/nivel1/nivel2/nivel3

# 4. ¿Dónde estás?
pwd
# /home/kali/practica/nivel1/nivel2/nivel3

# 5. Sube dos niveles
cd ../..
pwd
# /home/kali/practica/nivel1

# 6. Vuelve a nivel3 en un comando
cd nivel2/nivel3

# 7. Ve a home en un salto
cd ~

# 8. Vuelve donde estabas
cd -
pwd
# /home/kali/practica/nivel1/nivel2/nivel3
```

---

### 4. `mkdir` - Make Directory

**¿Qué hace?**  
Crea directorios (carpetas).

```bash
# Crear un directorio
mkdir mi_carpeta

# Crear múltiples directorios
mkdir carpeta1 carpeta2 carpeta3

# Crear estructura completa (parents)
mkdir -p proyectos/web/frontend/components
# Crea toda la ruta aunque no exista

# Crear con permisos específicos
mkdir -m 755 carpeta_publica

# Ver lo que creas
mkdir -v nueva_carpeta
# Output: mkdir: created directory 'nueva_carpeta'
```

#### **Estructura para el curso:**

```bash
# Crea tu estructura de trabajo
cd ~
mkdir -p ciberseguridad/{labs,notas,proyectos,scripts,capturas}

# Verificar
ls ciberseguridad/
# Output: labs  notas  proyectos  scripts  capturas

# Crear subdirectorios
mkdir -p ciberseguridad/labs/{nmap,wireshark,metasploit}
mkdir -p ciberseguridad/scripts/{bash,python}

# Ver estructura completa
tree ciberseguridad
# Si no tienes tree: sudo apt install tree
```

---

### 5. `touch` - Crear Archivo Vacío

**¿Qué hace?**  
Crea archivo vacío o actualiza timestamp.

```bash
# Crear archivo
touch archivo.txt

# Crear múltiples archivos
touch file1.txt file2.txt file3.txt

# Crear con ruta
touch ~/ciberseguridad/notas/dia2.md

# Actualizar timestamp de archivo existente
touch archivo_viejo.txt
# (Fecha de modificación se actualiza a ahora)
```

---

## 📄 PARTE 3: MANIPULACIÓN DE ARCHIVOS (25 minutos)

### 6. `cat` - Concatenate and Display

**¿Qué hace?**  
Muestra contenido de archivos.

```bash
# Ver contenido
cat archivo.txt

# Ver múltiples archivos
cat file1.txt file2.txt

# Concatenar archivos en uno nuevo
cat file1.txt file2.txt > combined.txt

# Ver con números de línea
cat -n archivo.txt

# Ver caracteres especiales
cat -A archivo.txt
# $ = fin de línea, ^I = tab
```

**Cuándo NO usar cat:**
```bash
# ❌ Para archivos grandes
cat /var/log/syslog  # Puede ser 500MB+

# ✅ Usa less o head/tail en su lugar
```

---

### 7. `less` - Paginador

**¿Qué hace?**  
Ver archivos grandes paginando (como un libro).

```bash
# Ver archivo
less /var/log/syslog

# Controles dentro de less:
# Espacio    = Página siguiente
# b          = Página anterior
# /texto     = Buscar "texto"
# n          = Siguiente resultado
# N          = Resultado anterior
# G          = Ir al final
# g          = Ir al inicio
# q          = Salir

# Ver con números de línea
less -N archivo.txt

# Ver múltiples archivos
less file1.txt file2.txt
# :n = siguiente archivo
# :p = archivo anterior
```

---

### 8. `head` y `tail` - Ver Inicio/Final

```bash
# Ver primeras 10 líneas (default)
head archivo.txt

# Ver primeras N líneas
head -n 20 archivo.txt
# O simplemente:
head -20 archivo.txt

# Ver últimas 10 líneas
tail archivo.txt

# Ver últimas N líneas
tail -n 50 archivo.txt

# SEGUIR archivo en tiempo real (logs)
tail -f /var/log/syslog
# Ctrl+C para detener

# Seguir múltiples archivos
tail -f /var/log/syslog /var/log/auth.log

# Ver líneas nuevas desde ahora
tail -f --since=now /var/log/syslog
```

**Uso en Seguridad:**
```bash
# Monitorear intentos de login
sudo tail -f /var/log/auth.log | grep Failed

# Ver últimos 100 eventos de firewall
sudo tail -100 /var/log/ufw.log

# Seguir conexiones en tiempo real
sudo tcpdump -i eth0 | tee capture.log
```

---

### 9. `cp` - Copy

```bash
# Copiar archivo
cp origen.txt destino.txt

# Copiar a otro directorio
cp archivo.txt /home/kali/Documents/

# Copiar directorio (recursivo)
cp -r carpeta/ /backup/

# Copiar manteniendo permisos y timestamps
cp -p archivo.txt backup.txt

# Copiar con confirmación
cp -i archivo.txt destino.txt
# Pregunta si sobrescribir

# Copiar verboso (mostrar progreso)
cp -v archivo.txt destino.txt

# Copiar solo si es más nuevo
cp -u archivo.txt destino.txt
```

**Backup rápido:**
```bash
# Backup de archivo importante
cp script.sh script.sh.backup

# Backup con timestamp
cp script.sh script.sh.$(date +%Y%m%d)
# Resultado: script.sh.20250103
```

---

### 10. `mv` - Move/Rename

```bash
# Renombrar archivo
mv viejo.txt nuevo.txt

# Mover archivo
mv archivo.txt /home/kali/Documents/

# Mover directorio
mv carpeta/ /otro/lugar/

# Mover múltiples archivos
mv file1.txt file2.txt file3.txt /destino/

# Mover con confirmación
mv -i archivo.txt destino.txt

# Mover solo si es más nuevo
mv -u archivo.txt destino.txt
```

**Renombrado masivo:**
```bash
# Renombrar .txt a .md
for file in *.txt; do
    mv "$file" "${file%.txt}.md"
done
```

---

### 11. `rm` - Remove (⚠️ PELIGROSO)

```bash
# Eliminar archivo
rm archivo.txt

# Eliminar múltiples archivos
rm file1.txt file2.txt

# Eliminar con confirmación
rm -i archivo.txt

# Eliminar directorio vacío
rmdir carpeta/

# Eliminar directorio con contenido
rm -r carpeta/

# Forzar eliminación (SIN CONFIRMACIÓN)
rm -rf carpeta/
# ⚠️ PELIGRO: No pide confirmación, elimina TODO

# Eliminar archivos que coincidan con patrón
rm *.log
rm test_*.txt

# Ver qué se eliminará (dry-run con echo)
echo rm *.log
# Luego ejecuta sin echo
```

**⚠️ ADVERTENCIAS CRÍTICAS:**

```bash
# ❌ NUNCA EJECUTES ESTO (destruye todo el sistema)
sudo rm -rf /
# Linux moderno lo previene, pero NO lo pruebes

# ❌ CUIDADO con espacios
rm -rf carpeta /
# Elimina carpeta Y luego intenta eliminar /

# ✅ CORRECTO
rm -rf carpeta/

# ✅ Usar trash en lugar de rm permanente
# Instalar: sudo apt install trash-cli
trash archivo.txt  # Mueve a papelera
trash-list         # Ver papelera
trash-restore      # Restaurar
```

---

## 🔍 PARTE 4: BÚSQUEDA Y FILTRADO (20 minutos)

### 12. `find` - Buscar Archivos

**Sintaxis básica:**
```bash
find [donde_buscar] [criterio] [acción]
```

#### **Por nombre:**

```bash
# Buscar archivo específico
find /home/kali -name "script.sh"

# Buscar case-insensitive
find /home/kali -iname "script.sh"
# Encuentra: script.sh, Script.sh, SCRIPT.SH

# Buscar con wildcard
find /home/kali -name "*.txt"
find /etc -name "*.conf"

# Buscar directorios
find /home/kali -type d -name "proyectos"

# Buscar solo archivos
find /home/kali -type f -name "*.log"
```

#### **Por tamaño:**

```bash
# Archivos mayores a 100MB
find /var -type f -size +100M

# Archivos menores a 10KB
find /home -type f -size -10k

# Archivos exactamente 1GB
find / -type f -size 1G

# Unidades: c=bytes, k=KB, M=MB, G=GB
```

#### **Por fecha:**

```bash
# Modificados en últimas 24 horas
find /home/kali -type f -mtime -1

# Modificados hace más de 7 días
find /home/kali -type f -mtime +7

# Modificados hace exactamente 2 días
find /home/kali -type f -mtime 2

# Accedidos en última hora
find /var/log -type f -amin -60

# Creados en última semana
find /home/kali -type f -ctime -7
```

#### **Por permisos:**

```bash
# Archivos con SUID (escalación de privilegios)
find / -perm -4000 -type f 2>/dev/null

# Archivos con SGID
find / -perm -2000 -type f 2>/dev/null

# Archivos escribibles por todos
find / -perm -002 -type f 2>/dev/null

# Archivos ejecutables
find /home/kali -type f -executable
```

#### **Por usuario/grupo:**

```bash
# Archivos de usuario específico
find /home -user kali

# Archivos de grupo específico
find /var -group www-data

# Archivos sin dueño (huérfanos)
find / -nouser 2>/dev/null
```

#### **Ejecutar acciones:**

```bash
# Eliminar archivos encontrados
find /tmp -name "*.tmp" -delete

# Ejecutar comando en cada resultado
find /home/kali -name "*.txt" -exec cat {} \;

# Con confirmación
find /home/kali -name "*.log" -ok rm {} \;

# Copiar archivos encontrados
find /var/log -name "*.log" -exec cp {} /backup/ \;

# Cambiar permisos
find /home/kali/scripts -name "*.sh" -exec chmod +x {} \;
```

#### **Combinaciones complejas:**

```bash
# Archivos .txt modificados en última semana mayores a 1MB
find /home -name "*.txt" -type f -mtime -7 -size +1M

# Archivos PHP con permisos 777 (peligroso)
find /var/www -name "*.php" -perm 0777

# Logs mayores a 100MB y más viejos de 30 días
find /var/log -name "*.log" -size +100M -mtime +30 -delete
```

**Uso en Seguridad:**
```bash
# Buscar archivos con SUID (posible escalación)
find / -perm -4000 -type f -ls 2>/dev/null

# Buscar archivos ocultos sospechosos
find /home -name ".*" -type f

# Buscar scripts ejecutables en home (backdoors)
find /home -name "*.sh" -o -name "*.py" -type f -executable

# Buscar archivos modificados hoy (posible compromiso)
find /etc -type f -mtime 0
```

---

### 13. `grep` - Buscar Texto en Archivos

**Sintaxis:**
```bash
grep [opciones] "patrón" archivo(s)
```

#### **Uso básico:**

```bash
# Buscar palabra en archivo
grep "error" logfile.txt

# Buscar en múltiples archivos
grep "password" *.txt

# Buscar recursivamente en directorios
grep -r "TODO" /home/kali/proyectos/

# Case-insensitive
grep -i "error" logfile.txt
# Encuentra: Error, ERROR, error

# Mostrar número de línea
grep -n "error" logfile.txt
# Output: 42:This is an error message

# Contar ocurrencias
grep -c "error" logfile.txt
# Output: 15
```

#### **Invertir búsqueda:**

```bash
# Mostrar líneas que NO contienen "DEBUG"
grep -v "DEBUG" app.log

# Útil para filtrar
grep -v "^#" config.txt  # Líneas sin comentarios
grep -v "^$" file.txt    # Líneas no vacías
```

#### **Expresiones regulares:**

```bash
# Buscar líneas que empiezan con "Error"
grep "^Error" logfile.txt

# Buscar líneas que terminan con "failed"
grep "failed$" logfile.txt

# Buscar IPs (simple)
grep -E "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" logfile.txt

# Buscar emails
grep -E "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b" file.txt

# Buscar palabras completas
grep -w "error" logfile.txt
# Encuentra "error" pero NO "errors" ni "terrorista"
```

#### **Contexto:**

```bash
# Mostrar 3 líneas ANTES del match
grep -B 3 "error" logfile.txt

# Mostrar 3 líneas DESPUÉS del match
grep -A 3 "error" logfile.txt

# Mostrar 3 líneas antes Y después
grep -C 3 "error" logfile.txt
```

#### **Colores y formato:**

```bash
# Resaltar matches en color
grep --color=auto "error" logfile.txt

# Mostrar solo el match (no toda la línea)
grep -o "error" logfile.txt

# Mostrar solo nombres de archivos con match
grep -l "password" *.txt

# Mostrar archivos SIN match
grep -L "password" *.txt
```

**Uso en Seguridad:**
```bash
# Buscar intentos de login fallidos
sudo grep "Failed password" /var/log/auth.log

# Buscar IPs específicas en logs
grep "192.168.1.50" /var/log/apache2/access.log

# Buscar palabras clave sospechosas
grep -ri "eval\|exec\|system" /var/www/

# Buscar errores SQL injection
grep -i "union select" /var/log/apache2/access.log

# Buscar accesos a archivos sensibles
grep "/etc/passwd" /var/log/apache2/access.log
```

---

## 🔐 PARTE 5: PERMISOS Y OWNERSHIP (15 minutos)

### Entender Permisos Linux

```
-rwxr-xr-x
 │││││││││
 ││││││││└─ Execute (otros)
 │││││││└─ Write (otros)
 ││││││└─ Read (otros)
 │││││└─ Execute (grupo)
 ││││└─ Write (grupo)
 │││└─ Read (grupo)
 ││└─ Execute (dueño)
 │└─ Write (dueño)
 └─ Read (dueño)

Valores octales:
r (read)    = 4
w (write)   = 2
x (execute) = 1

Ejemplos:
rwx = 4+2+1 = 7
rw- = 4+2+0 = 6
r-x = 4+0+1 = 5
r-- = 4+0+0 = 4
--- = 0+0+0 = 0
```

### 14. `chmod` - Cambiar Permisos

```bash
# Método octal (más común)
chmod 755 script.sh
# rwxr-xr-x: dueño puede todo, otros pueden leer y ejecutar

chmod 644 documento.txt
# rw-r--r--: dueño puede leer/escribir, otros solo leer

chmod 600 private.key
# rw-------: solo dueño puede leer/escribir

chmod 777 archivo.txt
# rwxrwxrwx: TODOS pueden todo (⚠️ PELIGROSO)

# Método simbólico
chmod +x script.sh        # Agregar ejecución para todos
chmod u+x script.sh       # Agregar ejecución para user
chmod g+w archivo.txt     # Agregar escritura para group
chmod o-r archivo.txt     # Quitar lectura para others
chmod a+r archivo.txt     # Agregar lectura para all

# Recursivo
chmod -R 755 /var/www/html/

# Ver cambios
chmod -v 644 archivo.txt
```

**Permisos comunes:**
```
755 = Ejecutables, directorios públicos
644 = Archivos de texto, HTML, configuración
600 = Archivos privados, keys SSH
400 = Solo lectura (configs sensibles)
700 = Directorios privados
777 = NUNCA (demasiado permisivo)
```

### 15. `chown` - Cambiar Dueño

```bash
# Cambiar dueño
sudo chown newuser archivo.txt

# Cambiar dueño y grupo
sudo chown newuser:newgroup archivo.txt

# Solo cambiar grupo
sudo chown :newgroup archivo.txt
# O:
sudo chgrp newgroup archivo.txt

# Recursivo
sudo chown -R kali:kali /home/kali/proyectos/

# Ver cambios
sudo chown -v kali archivo.txt
```

---

## 💻 PARTE 6: PROCESOS Y SISTEMA (10 minutos)

### 16. Comandos de Procesos

```bash
# Ver todos los procesos
ps aux

# Ver procesos en árbol
ps auxf
pstree

# Buscar proceso específico
ps aux | grep apache

# Monitor en tiempo real
top
# q = salir
# k = kill proceso (pide PID)
# Shift+M = ordenar por memoria
# Shift+P = ordenar por CPU

# htop (mejor que top, instalar primero)
sudo apt install htop
htop
# F9 = kill, F10 = quit

# Matar proceso por PID
kill 1234
kill -9 1234  # Forzar

# Matar por nombre
killall firefox
pkill apache2
```

### 17. Comandos de Sistema

```bash
# Info del sistema
uname -a
hostname
uptime

# Uso de disco
df -h          # Particiones
du -sh *       # Tamaño de directorios actuales
du -sh /var/log  # Tamaño de directorio específico

# Memoria RAM
free -h

# CPU info
lscpu
cat /proc/cpuinfo

# Dispositivos PCI
lspci

# Dispositivos USB
lsusb

# Info de red
ip addr show
ip route show
```

---

## ✅ EJERCICIO PRÁCTICO: CREAR TU PRIMER SCRIPT

```bash
# 1. Crear archivo
nano primer_script.sh

# 2. Contenido:
#!/bin/bash
# Mi primer script de ciberseguridad

echo "==================================="
echo "🔍 System Information Script"
echo "==================================="
echo ""

echo "📅 Fecha y hora:"
date
echo ""

echo "👤 Usuario actual:"
whoami
echo ""

echo "💻 Hostname:"
hostname
echo ""

echo "🌐 Dirección IP:"
ip addr show | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}'
echo ""

echo "📊 Uso de memoria:"
free -h
echo ""

echo "💾 Uso de disco:"
df -h /
echo ""

echo "✅ Script completado"

# 3. Guardar: Ctrl+O, Enter, Ctrl+X

# 4. Hacer ejecutable
chmod +x primer_script.sh

# 5. Ejecutar
./primer_script.sh
```

---

## ✅ CHECKLIST DÍA 2

Puedes hacer SIN consultar:

- [x] Navegar entre directorios (cd, pwd)
- [x] Listar archivos con detalles (ls -lah)
- [x] Crear directorios y archivos (mkdir, touch)
- [x] Copiar, mover, eliminar archivos
- [x] Buscar archivos (find)
- [x] Buscar texto en archivos (grep)
- [x] Ver contenido de archivos (cat, less, head, tail)
- [x] Entender permisos rwx
- [x] Cambiar permisos (chmod)
- [x] Crear y ejecutar script básico

---
**Contenido:**

```markdown
# Día 2: Terminal Linux

## Comandos dominados

### Navegación
- pwd, ls -lah, cd

### Archivos
- cp, mv, rm, touch, mkdir

### Búsqueda
- find / -name "*.txt"
- grep -r "password"

### Mi primer script
[Pegar código del script]

## Nivel alcanzado
Antes: 2/10
Ahora: 5/10

## Próximo objetivo
- Pipes y redirecciones
- Scripting intermedio
```

```bash
git add notas/dia_02_terminal_linux.md
git commit -m "Day 2: Linux terminal basics mastered"
git push
```

---

## 🚀 SIGUIENTE: DÍA 3 - GIT Y GITHUB

Mañana aprenderás:
- Git desde cero
- Crear repositorio
- Commits, branches
- Push/pull
- Configurar SSH keys

🎉 **¡Excelente! Ya puedes navegar Linux como un pro.**</parameter>