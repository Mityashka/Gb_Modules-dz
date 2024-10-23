import logging

def main():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    debug_info_handler = logging.FileHandler('debug_info.log')
    debug_info_handler.setLevel(logging.DEBUG)
    debug_info_handler.setFormatter(formatter)

    warning_error_handler = logging.FileHandler('warnings_errors.log')
    warning_error_handler.setLevel(logging.WARNING)
    warning_error_handler.setFormatter(formatter)

    logger.addHandler(debug_info_handler)
    logger.addHandler(warning_error_handler)

    logger.debug('DEBUG Level')
    logger.info('INFO Level')
    logger.warning('WARNING Level')
    logger.error('ERROR Level')
    logger.critical('CRITICAL Level')


if __name__ == '__main__':
    main()