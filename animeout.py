from dl import DL

class animeoutDL(DL):
    _site = 'animeout'
    _search_url = 'https://www.animeout.xyz/?s='

    def _get_results(self, soup) -> list:
        results = []
        animes = soup.find('div', class_='row responsive-cols kleo-masonry per-row-4').find_all('article')
        for anime in animes:
            header = anime.find('h3', class_='post-title entry-title').a
            name = self._clean_name(header.text)
            link = header['href']
            results.append((name, link, self._site))
        return results

    def _download_result(self, result: tuple):
        soup = self._get_soup(result[1])
        episodes = soup.find('p', style='text-align: center;').find_all('a', target='_blank')
        links = []
        # Pick out the episodes.
        for episode in episodes:
            if episode.text != 'Direct Download':
                continue
            link = episode['href']
            name = self._clean_name(link.split('.')[-2].split('/')[-1].split('] ')[1].split(' [')[0])
            links.append((link, name))
        # Download the episodes.
        episode_count = len(links)
        zfill_length = len(str(episode_count))
        for e in range(episode_count):
            self._display_progress('Downloading episode', e, episode_count)
            rel_path = f'animeout/{result[0]}/{links[e][1]}.mkv'
            self._download_file(links[e][0], rel_path)
        return
