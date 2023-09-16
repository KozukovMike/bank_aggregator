from bank.loggs.loggers import logger_pars_errors


class ParsErrors(Exception):

    @staticmethod
    def write_to_log(e: Exception, text: str = None) -> None:
        """
        Write error to log file
        """
        logger_pars_errors.error(f'e: {e} \n text: {text}')



