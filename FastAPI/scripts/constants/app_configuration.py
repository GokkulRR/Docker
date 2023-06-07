from configparser import ConfigParser
import os
conf_path = os.getcwd() + '\\configuration\\application.conf'
config = ConfigParser()
config.read(conf_path)

host = config.get('PortDetails', 'host', fallback='127.0.0.1')
port = config.get('PortDetails', 'port', fallback='8000')
