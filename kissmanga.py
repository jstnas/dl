import requests
import os
from dl import DL

class kissmangaDL(DL):
    _site = 'kissmanga'
    _base_url = 'https://kissmanga.org'
    _search_url = f'{_base_url}/manga_list?action=search&q='

    def _get_results(self, soup) -> list:
        results = []
        mangas = soup.find('div', class_='listing full').find_all('div', class_='item_movies_in_cat')
        for manga in mangas:
            header = manga.find('a', class_='item_movies_link')
            name = self._clean_name(header.text)
            link = self._base_url+header['href']
            results.append((name, link, self._site))
        return results

    def _download_result(self, result: tuple):
        chapters = self._get_chapters(result[1])
        chapter_count = len(chapters)
        zfill_length = len(str(chapter_count))
        for c in range(chapter_count):
            print(f'Downloading chapter {c + 1}/{chapter_count}')
            index = str(c).zfill(zfill_length)
            self._download_chapter(index, chapters[c])
        return

    def _get_chapters(self, link: str) -> list:
        chapters = []
        soup = self._get_soup(link).find('div', class_='listing listing8515 full').find_all('a')
        for chapter in soup:
            chapter_name = self._clean_name(chapter.text)
            chapter_link = self._base_url+chapter['href']
            chapters.insert(0, (chapter_name, chapter_link))
        return chapters

    def _download_chapter(self, prefix: str, chapter: tuple):
        soup = self._get_soup(chapter[1])
        images = soup.find('div', id='centerDivVideo').find_all('img')
        image_count = len(images)
        zfill_length = len(str(image_count))
        for i in range(image_count):
            self._display_progress('Downloading image', i, image_count)
            name = str(i).zfill(zfill_length)
            rel_path = f'{self._folder_name}/{prefix}_{chapter[0]}/{name}.jpg'
            self._download_file(images[i]['src'], rel_path)
        print()
        return
