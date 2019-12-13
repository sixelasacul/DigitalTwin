import logging

from master import Master

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def main():
    master = Master()
    master.start_reading_loop()


if __name__ == '__main__':
    main()
