import logging

from slave import Slave

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def main():
    slave = Slave()
    slave.start()


if __name__ == '__main__':
    main()
