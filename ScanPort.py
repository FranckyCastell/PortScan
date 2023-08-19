import subprocess

def run_nmap_scan(ip, protocol, ports):
    if protocol == "tcp":
        command = f"nmap -p {ports} --open -sS -Pn -n --min-rate 5000 {ip}"
    elif protocol == "udp":
        command = f"nmap -p {ports} --open -sU -Pn -n --min-rate 5000 {ip}"
    else:
        print("Protocolo no válido. Debe ser 'tcp' o 'udp'.")
        return
    
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        if result.returncode == 0:
            print("")
            print("RESULTADO DEL ESCANEO:")
            print(result.stdout)
        else:
            print("Upss... OCURRIÓ UN ERROR DURANTE EL ESCANEO")
            print(result.stderr)
    except Exception as e:
        print("UPSS... OCURRIÓ UN ERROR:", e)

def main():
    print("")
    ip = input("Introduce la dirección IP a escanear: ")
    print("")
    protocol = input("SELECCIONA EL PROTOCOLO DE ESCANEO ( tcp / udp ): ").lower()
    print("")
    ports_input = input("ESPECIFICA LOS PUERTOS QUE DESEAS ESCANEAR (EJ. '80,443' O 'all' PARA TODOS): ")
    
    if protocol not in ["tcp", "udp"]:
        print("PROTOCOLO NO VÁLIDO. DEBE SER 'tcp' o 'udp'")
        return
    
    if ports_input.lower() == "all":
        ports = "1-65535"
    else:
        ports = ports_input
    
    run_nmap_scan(ip, protocol, ports)

if __name__ == "__main__":
    main()
