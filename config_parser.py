import yaml

def get_config():
    with open("cfg.yaml", "r") as f:
        config = yaml.safe_load(f)
        f.close()
        return config

if __name__ == '__main__':
    with open("cfg.yaml", "r") as f:
        config = yaml.safe_load(f)
        print(config['chrome_driver_path'])
        f.close()
