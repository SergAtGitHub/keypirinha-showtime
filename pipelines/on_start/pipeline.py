from ...settings import Settings, SettingsHolder


def pipeline():
    return [
        init_settings,
        load_settings
    ]


def init_settings(args):
    plugin = args['plugin']
    plugin.config = Settings(SettingsHolder())


def load_settings(args):
    plugin = args['plugin']
    plugin.config.holder.fill_settings(plugin.load_settings())
