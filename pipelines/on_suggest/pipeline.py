from datetime import datetime
import keypirinha as kp


def pipeline():
    return [
        break_if_keyword_is_not_recognized,
        put_time_suggestion,
        show_suggestions
    ]


def show_suggestions(args):

    plugin = args.get('plugin')
    suggestions = args.get('suggestions')

    if suggestions:
        plugin.set_suggestions(suggestions, kp.Match.ANY, kp.Sort.NONE)


def put_time_suggestion(args):

    plugin = args.get('plugin')
    input = args.get("user_input")
    config = plugin.config

    current_time = datetime.now()
    time_label = current_time.strftime(config.time_title_format())
    date_label = config.show_time_description() and current_time.strftime(
        config.time_description_format()) or ""

    args["suggestions"] = [plugin.create_item(
        category=kp.ItemCategory.USER_BASE + 1,
        label=time_label,
        short_desc=date_label,

        # (on_execute) Some value that is passed to on_execute.
        target="target",

        # (arguments) The item object does not accept arguments.
        args_hint=kp.ItemArgsHint.FORBIDDEN,

        # (history) The item object will not be added to History.
        hit_hint=kp.ItemHitHint.IGNORE
    )]

def break_if_keyword_is_not_recognized(args):
    plugin = args['plugin']
    input = args.get("user_input")
    
    text = input.lower()
    if text not in plugin.config.time_keywords():
        args['aborted'] = True
