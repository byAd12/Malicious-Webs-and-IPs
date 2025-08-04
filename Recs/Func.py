import re, subprocess, time, psutil, os, sys, shutil
#----------------------------------------------------------------------------------------------------------------------------#
def get_rango_registrar(whois_data):
    match = re.search(r"(NetRange|inetnum):\s*([\d\.]+\s*-\s*[\d\.]+)", whois_data)
    if match:
        return match.group(2)
    else:
        return "NO ENCONTRADO"
#----------------------------------------------------------------------------------------------------------------------------#
def detectar_WiFi():
    conexiones = {"WiFi": False, "Cableada": False}
    ### WiFi
    try:
        resultado = subprocess.check_output(["netsh", "wlan", "show", "interfaces"], stderr=subprocess.STDOUT, text=True, encoding='cp850')
        if "SSID" in resultado:
            conexiones["WiFi"] = True
    except subprocess.CalledProcessError:
        conexiones["WiFi"] = False
    ### Cableada
    try:
        interfaces, estados = psutil.net_if_addrs(), psutil.net_if_stats()        
        for interfaz, addrs in interfaces.items():
            if interfaz in estados:
                if estados[interfaz].isup and "Ethernet" in interfaz:
                    conexiones["Cableada"] = True
                    break
    except Exception as e:
        pass
    if conexiones["WiFi"] == True or conexiones["Cableada"] == True:
        return True
    else:
        return False

def WiFi():
    if detectar_WiFi() == False:
        print("\n\n\033[93mSin acceso a Internet, porfavor conéctate a una red. Intentado de nuevo en 15s.\033[0m")
        try: time.sleep(15)
        except: pass
        if detectar_WiFi() == True:
            print("\n\n\033[92mAcceso a Internet detectado.\033[0m")
        else:
            print("\n\n\033[91mSin acceso a Internet, porfavor conéctate a una red y ejecuta de nuevo el programa.\033[0m")
            try: time.sleep(5)
            except: pass
            sys.exit()
    else:
        print("\n\n\033[92mAcceso a Internet detectado.\033[0m")
#----------------------------------------------------------------------------------------------------------------------------#
def detectar_vpn():
    interfaces_de_red = psutil.net_if_stats()
    for interfaz, stats in interfaces_de_red.items():
        if stats.isup and "vpn" in interfaz.lower():
            return True
    return False

def VPN():
    if detectar_vpn() == False and input("VPN no detectada. ¿Quieres continuar? (y/n): ") == "y":
        print("\033[92mVPN omitida.\033[0m")
    elif detectar_vpn() == False:
        print("\n\n\033[91mSe recomienda una VPN para ejecutar este programa. Porfavor habilita una y ejecuta el programa de nuevo.\033[0m\n")
        try: time.sleep(5)
        except: pass
        sys.exit()
    else:
        print("\033[92mVPN detectada.\033[0m")
#----------------------------------------------------------------------------------------------------------------------------#
def BORRAR_DATOS():
    def eliminar_carpeta(ruta):
        try:
            shutil.rmtree(ruta)
            print(f"\033[91mBorrado:\033[0m {ruta}")
        except Exception as e:
            print(f"\033[91mError eliminando:\033[0m {ruta}")
    
    def bytes_a_megabytes(bytes_valor):
        return bytes_valor / (1024 * 1024)
    
    total_carpetas, peso_total = 0, 0
    for dirpath, dirnames, filenames in os.walk("Logs/"):
        total_carpetas += len(dirnames)
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            peso_total += os.path.getsize(file_path)
    print("\033[94mRUTA ABSOLUTA:\033[0m       {}".format(os.path.abspath("Logs/")))
    print(f"\033[94mDirectorios Totales:\033[0m {total_carpetas}")
    print(f"\033[94mTotal:\033[0m               {round(bytes_a_megabytes(peso_total), 3)} MegaBytes\n")
    if input("\033[94mQuieres borrar los datos?\033[0m (y/n): ") == "y":
        for dirpath, dirnames, filenames in os.walk("Logs/", topdown=False):
            for dirname in dirnames:
                carpeta_a_eliminar = os.path.join(dirpath, dirname)
                eliminar_carpeta(carpeta_a_eliminar)
        if total_carpetas == 0:
            print("\033[91m0 Carpetas borradas. \033[0m")
            try: time.sleep(5)
            except: pass
            sys.exit()
    try: time.sleep(10)
    except: pass
    sys.exit()
#----------------------------------------------------------------------------------------------------------------------------#