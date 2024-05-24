import os
import socket
import debugpy
from app import create_app


def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("0.0.0.0", port)) == 0


# Démarrer debugpy et écouter les connexions de débogage
if os.getenv('ENV_CONFIG') == 'development':
    debug_port = 5678
    if not is_port_in_use(debug_port):
        debugpy.listen(("0.0.0.0", debug_port))
        print("Waiting for debugger attach...")
        debugpy.wait_for_client()
    else:
        print(
            f"Port {debug_port} is already in use. Skipping debugpy initialization.")

config_name = os.getenv('ENV_CONFIG') or 'development'
app = create_app(config_name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
