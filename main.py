import requests, socket, json, os, datetime, whois, shutil, sys, time
from prettytable import PrettyTable
from art import *
from datetime import datetime
from bs4 import BeautifulSoup
from Recs.Func import get_rango_registrar, WiFi, VPN, BORRAR_DATOS
from colorama import init, Fore; init()

FB, FW, FR = Fore.BLUE, Fore.WHITE, Fore.RED

#-----------------------------------------------------------------------------------------------------------------------------------------#
#- Mirar si tiene una red y VPN conectada -#
WiFi(), VPN()
#-----------------------------------------------------------------------------------------------------------------------------------------#
#- MODO -#
modo = ""
while True:
    modo = input(f"\n{FB}¿Qué quieres hacer?\n\n\t1:{FW} ESCANEAR UN DOMINIO\n\t{FB}2:{FW} BORRAR REGISTROS\n\t{FB}3:{FW} CRÉDITOS :)\n\t{FB}4:{FW} CERRAR EL PROGRAMA\n\n{FB}Respuesta:{FW} ")
    if modo == "" or modo == None:
        print("\033[H\033[J")
    else:
        break

if int(modo) == 2:
    print("\033[H\033[J")
    BORRAR_DATOS()
elif int(modo) == 3:
    print("\033[H\033[J")
    print(f"{FB}byAd12\nadgimenezp@gmail.com\nhttps://byad12.pages.dev{FW}\n\nCerrando el programa en 25 segundos.")
    try: time.sleep(25)
    except: pass
    sys.exit()
elif int(modo) == 4:
    sys.exit()
else:
    print("\033[H\033[J")

#-----------------------------------------------------------------------------------------------------------------------------------------#
#- API Key -#
with open("Jsons/key.json", mode="r") as file:
    f = json.load(file)
    api_key = f["VT_key"]
    CLDF_key = f["CLDF_key"]
#-----------------------------------------------------------------------------------------------------------------------------------------#
Domain = input(str(f"\033[95mDominio:{FW} ")).lower()
if "http://" in Domain or "https://" in Domain:
    try:
        Domain = Domain.replace("http://", "")
    except:
        Domain = Domain.replace("https://", "")
if "www." in Domain:
    try:
        Domain = Domain.replace("www.", "")
    except:
        pass
domain_info = whois.whois(Domain)
try:
    IPv4 = socket.gethostbyname(Domain)
except:
    print(f"{FB}Dominio no encontrado{FW}")
    try: time.sleep(5)
    except: pass
    sys.exit()
try:
    os.mkdir(f"Logs/{Domain}/")
except:
    pass #- Existe -#
#- ADVERTIR -#
with open(f"Jsons/Reporte.json", "r") as file:
    json_cnt = json.loads(file.read())
    print(Domain, IPv4)
    if str(Domain) in str(json_cnt):
        print("\n\033[91mEL DOMINIO ESTÁ GUARDADO COMO MALICIOSO. ¿QUIERES CONTINUAR? (s/n){FW}")
        if input("\033[91mRespuesta: {FW}") == "s":
            pass
        else:
            sys.exit()
    if str(IPv4) in str(json_cnt):
        print("\n\033[91mLA IPv4 ESTÁ GUARDADA COMO MALICIOSA. ¿QUIERES CONTINUAR? (s/n){FW}")
        if input("\033[91mRespuesta: {FW}") == "s":
            pass
        else:
            sys.exit()
print("\033[H\033[J\n\033[95mDominio: {}{}".format(FW, Domain))
#-----------------------------------------------------------------------------------------------------------------------------------------#
try:
    Contenido, protocolo = requests.get(f"https://www.{Domain}").text, "HTTPS" #- Protocolo HTTPS -#
except:
    Contenido, protocolo = requests.get(f"http://www.{Domain}").text, "HTTP"  #- Protocolo HTTP -#
#- Todas las URLs -#
soup = BeautifulSoup(Contenido, "html.parser")
urls, fin_urls = [], []
for link in soup.find_all('a', href=True):
    urls.append(link["href"])
img_tags = soup.find_all("img")
for img in img_tags:
    if 'src' in img.attrs:
        urls.append(img["src"])
#- Filtros -#
a1 = [d.replace("https://www.", "") for d in urls] #- Acortar URLs -#
a2 = [d.replace("http://www.", "") for d in a1]
a3 = [d.replace("https://", "") for d in a2]
for i in [d.replace("http://", "") for d in a3]: #- Eliminar registros vacios -#
    if i == "/":
        fin_urls.append(i)
