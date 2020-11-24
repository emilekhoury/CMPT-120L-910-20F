import logging
import argparse

logger = logging.getLogger()
logger.setLevel(logging.WARNING)
parser = argparse.ArgumentParser()

parser.add_argument("-n", "--number", 
    help="This will be the number inputed",
    type=int)
args = parser.parse_args()
number = args.number

logger.info(number)

def sigma_notation(n, total):
    if n == 10:
        return (total)
    
    return sigma_notation(n + 1, n + total)

print(sigma_notation(number, 0))