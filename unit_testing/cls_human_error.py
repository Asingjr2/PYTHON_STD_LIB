"""Custom exception class to handle human input error."""


class HumanError(Exception):
    def __init__(self, cause):
        self.cause = cause
        self.message = 'Something happened HUMAN'
        