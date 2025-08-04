# Malicious-Webs-and-IPs
Informe actualizado en [04/08/2025] con dominios marcados como maliciosos en más de 2 antivirus junto con IPS también marcados como maliciosos.
Este informe fue creado con [Virustotal](https://virustotal.com) y [CloudFare](https://cloudfare.com) **API** en [Python3](https://python.org).

# Claves de API
Este código requiere 2 claves de API para funcionar:

## [CloudFlare](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/)

1. Visite: https://dash.cloudflare.com/profile/api-tokens
2. En "Claves de API" > "Global API Key" > "Ver"
3. Pedirá credenciales y luego lo tendrás que copiar al portapapeles
4. En el código, desde la raíz del proyecto, diríjase a ```./Jsons/key.json```
   Luego tendrás que poner el valor en: ```"CLDF_key": "AQUÍ"```

## [VirusTotal](https://docs.virustotal.com/docs/please-give-me-an-api-key)

1. Tendrás que acceder al menú desplegable de la [página principal](https://www.virustotal.com/) y pulsar en "API Key"
2. En el apartado de "API Key" tendrás que copiarlo la llave que aparece en el portapapeles
3. En el código, desde la raíz del proyecto, diríjase a ```./Jsons/key.json```
   Luego tendrás que poner el valor en: ```"VT_key": "AQUÍ"```


# Contacto
- **Email**: adgimenezp@gmail.com
- **Web**: [byad12.pages.dev](https://byad12.pages.dev)
- **Patreon**: [patreon.com/byAd12](https://www.patreon.com/byAd12)
