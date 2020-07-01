'''
Url documentation -->
  https://developers.google.com/maps/documentation/geocoding/get-api-key?hl=pt_BR
  https://developers.google.com/maps/documentation/javascript/geocoding?hl=pt_BR
  https://github.com/googlemaps/google-maps-services-python

Easy use -->
  by url:
    https://maps.googleapis.com/maps/api/geocode/json?address=<<1600+Amphitheatre+Parkway,+Mountain+View,+CA>>&key=<<YOUR_API_KEY>>

  or client by library :
    googlemaps  
'''

import googlemaps
from datetime import datetime

from DI import ENV

class Gmaps:
  def __init__(self, key):
    self.gmaps = googlemaps.Client(key=key)

  def latlongToAddress(self, address=None):
    #example address = 1600 Amphitheatre Parkway, Mountain View, CA
    if(address):
      geocode_result = self.gmaps.geocode(address)
    else:
      geocode_result = self.gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

    return geocode_result


if __name__ == '__main__':
  o_gmaps = Gmaps(ENV.GMAPS_API_TWO)

  print(o_gmaps.latlongToAddress("Centro"))