
import importlib
import pprint

from info_monitor import get_info_providers


def check_interface() -> dict:
    info_providers = get_info_providers()
    if len(info_providers) == 0:
        report = {
            'No info providers': {
                'No info providers': 'No info providers'
            }
        }
        return report

    report = dict()

    for provider in info_providers:

        report[provider] = dict()

        module_eligible_for_next_check = True

        provider_module = importlib.import_module(f'info_providers.{provider}')

        module_has_get_info = hasattr(provider_module, 'get_info')
        report[provider]['01 - module has get info'] = module_has_get_info
        module_eligible_for_next_check = module_has_get_info

        if module_eligible_for_next_check:
            module_get_info_result = provider_module.get_info()
            module_returns_list = isinstance(module_get_info_result, list)
            report[provider]['02 - module returns list'] = module_returns_list
            module_eligible_for_next_check = module_returns_list

        if module_eligible_for_next_check:
            items_are_dictionaries = list()
            for item in module_get_info_result:
                items_are_dictionaries.append(isinstance(item, dict))
            report[provider]['03 - list contains dictionaries'] = all(items_are_dictionaries)
            module_eligible_for_next_check = all(items_are_dictionaries)

        if module_eligible_for_next_check:
            dictionaries_contain_info_key = list()
            for item in module_get_info_result:
                dictionaries_contain_info_key.append('info' in item)
            report[provider]['04 - dictionaries contain info key'] = all(dictionaries_contain_info_key)

    return report

if __name__ == '__main__':
    pprint.pprint(check_interface())

