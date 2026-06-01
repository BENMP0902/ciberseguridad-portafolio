# Reporte de reconocimiento

## Objetivo

- URL original: `scanme.nmap.org`
- Dominio analizado: `scanme.nmap.org`
- Fecha de ejecucion: `2026-05-31 23:38:20`


## Ping

### Comando ejecutado

```bash
ping -c 1 scanme.nmap.org
```

### Estado

- Exito: `True`
- Codigo de salida: `0`

### Salida

```text
PING scanme.nmap.org (45.33.32.156) 56(84) bytes of data.
64 bytes from scanme.nmap.org (45.33.32.156): icmp_seq=1 ttl=46 time=131 ms

--- scanme.nmap.org ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 131.451/131.451/131.451/0.000 ms
```


## DNS - dig +short

### Comando ejecutado

```bash
dig +short scanme.nmap.org
```

### Estado

- Exito: `True`
- Codigo de salida: `0`

### Salida

```text
45.33.32.156
```


## WHOIS

### Comando ejecutado

```bash
whois scanme.nmap.org
```

### Estado

- Exito: `True`
- Codigo de salida: `0`

### Salida

```text
Malformed request.
>>> Last update of WHOIS database: 2026-06-01T05:38:18Z <<<

Terms of Use: Access to Public Interest Registry WHOIS information is provided to assist persons in determining the contents of a domain name registration record in the Public Interest Registry registry database. The data in this record is provided by Public Interest Registry for informational purposes only, and Public Interest Registry does not guarantee its accuracy. This service is intended only for query-based access. You agree that you will use this data only for lawful purposes and that, under no circumstances will you use this data to (a) allow, enable, or otherwise support the transmission by e-mail, telephone, or facsimile of mass unsolicited, commercial advertising or solicitations to entities other than the data recipient's own existing customers; or (b) enable high volume, automated, electronic processes that send queries or data to the systems of Registry Operator, a Registrar, or Identity Digital except as reasonably necessary to register domain names or modify existing registrations. All rights reserved. Public Interest Registry reserves the right to modify these terms at any time. By submitting this query, you agree to abide by this policy.  The Registrar of Record identified in this output may have an RDDS service that can be queried for additional information on how to contact the Registrant, Admin, or Tech contact of the queried domain name.
```


## WHOIS - 45.33.32.156

### Comando ejecutado

```bash
whois 45.33.32.156
```

### Estado

- Exito: `True`
- Codigo de salida: `0`

### Salida

