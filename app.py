from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger(log_uncaught_exceptions=True)

if __name__ == "__main__":
    raise(Exception("This will create a structured log"))
