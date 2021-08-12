from dl import DL

class animeoutDL(DL):
    _site = 'animeout'
    _search_url = 'https://www.animeout.xyz/?s='

    def _get_results(self, soup) -> list:
        results = []
        animes = soup.find('div', class_='row responsive-cols kleo-masonry per-row-4').find_all('article')
        for anime in animes:
            header = anime.find('h3', class_='post-title entry-title').a
            name = header.text
            link = header['href']
            results.append((name, link, self._site))
        return results
