class WeatherDataRow:
    def __init__(self, pkt, max_temp, mean_temp, min_temp, max_humidity, mean_humidity):
        self.pkt = pkt
        self.max_temp = int(max_temp) if max_temp is not None and max_temp != '' else 0
        self.mean_temp = int(mean_temp) if mean_temp is not None and mean_temp != '' else 0
        self.min_temp = int(min_temp) if min_temp is not None and min_temp != '' else 0
        self.max_humidity = int(max_humidity) if max_humidity is not None and max_humidity != '' else 0
        self.mean_humidity = int(mean_humidity) if mean_humidity is not None and mean_humidity != '' else None

