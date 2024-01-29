from pathlib import Path
import logging

import helpers.load as load
import helpers.matrix as matrix
<<<<<<< Updated upstream
import helpers.logger.loggersetup as loggersetup
=======
import helpers.log.config as logconfig
import helpers.log.decorators as logdecorators
from pathlib import Path

>>>>>>> Stashed changes
import battleship
import helpers.matrix as matrix

<<<<<<< Updated upstream

loggersetup.setup(level='DEBUG')
logger = logging.getLogger(__name__)

=======
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
>>>>>>> Stashed changes
def main(solution):
    logger.info(f'START main: {logger.getEffectiveLevel() = }')
    extensions = 'json, ascii, csv'
    for file_path in load.get_files('battlefield.ascii'):
        tests = load.battlefield(file_path)
        for test in tests:
            name = test['name']
            battlefield = test['data']
            expected = test['expected']

            battlefield = get_converter(name)(battlefield)
            matrix.display(battlefield, clear_screen=False)
            result = solution(battlefield)
            logger.info(f'{name} -> {result = } -> {expected = }')
            
            print()
            print()


if __name__ == '__main__':
    import sys
    sys.exit(main(solution=battleship.validate))