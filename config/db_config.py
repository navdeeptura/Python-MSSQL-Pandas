import configparser

def get_db_settings(config_path):
    db_config = configparser.ConfigParser()
    db_config.read(config_path)
    return {
        "server": db_config["database"]["server"],
        "database": db_config["database"]["database"],
        "user": db_config["database"]["user"],
        "password": db_config["database"]["password"]
    }
