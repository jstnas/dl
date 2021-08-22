import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

class DL:
    _site: str
    _search_url: str
    _folder_name: str
    _parser: str = 'html.parser'

    def __init__(self, query: str):
        # Get results from the query.
        encoded_query = quote(query)
        full_url = self._search_url + encoded_query
        soup = self._get_soup(full_url)
        results = self._get_results(soup)
        result = self._pick_result(results)
        self._folder_name = result[0]
        self._download_result(result)
        return

    def _get_soup(self, url: str) -> BeautifulSoup:
        request = requests.get(url)
        request.raise_for_status()
        return BeautifulSoup(request.content, self._parser)

    def _get_results(self, soup) -> list:
        raise NotImplementedError('A downloader needs to implement get results function')

    def _pick_result(self, results: list) -> tuple:
        self._display_results(results)
        while True:
            try:
                option = input('choose which to download: ')
                # Return the first option by default.
                if option == '':
                    return results[0]
                option = int(option)
            except ValueError:
                print('option has to be an integer')
                continue
            if option < 0 or option >= len(results):
                print(f'option has to be between 0 and {len(results)}')
                continue
            return results[option]
        return None

    def _display_results(self, results: list):
        for r in range(len(results)):
            clean_result = results[r][0]
            print(f'{r} {clean_result}')
        return

    def _download_result(self, result: tuple):
        raise NotImplementedError('A downloader needs to implement download results function')

    def _display_progress(self, msg: str, current: int, total: int):
        print(f'\r{msg} {current + 1}/{total}', end='')
        return

    def _clean_name(self, name: str) -> str:
        name = name.lower()
        # Remove certain characters.
        for c in '\n-:"\'':
            name = name.replace(c, '')
        # Replace whitespace with underline.
        name = '_'.join(name.split())
        return name
