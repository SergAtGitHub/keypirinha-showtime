import keypirinha as kp
from datetime import datetime


class ShowTime(kp.Plugin):

    def __init__(self):
        super().__init__()

    def on_start(self):
        self.acceptable_time_inputs = [
            "time",
            "now"
        ]

    def on_suggest(self, user_input, items_chain=[]):
        args = {'user_input': user_input}

        suggestions = self.get_time_suggestions(args)
        
        self.set_suggestions(list(suggestions),
                             kp.Match.ANY, kp.Sort.NONE)

    def get_time_suggestions(self, args):
        input = args.get("user_input")

        text = input.lower()
        if text not in self.acceptable_time_inputs:
            return

        time_label = datetime.now()

        yield self.create_item(
            category=kp.ItemCategory.USER_BASE + 1,
            label=time_label.strftime("%H:%M"),
            short_desc="",

            # (on_execute) Some value that is passed to on_execute.
            target="target",

            # (arguments) The item object does not accept arguments.
            args_hint=kp.ItemArgsHint.FORBIDDEN,

            # (history) The item object will not be added to History.
            hit_hint=kp.ItemHitHint.IGNORE
        )