#- Ordenar -#
t5, t6, t7, t8 = PrettyTable(["Imágenes", "Valuees"]), PrettyTable(["Documentos", "Valuees"]), PrettyTable(["Programación", "Valuees"]), PrettyTable(["Otros", "Valuees"])
añadidos, a21, a22, a23, a24 = [], 0, 0, 0, 0
var1, var2, var3 = [".png", ".ico", ".jpg", ".jpeg", ".svg"], [".pdf", ".docx", ".txt"], [".html", ".htm", ".js", ".css", ".py"]
for i in a3:
    for i2 in var1:
        if i2 in i:
            if i not in añadidos:
                añadidos.append(i)
                t5.add_row([" ", f"{FB}{i}{FW}"])
                a21 += 1
for i in a3:
    for i2 in var2:
        if i2 in i:
            if i not in añadidos:
                añadidos.append(i)
                t6.add_row([" ", f"{FB}{i}{FW}"])
                a22 += 1
for i in a3:
    for i2 in var3:
        if i2 in i:
            if i not in añadidos:
                añadidos.append(i)
                t7.add_row([" ", f"{FB}{i}{FW}"])
                a23 += 1
for i in a3:
    if i not in añadidos:
        if str(i) == "/" or str(i) == "javascript:;" or str(i) == "#":
            pass
        else:
            t8.add_row([" ", f"{FB}{str(i)}{FW}"])
            a24 += 1
#- Mirando por tablas vacías para añadir una celda -#
tables, variables = [t5, t6, t7, t8], [a21, a22, a23, a24]
for table, variable in zip(tables, variables):
    if variable == 0:
        table.add_row([" ", " "])
#-----------------------------------------------------------------------------------------------------------------------------------------#
file1 = open(f"Logs/{Domain}/IP_Report.txt", "w")
file1.write(requests.get(f"https://www.virustotal.com/api/v3/ip_addresses/{IPv4}", headers={"accept": "application/json", "x-apikey": api_key}).text)
file1.close()
#- IP_Report y Variable de su contenido -#
with open(f"Logs/{Domain}/IP_Report.txt", "r") as file:
    datos_json = json.loads(file.read())
    #- Mirar si la API key es incorrecta -#
    if str("Wrong API key") in str(datos_json):
        print(f"Error de VirusTotal: {FR}Wrong API key{FW}")
        sys.exit()
#-----------------------------------------------------------------------------------------------------------------------------------------#
file2 = open(f"Logs/{Domain}/Domain_Report.txt", "w")
file2.write(requests.get(f"https://www.virustotal.com/api/v3/domains/{Domain}", headers={"accept": "application/json", "x-apikey": api_key}).text)
file2.close()
#- Domain_Report y Variable de su contenido -#
with open(f"Logs/{Domain}/Domain_Report.txt", "r") as file:
    datos_json2 = json.loads(file.read())
#-----------------------------------------------------------------------------------------------------------------------------------------#
#- "Whois" del IP_Report -#
file3 = open(f"Logs/{Domain}/Whois.txt", "w")
file3.write(datos_json["data"]["attributes"]["whois"])
file3.close()
#-----------------------------------------------------------------------------------------------------------------------------------------#
file4 = open(f"Logs/{Domain}/Report-CLDF.txt", "w")
file4.write("{}".format(requests.request("GET", "https://api.cloudflare.com/client/v4/radar/entities/ip", headers={"Content-Type": "application/json", "X-Auth-Email": "adgimenezp@gmail.com", "X-Auth-Key": CLDF_key}, params={"format": "json", "ip": IPv4}).text))
file4.close()
#- Domain_Report-CLDF y Variable de su contenido -#
with open(f"Logs/{Domain}/Report-CLDF.txt", "r") as file:
    datos_json3 = json.loads(file.read())
#-------------------------------- VARIABLES ----------------------------------------------------------------------------------------------#
#- Seguridad > último análisis -#
try:
    fecha_timestamp = int(datos_json2["data"]["attributes"]["last_analysis_date"])
    fecha_formateada = datetime.utcfromtimestamp(fecha_timestamp).strftime("%d-%m-%Y")
except:
    fecha_formateada = "-"
