__author__ = 'IfCheung'

import os


class Config:
    SECRET_KEY = os.getenv("SECRET KEY") or 'this is site secret key'

class DefaultConfig(Config):
    MYSQL_SERVER = "localhost"
    MYSQL_PORT = "3306"
    MYSQL_USER = "root"
    MYSQL_PASSWD = "123"
    MYSQL_DATABASE = "ifcheung"
    DEBUG = True

    SQLALCHEMY_ECHO = True

    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (MYSQL_USER, MYSQL_PASSWD, \
                                                          MYSQL_SERVER, MYSQL_PORT, MYSQL_DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    MYSQL_SERVER = "localhost"
    MYSQL_PORT = "3306"
    MYSQL_USER = "root"
    MYSQL_PASSWD = "123"
    MYSQL_DATABASE = "ifcheung"
    DEBUG = True

    SQLALCHEMY_ECHO = True

    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (MYSQL_USER, MYSQL_PASSWD, \
                                                          MYSQL_SERVER, MYSQL_PORT, MYSQL_DATABASE)

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI') or \
    #     'sqlite:///%s' % os.path.join(basedir, 'data_dev_sqlite.db')
config = {
    'develop': DevelopConfig,
    'main': DefaultConfig,
}
if __name__ == '__main__':
    devconf = DevelopConfig()
    print(devconf.SQLALCHEMY_DATABASE_URI)