```text
#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/resources/registry/whois/tou/
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
#
# Copyright 1997-2026, American Registry for Internet Numbers, Ltd.
#



# start

NetRange:       45.33.0.0 - 45.33.127.255
CIDR:           45.33.0.0/17
NetName:        LINODE-US
NetHandle:      NET-45-33-0-0-1
Parent:         NET45 (NET-45-0-0-0-0)
NetType:        Direct Allocation
OriginAS:       
Organization:   Akamai Technologies, Inc. (AKAMAI)
RegDate:        2015-03-20
Updated:        2023-09-18
Comment:        Geofeed https://ipgeo.akamai.com/linode-geofeed.csv
Ref:            https://rdap.arin.net/registry/ip/45.33.0.0



OrgName:        Akamai Technologies, Inc.
OrgId:          AKAMAI
Address:        145 Broadway
City:           Cambridge
StateProv:      MA
PostalCode:     02142
Country:        US
RegDate:        1999-01-21
Updated:        2023-10-24
Ref:            https://rdap.arin.net/registry/entity/AKAMAI


OrgTechHandle: IPADM11-ARIN
OrgTechName:   ipadmin
OrgTechPhone:  +1-617-444-0017 
OrgTechEmail:  ip-admin@akamai.com
OrgTechRef:    https://rdap.arin.net/registry/entity/IPADM11-ARIN

OrgAbuseHandle: NUS-ARIN
OrgAbuseName:   NOC United States
OrgAbusePhone:  +1-617-444-2535 
OrgAbuseEmail:  abuse@akamai.com
OrgAbuseRef:    https://rdap.arin.net/registry/entity/NUS-ARIN

OrgTechHandle: SJS98-ARIN
OrgTechName:   Schecter, Steven Jay
OrgTechPhone:  +1-617-274-7134 
OrgTechEmail:  ip-admin@akamai.com
OrgTechRef:    https://rdap.arin.net/registry/entity/SJS98-ARIN

RTechHandle: LNO21-ARIN
RTechName:   Linode Network Operations
RTechPhone:  +1-609-380-7100 
RTechEmail:  support@linode.com
RTechRef:    https://rdap.arin.net/registry/entity/LNO21-ARIN

RNOCHandle: LNO21-ARIN
RNOCName:   Linode Network Operations
RNOCPhone:  +1-609-380-7100 
RNOCEmail:  support@linode.com
RNOCRef:    https://rdap.arin.net/registry/entity/LNO21-ARIN

RAbuseHandle: LAS12-ARIN
RAbuseName:   Linode Abuse Support
RAbusePhone:  +1-609-380-7100 
RAbuseEmail:  abuse@linode.com
RAbuseRef:    https://rdap.arin.net/registry/entity/LAS12-ARIN

# end


# start

NetRange:       45.33.0.0 - 45.33.127.255
CIDR:           45.33.0.0/17
NetName:        LINODE
NetHandle:      NET-45-33-0-0-2
Parent:         LINODE-US (NET-45-33-0-0-1)
NetType:        Reassigned
OriginAS:       
Organization:   Linode (LINOD)
RegDate:        2022-12-21
Updated:        2023-09-18
Comment:        Geofeed https://ipgeo.akamai.com/linode-geofeed.csv
Ref:            https://rdap.arin.net/registry/ip/45.33.0.0



OrgName:        Linode
OrgId:          LINOD
Address:        249 Arch St
City:           Philadelphia
StateProv:      PA
PostalCode:     19106
Country:        US
RegDate:        2008-04-24
Updated:        2022-12-15
Comment:        http://www.linode.com
Ref:            https://rdap.arin.net/registry/entity/LINOD


OrgNOCHandle: LNO21-ARIN
OrgNOCName:   Linode Network Operations
OrgNOCPhone:  +1-609-380-7100 
OrgNOCEmail:  support@linode.com
OrgNOCRef:    https://rdap.arin.net/registry/entity/LNO21-ARIN

OrgTechHandle: LNO21-ARIN
OrgTechName:   Linode Network Operations
OrgTechPhone:  +1-609-380-7100 
OrgTechEmail:  support@linode.com
OrgTechRef:    https://rdap.arin.net/registry/entity/LNO21-ARIN

OrgAbuseHandle: LAS12-ARIN
OrgAbuseName:   Linode Abuse Support
OrgAbusePhone:  +1-609-380-7100 
OrgAbuseEmail:  abuse@linode.com
OrgAbuseRef:    https://rdap.arin.net/registry/entity/LAS12-ARIN

OrgTechHandle: IPADM11-ARIN
OrgTechName:   ipadmin
OrgTechPhone:  +1-617-444-0017 
OrgTechEmail:  ip-admin@akamai.com
OrgTechRef:    https://rdap.arin.net/registry/entity/IPADM11-ARIN

# end



#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/resources/registry/whois/tou/
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
#
# Copyright 1997-2026, American Registry for Internet Numbers, Ltd.
#
```


## IP Info para `45.33.32.156`

### Comando ejecutado

```bash
curl -s https://ipinfo.io/45.33.32.156
```

### Estado

- Éxito: `True`
- Código de salida: `0`

### Salida

```json
{
  "ip": "45.33.32.156",
  "hostname": "scanme.nmap.org",
  "city": "Fremont",
  "region": "California",
  "country": "US",
  "loc": "37.5483,-121.9886",
  "org": "AS63949 Akamai Connected Cloud",
  "postal": "94536",
  "timezone": "America/Los_Angeles",
  "readme": "https://ipinfo.io/missingauth"
}
```

