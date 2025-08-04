# Malicious-Webs-and-IPs
Informe actualizado en [04/08/2025] con dominios marcados como maliciosos en más de 2 antivirus junto con IPS también marcados como maliciosos: [aquí](https://github.com/byAd12/Malicious-Webs-and-IPs/blob/main/Ejemplo.json).

# ¿Qué es?
Programa en Python3 que usa la API de Cloudflare y VirusTotal para generar un reporte completo sobre una IP (sólo IPv4) o de una página web mediante su DNS. Enseña datos como reportes de confiabilidad de varios antivirus, recursos enlazados, información sobre el nombre de dominio y otras funcionalidades.

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

# Capturas de pantalla
<img width="1746" height="976" alt="Captura de pantalla 2025-08-04 210537" src="https://github.com/user-attachments/assets/f4426b9e-9a46-460d-b564-0c74a516d833" />
<img width="1746" height="976" alt="Captura de pantalla 2025-08-04 210631" src="https://github.com/user-attachments/assets/7f713811-adde-4d03-8f64-747bf7d52f2c" />
<img width="1746" height="976" alt="Captura de pantalla 2025-08-04 210647" src="https://github.com/user-attachments/assets/4991ec3a-8b0a-44f5-a7a7-252f65991541" />
<img width="1746" height="976" alt="Captura de pantalla 2025-08-04 210705" src="https://github.com/user-attachments/assets/0f50499b-699e-4140-9f1a-4a14c3c397d6" />


# Contacto
- **Email**: adgimenezp@gmail.com
- **Web**: [byad12.pages.dev](https://byad12.pages.dev)
- **Patreon**: [patreon.com/byAd12](https://www.patreon.com/byAd12)
