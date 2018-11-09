import requests


class SdgApi:
    base = 'https://unstats.un.org/SDGAPI'

    def get(self, extension):
        url = self.base + extension
        return requests.get(url).json()

    # GeoArea

    def GeoArea_list(self):
        return self.get('/v1/sdg/GeoArea/List')


    # Series

    def Series_list(self):
        return self.get('/v1/sdg/Series/List')

