import configparser

config = configparser.ConfigParser()
config.read("config.property")

#config['TEST2'] = {}
#onfig['TEST2']['key'] = 'value'


print(config.sections())
print(config.options('CI'))

print(config['DEFAULT']['SECRET_KEY'])
#print(config['TEST']['TEST_TIMEOUT'])
print(config['CI']['HOOK_URL'])


"""
with open('config.property', 'wb') as file:
    file.seek(2, 0)
    config.write(file)
"""