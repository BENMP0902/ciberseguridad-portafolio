# recon-tool

Script de reconocimiento pasivo entregado en clase de Ciberseguridad.
Ejecuta ping, dig, whois e IP intelligence (ipinfo.io) sobre un target
y genera un reporte Markdown.

## Origen

Material del curso de Ciberseguridad (Hybridge Education). No es código
propio; se incluye en este repo como referencia y para documentar el
output que produce.

## Dependencias de sistema

`ping`, `dig`, `whois`, `curl` deben estar instalados y en el PATH.
Solo usa stdlib de Python — sin `pip install` necesario.

## Uso

```bash
python3 recon_tool.py -u <url> [-o <output.md>]
```

## Ejemplo

```bash
python3 recon_tool.py -u scanme.nmap.org -o reporte_scanme.md
```

Ver `evidencia/reporte_scanme_nmap_org.md` para muestra del output.

## Notas

- Solo realiza reconocimiento **pasivo** (ningún SYN scan, ningún port scan).
- `ipinfo.io` rate-limita; no abusar con múltiples corridas consecutivas.
- Solo extrae IPs IPv4 del output de `dig`; ignora IPv6 (AAAA records).