config = {
    'website': 'example.com',
    'dbType': 'mysql',
    'dbUser': 'admin',
    'dbPassword': '1234',
}

print(len(config))

print(config)

print(config['dbType'])

for key in config:
    print(f"Klucz w config: {key} z wartością {config[key]}")