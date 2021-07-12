import configparser

'''
取配置文件方式一 --001
可以读取配置文件的值
可以新增配置文件的值
'''


class ConfigUtils():

    def __init__(self, config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path)

    def read_value(self, section, key):
        '''读取配置文件的值'''

        value = self.cfg.get(section, key)
        return value


if __name__ == "__main__":
    pass
