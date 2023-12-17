import json
import haversine


class Scanner():
    def __init__(self):
        self.user_coord = tuple

        self.closest_dest = float
        self.closest_lat = float
        self.closest_lon = float
        self.closest_adress = str
        self.closest_type = str
        self.closest_timework = str
        self.closest_content = str

    def toilet_parse(self):
        with open('data.json', 'r') as f:
            data = json.load(f)

            for i in data:
                try:
                    t_lat = float(i['lat'])
                    t_lon = float(i['lng'])
                    t_coord = (t_lat, t_lon)
                except ValueError:
                    pass

                haversine_calc = haversine.haversine(self.user_coord, t_coord)

                try:
                    if self.closest_dest > haversine_calc:

                        self.closest_dest = haversine_calc
                        self.closest_lat = i['lat']
                        self.closest_lon = i['lng']
                        self.closest_adress = i['address']
                        self.closest_type = i['type']
                        self.closest_timework = i['timework']
                        self.closest_content = i['content']

                except TypeError:
                    self.closest_dest = haversine_calc
