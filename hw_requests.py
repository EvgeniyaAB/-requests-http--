import requests
import pprint


# #task 1
# url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
# resp = requests.get(url)
# resp_json = resp.json()
# heroes = ('Hulk', 'Captain America', 'Thanos')
# heroes_strenth = {}
# for num in resp_json:
#     for hero in heroes:
#         if hero == num['name']:
#             heroes_strenth[num['name']] = num['powerstats']['intelligence']
#
# print(max(heroes_strenth, key=heroes_strenth.get))

#task 2

import reddit
import yadisk
import pprint


class YandexDisk:
    def __init__(self, token):
        self.yandex_url = 'https://cloud-api.yandex.net/'
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = f'{self.yandex_url}v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(url=upload_url, headers=headers, params=params)

        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href_response = self._get_upload_link(disk_file_path=disk_file_path)
        href = href_response.get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))

        if response.status_code == 201:
            print("Загружено успешно")

if __name__ == '__main__':
    ya = YandexDisk(token="TOKEN")
    ya.upload_file_to_disk("Нетология_курс/New_file.txt", "New_file.txt")