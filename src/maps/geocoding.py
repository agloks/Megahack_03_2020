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

  from googlemaps.places import find_place
  from googlemaps.places import places
  from googlemaps.places import places_nearby
  from googlemaps.places import place
  from googlemaps.places import places_photo
  from googlemaps.places import places_autocomplete
  from googlemaps.places import places_autocomplete_query
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

  def placeNearby(self, location, radius, language="br"):
      '''
      :param location: The latitude/longitude value for which you wish to obtain the
                        closest, human-readable address.
      :type location: string, dict, list, or tuple

      :param radius: Distance in meters within which to bias results.
      :type radius: int

      :param region: The region code, optional parameter.
      See more @ https://developers.google.com/places/web-service/search
      :type region: string

      :param min_price: Restricts results to only those places with no less than
                        this price level. Valid values are in the range from 0
                        (most affordable) to 4 (most expensive).
      :type min_price: int

      :param max_price: Restricts results to only those places with no greater
                        than this price level. Valid values are in the range
                        from 0 (most affordable) to 4 (most expensive).
      :type max_price: int

      :param name: One or more terms to be matched against the names of places.
      :type name: string or list of strings

      :param open_now: Return only those places that are open for business at
                      the time the query is sent.
      :type open_now: bool

      :param rank_by: Specifies the order in which results are listed.
                      Possible values are: prominence (default), distance
      :type rank_by: string

      :rtype: result dict with the following keys:
              status: status code
              results: list of places
              html_attributions: set of attributions which must be displayed
              next_page_token: token for retrieving the next page of results
      '''
      place_nearby_result = self.gmaps.places(location=location, query="boate", language=language)
      return place_nearby_result



if __name__ == '__main__':
  o_gmaps = Gmaps(ENV.GMAPS_API_TWO)

  # print(o_gmaps.latlongToAddress("Avenida Paulista, SP"))
  print(o_gmaps.placeNearby((-23.5525567, -46.64398449999999), 20))