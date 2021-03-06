supported_distributions = {
    'chi2': '$\chi^2$'
}


class DistributionError(Exception):
    """
        Error for unsupported distribution input
    """
    def __init__(self, code):
        self.code = code

    def __str__(self):
        exception_msg = "Distribution {} is not supported".format(self.code)
        return exception_msg
