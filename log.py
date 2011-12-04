#! /usr/bin/python2.7

import logging

logging.basicConfig(filename='/tmp/example.log',level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(module)-10s %(funcName)-10s> %(message)s')

logger = logging.getLogger(__name__)
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