#- Seguridad > último DNS -#
try:
    fecha_timestamp2 = int(datos_json2["data"]["attributes"]["last_dns_records_date"])
    fecha_formateada2 = datetime.utcfromtimestamp(fecha_timestamp2).strftime("%d-%m-%Y")
except:
    fecha_formateada2 = "-"
#- Seguridad > último certificado HTTPS -#
try:
    fecha_timestamp3 = int(datos_json2["data"]["attributes"]["last_https_certificate_date"])
    fecha_formateada3 = datetime.utcfromtimestamp(fecha_timestamp3).strftime("%d-%m-%Y")
except:
    fecha_formateada3 = "-"
#- Reportes de IP y Dominio -#
l, l2, l3, l4 = [], [], [], [] #- Reportes -#
lcount = 0
try:
    for engine, analysis_result in datos_json2["data"]["attributes"]["last_analysis_results"].items(): # Reportes Dominio Maliciosos
        if analysis_result["category"] == "malicious":
            l.append(analysis_result["engine_name"])
            lcount += 1
    for engine, analysis_result in datos_json2["data"]["attributes"]["last_analysis_results"].items(): # R. Dominio Sospechosos
        if analysis_result["category"] == "suspicious":
            l2.append(analysis_result["engine_name"])
    for engine, analysis_result in datos_json["data"]["attributes"]["last_analysis_results"].items(): # Reportes IP Maliciosos
        if analysis_result["category"] == "malicious":
            l3.append(analysis_result["engine_name"])
    for engine, analysis_result in datos_json["data"]["attributes"]["last_analysis_results"].items(): # R. IP Sospechosos
        if analysis_result["category"] == "suspicious":
            l4.append(analysis_result["engine_name"])
except:
    print("{FB}Dominio no encontrado.{FW}")
    try: time.sleep(5)
    except: pass
    sys.exit()
#------------------------------ TABLAS ---------------------------------------------------------------------------------------------------#
#- Tabla principal -#
t = PrettyTable([" ", "Valor", "Información"])
t.add_row(["Dominio", Domain, "Propietario: {}{}{}\nRegistrador: {}{}{}\nCertificado: {}{}{}".format(FB, datos_json["data"]["attributes"]["as_owner"],FW, FB, str(domain_info.registrar).replace("None", f"\033[91m-{FW}"),FW, FB, protocolo,FW)])
try:
    t.add_row(["Creación", "{}{}{}".format(FB, str(domain_info.creation_date[1]), FW), " "])
except:
    t.add_row(["Creación", f"{FB}-{FW}", " "])
try:
    t.add_row(["Expiración", "No antes de:\nNo después de:", "{}{}{} \n{}{}{}".format(FB,datos_json2["data"]["attributes"]["last_https_certificate"]["validity"]["not_after"],FW,FB, datos_json2["data"]["attributes"]["last_https_certificate"]["validity"]["not_before"],FW)])
except:
    t.add_row(["Expiración", "No antes de:\nNo después de:", f"{FB}-{FW} \n{FB}-{FW}"])
#- Tabla 2 -#
t11 = PrettyTable([" ", "Valor", "Información"])
t11.add_row(["dnssec", "{}{}{}".format(FB,str(domain_info.dnssec).replace("None", "-"), FW), " "])
t11.add_row(["Servidor WHOIS", "{}{}{}".format(FB,str(domain_info.whois_server).replace("None", "-"), FW), " "])
t11.add_row(["Emails", "{}{}{}".format(FB,str(domain_info.emails).replace("None", "-"), FW), " "])
t11.add_row(["Org", "{}{}{}".format(FB,str(domain_info.org).replace("None", "-"), FW), " "])
t11.add_row(["Dirección", "{}{}, {}, {}{}".format(FB,str(domain_info.city).replace("None", "-"), str(domain_info.state).replace("None", "-"), str(domain_info.country).replace("None", "-"), FW), "{}{}{}".format(FB, str(domain_info.registrant_postal_code).replace("None", ""),FW)])
#- Network -#
t1 = PrettyTable([" ", "Valor", "Información"])
try:
    range_registrar = get_rango_registrar(datos_json["data"]["attributes"]["whois"])
    range_registrar = range_registrar.replace(" - ", f"{FW} a \n {FB}")
    t1.add_row(["IPv4", "{}{}{}".format(FB,datos_json["data"]["id"],FW), f"Rango: {FB}{range_registrar}{FW} \nRegistrador: {FB}{datos_json['data']['attributes']['regional_internet_registry']}{FW}\nRed: {FB}{datos_json['data']['attributes']['network']}{FW}"])
