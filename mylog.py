import logging


def make_console_handler(level):
    console = logging.StreamHandler()
    console.setLevel(level)
    return console


def setup_logging(option, level=logging.INFO):
    logging.root.setLevel(level)
    # logging.root.addHandler(json_handler)

    # 'silent handler is ignored'
    if option == 'console':
        console_handler = make_console_handler(level)
        format_str = '%(asctime)s %(name)-30s %(levelname)-8s %(message)s'
        datefmt_str = '%m-%d %H:%M'
        console_handler.setFormatter(
            logging.Formatter(format_str, datefmt_str))
        logging.root.addHandler(console_handler)
