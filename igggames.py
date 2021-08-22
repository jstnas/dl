from urllib.parse import unquote
from dl import DL

class igggamesDL(DL):
    _site = 'igggames'
    _search_url = 'https://igg-games.cc/search/'

    def _get_results(self, soup) -> list:
        results = []
        games = soup.find('div', class_='uk-width-expand@m').find_all('a', class_='uk-link-reset')
        for game in games:
            name = self._clean_name(game.text)
            link = game['href']
            results.append((name, link, self._site))
        return results

    def _download_result(self, result: tuple):
        soup = self._get_soup(result[1])
        providers = soup.find_all('b', class_='uk-heading-bullet')
        results = []
        for provider in providers:
            link = unquote(provider.next_sibling.next_sibling['href'].split('=')[1])
            name = self._clean_name(link.split('//')[1].split('.')[0])
            print(link)
        return
