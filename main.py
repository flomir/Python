from ConfigurationHelper import ConfigurationHelper

def print_with_hello(name):
    print("Hello, {}!".format(name))

def main():
    config = ConfigurationHelper()
    print("Hello")
    print_with_hello(config.get_config_name())

if __name__ == "__main__": main()