except:
    t1.add_row(["IPv4", "{}{}{}".format(FB,datos_json["data"]["id"],FW), f"Rango: {FB}{get_rango_registrar(datos_json['data']['attributes']['whois'])}{FW} \nRegistrador: {FB}NO ENCONTRADO{FW}\nRed: {FB}{datos_json['data']['attributes']['network']}{FW}"])
t1.add_row(["ASN", "{}{}{}".format(FB,datos_json3["result"]["ip"]["asn"],FW), "Nombre: {}{}{} \nOrg: {}{}{} \nUbicación: {}{}{}".format(FB,datos_json3["result"]["ip"]["asnName"],FW, FB,datos_json3["result"]["ip"]["asnOrgName"],FW, FB, datos_json3["result"]["ip"]["asnLocation"],FW)])
#- Tabla de Reportes -#
t2 = PrettyTable([" ", "Valor"])
t2.add_row(["IP", "{}{}{}".format(FB,datos_json["data"]["attributes"]["last_analysis_stats"],FW)])
t2.add_row(["Reportes Maliciosos", "\033[91m{}{}".format(", ".join(l3),FW)])
t2.add_row(["Reportes Sospechosos", "\033[93m{}{}".format(", ".join(l4),FW)])
t2.add_row(["Dominio", "{}{}{}".format(FB,datos_json2["data"]["attributes"]["last_analysis_stats"],FW)])
t2.add_row(["Reportes Maliciosos", "\033[91m{}{}".format(", ".join(l),FW)])
t2.add_row(["Reportes Sospechosos", "\033[93m{}{}".format(", ".join(l2),FW)])
#- Tabla de Seguridad -#
t2b = PrettyTable([" ", "Valor", "Información"])
t2b.add_row(["Votos del Dominio", "Maliciosos: {}{}{} \nBueno: {}{}{}".format(FB,datos_json2["data"]["attributes"]["total_votes"]["malicious"],FW,FB, datos_json2["data"]["attributes"]["total_votes"]["harmless"],FW), "Total: {}{}{} \nReputación: {}{}{}".format(FB,int(datos_json2["data"]["attributes"]["total_votes"]["harmless"]) + int(datos_json2["data"]["attributes"]["total_votes"]["malicious"]),FW,FB, datos_json2["data"]["attributes"]["reputation"],FW)])
t2b.add_row(["Último análisis", f"{FB}{fecha_formateada}{FW}", f"{FB}(VirusTotal){FW}"])
t2b.add_row(["Última consulta DNS", f"{FB}{fecha_formateada2}{FW}", " "])
t2b.add_row(["Último certificado HTTPS", f"{FB}{fecha_formateada3}{FW}", ""])
try:
    t2b.add_row(["Certificado HTTPS", "Algoritmo: {}{}{}\nValidación: {}{}{}".format(FB,datos_json2["data"]["attributes"]["last_https_certificate"]["public_key"]["algorithm"],FW,FB, datos_json2["data"]["attributes"]["last_https_certificate"]["validity"]["not_after"],FW), ""])
except:
    try:
        t2b.add_row(["Certificado HTTPS", "Algoritmo: {}{}{} \nValidación: {}-{}".format(FB,datos_json2["data"]["attributes"]["last_https_certificate"]["public_key"]["algorithm"]), ""],FW)
    except:
        t2b.add_row(["Certificado HTTPS", f"Algoritmo: {FB}-{FW} \nValidación: {FB}-{FW}", ""])
#- Tabla de DNS comunes -#
t3 = PrettyTable(["Tipo", "Valor", "TTL", "Prioridad"])
for i in datos_json2["data"]["attributes"]["last_dns_records"]:
    t3.add_row([i.get("type", ""), i.get("value", ""), i.get("ttl", ""), i.get("priority", "")])
