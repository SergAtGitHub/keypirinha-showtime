from keypirinha import Plugin
from .pipelines import pipelines as p


class ShowTime(Plugin):
    """
    Plugin that is intended to show the current time.
    """

    def __init__(self):
        """
        Empty constructor, making a call to base.
        """
        super().__init__()

    def on_start(self):
        args = {'plugin': self}
        p.on_start(args)

    def on_suggest(self, user_input, items_chain=[]):
        args = {'plugin': self, 'user_input': user_input,
                'items_chain': items_chain}
        p.on_suggest(args)
