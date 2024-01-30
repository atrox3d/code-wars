import logging
from pathlib import Path

import helpers.log.config as logconfig
import helpers.log.decorators as logdecorators
import helpers.loader as loader
import helpers.matrix as matrix

import battleship

config = logconfig.setup_logging(level='INFO')
logger = logging.getLogger(__name__)

logdecorators.decorate_module_functions(
                                module=battleship, 
                                decorator=logdecorators.logdecorator, 
                                log=logger.debug,
                                max_args_len=10
            )
def get_converter(filename):
    def nullconverter(battlefield):
        return battlefield
    
    extension = Path(filename).suffix
    if extension == '.ascii':
        return matrix.ascii_to_int
    elif extension == '.csv':
        return matrix.csv_to_int
    elif extension == '.json':
        return nullconverter
    else:
        raise NotImplementedError(f'extension {extension} is not implemented')

@logdecorators.logdecorator()
def main(solution):
    extensions = 'json, ascii, csv'
    for file_path in loader.get_files(extensions=extensions):
        tests = loader.load_battlefield(file_path)
        for test in tests:
            logger.debug(f'{test = }')
            
            battlefield = get_converter(test['filename'])(test['data'])
            matrix.display(battlefield, clear_screen=False)
            
            result = solution(battlefield)
            logger.info(f'{test["filename"]}::{test["name"]}: {result = } expected: {test["expected"]}')
            print()
            print()

if __name__ == '__main__':
    import sys
    sys.exit(main(solution=battleship.validate))