import os
from app import create_app

config_name = os.getenv('ENV_CONFIG') or 'development'
app = create_app(config_name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
