import logging
import logging.handlers

class logManager:
    logging_initialized = False
    logger_instance = None

    @staticmethod
    def config_logger():
        logger = logging.getLogger(__name__)

        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)
        LOG_FILENAME = "test_output/TestLogs/tests.log"
        fileHandler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when='D', interval=1)
        fileHandler.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        consoleHandler.setFormatter(formatter)
        fileHandler.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(consoleHandler)
        logger.addHandler(fileHandler)

        # Logs
        # logger.debug('A debug message on log_config')
        # logger.info('An info message')
        # logger.warning('Something is not right.')
        # logger.error('A Major error has happened.')
        # logger.critical('Fatal error. Cannot continue')
        logManager.logging_initialized = True
        logManager.logger_instance = logger
        return logManager.logger_instance

    @staticmethod
    def get_logger_instance():
        if not logManager.logging_initialized:
            return logManager.config_logger()
        else:
            return logManager.logger_instance
