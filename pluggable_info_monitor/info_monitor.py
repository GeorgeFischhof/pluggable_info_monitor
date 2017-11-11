
import importlib
from pathlib import Path
import sys

from flask import Flask, redirect, render_template, request, url_for
from waitress import serve

from PIM_config import index_page_number_of_columns
from PIM_config import show_next_info_after_seconds
from PIM_config import web_server_ip_address
from PIM_config import web_server_port_number
from PIM_config import welcome_message_on_index_page
from version import version, version_date


app = Flask(__name__)


def get_info_providers(test_mode=False) -> list:
    info_path = Path('info_providers')
    info_provider_files = [file for file in info_path.glob('*.py')]
    info_providers = [provider.stem for provider in info_provider_files]

    info_providers.sort()
    return info_providers


@app.route('/')
def index():
    info_providers = get_info_providers()
    if len(info_providers) != 0:
        next_provider = info_providers[0]
    else:
        next_provider = ''
    base_url = url_for('info_pages', provider='')
    version_string = f'v{version} ({version_date})'
    return render_template('index.html',
                           welcome_message_on_index_page=welcome_message_on_index_page,
                           base_url=base_url,
                           info_providers=info_providers,
                           next_provider=next_provider,
                           show_next_info_after_seconds=show_next_info_after_seconds,
                           index_page_number_of_columns=index_page_number_of_columns,
                           version=version_string)


@app.route('/info_pages/<provider>')
def info_pages(provider):
    provider_path = 'info_providers'
    providers = get_info_providers()

    if provider in providers:
        try:
            next_provider = providers[(providers.index(provider)) + 1]
        except IndexError:
            next_provider = providers[0]

        provider_module = importlib.import_module(f'{provider_path}.{provider}')
        if hasattr(importlib, 'reload'):
            provider_module = importlib.reload(provider_module)

        info = provider_module.get_info()

        return render_template('info_screen.html',
                               title=provider,
                               next_provider=next_provider,
                               info=info,
                               show_next_info_after_seconds=show_next_info_after_seconds)

    else:
        return redirect(url_for('index'))

    # caching can be solved
    # with generated template from Jinja ... next version


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    serve(app, listen=f'{web_server_ip_address}:{web_server_port_number}')