#- 2nd Tabla de DNS no comunes -#
rname_record = next((record for record in datos_json2['data']['attributes']['last_dns_records'] if record.get('type') == 'SOA'), None)
t4 = PrettyTable(["Rname", "Reintento", "Refresco", "Mínimo", "Valor", "Expiración", "TTL", "Serial", "Tipo"])
if rname_record:
    t4.add_row([rname_record.get("rname", ""), rname_record.get("retry", ""), rname_record.get("refresh", ""), rname_record.get("minimum", ""), rname_record.get("value", ""),rname_record.get("expire", ""), rname_record.get("ttl", ""), rname_record.get("serial", ""), rname_record.get("type", "")])
#-----------------------------------------------------------------------------------------------------------------------------------------#
#- Guardar IPs y Dominios maliciosos -#
with open("Jsons/Reporte.json", "r") as f:
    data_json3 = json.load(f)
l5, l6, d = data_json3["Domains"], data_json3["IPs"], False #- Variables -#
if l:
    if Domain not in data_json3["Domains"]:
        l5.append(Domain)
    #add_db(Domain, IPv4)
if l3:
    if IPv4 not in data_json3["IPs"]:
        l6.append(IPv4)
    #add_db2("<IP_Only>", IPv4)
data_json3["Domains"] = l5 #- Guardar datos -#
data_json3["IPs"] = l6

with open("Jsons/Reporte.json", "w") as f:
    json.dump(data_json3, f, indent=4)
#-----------------------------------------------------------------------------------------------------------------------------------------#
mensajes_final, Separador = [f"Escaneado a las {FB}{datetime.now()}{FW} (UTC +1)", "\n\nINTERNAMENTE", t, t11, "\nRED", t1, "\n\nREPORTES", t2, "\nSEGURIDAD (DEL DOMINIO)", t2b, "\n\nDNS", t3, t4, "\n\nCONTENIDO RELACIONADO", t5, t6, t7, t8, "\n\n\nElige una opción:"], "-"*38
for i in mensajes_final:
    print(i)
#-
filw, filw2 = 0, 0
if str(input(f"-----\n\033[92m¿Quieres exportar los resultados en /Descargas? (s/n){FW}\nRespuesta: ")).lower() in ["yes", "y", "ye", "si", "s"]:
    exportado, menssaje_a_exportar = "", [f"LEER ANTES: Todos los datos son públicos así que no hay infracciones. Los datos fueron obtenidos por la API de VirusTotal y solicitudes al dominio y a su IP correspondiente.\nPreguntas: adgimenezp@gmail.com.\nRecomendado: Hacer zoom al 60% para ver <<CONTENIDO RELACIONADO>>.\n\nESCANEADO A LAS: {datetime.now()} (UTC +1)\n{Separador}\n\n\n\nINTERNAMENTE\n{t}\n{t11}\n\nRED\n{t1}\n\n\nREPORTES\n{t2}\n\nSEGURIDAD (DEL DOMINIO)\n{t2b}\n\n\nDNS\n{t3}\n{t4}\n\n\nPÁGINAS RELACIONADAS\n{t5}\n{t6}\n{t7}\n{t8}\n\n\n"]
    for i in menssaje_a_exportar:
        exportado += str(i)
    file4 = open("{}/Reporte-{}.txt".format(os.path.join(os.path.expanduser("~"), "Downloads"), Domain), "w")
    ex = str(exportado).replace("[90m", "")
    ex = str(ex).replace("[91m", "")
    ex = str(ex).replace("[92m", "")
    ex = str(ex).replace("[93m", "")
    ex = str(ex).replace("[94m", "")
    ex = str(ex).replace("[0m", "")
    file4.write(ex)
    file4.close()

if str(input(f"-----\n\033[92m¿Quieres eliminar los registros para liberar un poco de espacio? (s/n){FW}\nRespuesta: ").format()).lower() in ["yes", "y", "ye", "si", "s"]:
    for i in ["URLs.txt", "Whois.txt", "IP_Report.txt", "Domain_Report.txt", "Report-CLDF.txt"]:
        try:
            os.remove(f"Logs/{Domain}/{i}")
            filw += 1
        except:
            pass
    try:
        shutil.rmtree(f"Logs/{Domain}/")
        filw2 += 1
    except:
        pass
    print(f"{FB}Se borraron {filw}/4 archivos y {filw2}/1 carpeta{FW}")
if input(f"-----\n\033[92m¿Quieres seguir ejecutando el programa? (s/n) (CRTL+C para pararlo){FW}\nRespuesta: ").lower() in ["yes", "y", "ye", "si", "s"]:
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
#-----------------------------------------------------------------------------------------------------------------------------------------#