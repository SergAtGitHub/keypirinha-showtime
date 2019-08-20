class SettingsHolder:

    def __init__(self):
        self.settings = {
            "time": {
                "show_time_keywords": {
                    "default": ["time", "now"],
                    "type": "multiline"
                },
                "show_additional_info_in_description": {
                    "default": False,
                    "type": "bool"
                },
                "time_title_format":  {
                    "default": "%H:%M",
                    "type": ""
                },
                "time_description_format": {
                    "default": "%x",
                    "type": ""
                }
            }
        }

    def fill_settings(self, settings_provider):
        for (k, v) in self.settings.items():
            self.fill_section(settings_provider, k, v)

    def fill_section(self, settings_provider, sectionName, sectionValue):
        for (k, v) in sectionValue.items():
            self.fill_setting(settings_provider, sectionName, k, v)

    def fill_setting(self, settings_provider, sectionName, settingName, settingValue):
        default = settingValue["default"]
        expected_type = settingValue["type"]
        method = "get"

        if expected_type:
            method += "_" + expected_type

        method_to_call = getattr(settings_provider, method)

        settingValue["value"] = method_to_call(
            settingName, sectionName, default)


class Settings:
    def __init__(self, holder):
        self.holder = holder
        self.settings = holder.settings

    def time_keywords(self) -> list:
        return self.settings["time"]["show_time_keywords"]["value"]

    def show_time_description(self) -> bool:
        return self.settings["time"]["show_additional_info_in_description"]["value"]

    def time_description_format(self) -> str:
        return self.settings["time"]["time_description_format"]["value"]

    def time_title_format(self) -> str:
        return self.settings["time"]["time_title_format"]["value"]
