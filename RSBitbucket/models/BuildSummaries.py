import sys

class BuildSummaries:
    def __init__(self, cancelled, successful, in_progress, failed, unknown):
        self.cancelled = cancelled
        self.successful = successful
        self.in_progress = in_progress
        self.failed = failed
        self.unknown = unknown

    def display_status(self) -> str:
        if self.cancelled:
            return 'Cancelled'
        if self.successful:
            return 'Successful'
        if self.in_progress:
            return 'In progress'
        if self.failed:
            return 'Failed'
        if self.unknown:
            return 'Unknown'

    def display_status_emoji(self) -> str:
        if self.cancelled:
            return '⏹️'
        if self.successful:
            return '✅'
        if self.in_progress:
            return '🔵'
        if self.failed:
            return '❌'
        if self.unknown:
            return '🤷'



    @classmethod
    def from_response(cls, response):
        values = list(response.values())[0]
        cancelled = values['cancelled']
        successful = values['successful']
        in_progress = values['inProgress']
        failed = values['failed']
        unknown = values['unknown']
        return cls(cancelled, successful, in_progress, failed, unknown)

    @classmethod
    def empty(cls):
        return  cls(0,0,0,0,0)


