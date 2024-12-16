import ctypes
import sys
import subprocess

def change_ip_4_address():
    def run_as_admin():
        """Solicita permisos de administrador si el script no se está ejecutando con privilegios elevados."""
        try:
            # Verifica si ya se está ejecutando como administrador
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        except:
            is_admin = False

        if not is_admin:
            # Reinicia el script con permisos elevados
            print("Solicitando permisos de administrador...")
            script = sys.executable  # Ruta al ejecutable de Python
            params = ' '.join([f'"{arg}"' for arg in sys.argv])  # Argumentos del script
            ctypes.windll.shell32.ShellExecuteW(None, "runas", script, params, None, 1)
            sys.exit()

    # Solicitar permisos al inicio
    run_as_admin()

    # Configuración de red
    interface_name = "Ethernet"  # Cambia este nombre según tu interfaz
    new_ip = "192.168.3.100"
    subnet_mask = "255.255.255.0"

    try:
        # Cambia la dirección IP y la máscara de subred
        result = subprocess.run(
            ["netsh", "interface", "ip", "set", "address", interface_name, "static", new_ip, subnet_mask],
            check=True,
            capture_output=True,
            text=True
        )
        print("Dirección IP cambiada con éxito.")
        print(f"Salida: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print("Error al cambiar la dirección IP.")
        print(f"Mensaje de error: {e.stderr}")

if __name__ == "__main__":
    change_ip_4_address()