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
    if(address == None):
      return "missing address" 
      
    geocode_result = self.gmaps.geocode(address)

    result = {
      "lat": geocode_result[0]["geometry"]["location"]["lat"],
      "long": geocode_result[0]["geometry"]["location"]["lng"]
    }

    return result

  def placeNearby(self, location, radius=None, p_type="restaurant", language="pt-BR", rank_by="distance"):
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

    OBS:
      1) not is able to use at same time rank_by and radius, only one must be choice
      2) vicinity property have possible to coming with few information, in this case let go doing regex to take just whether has some number
    '''
    # place_nearby_result = self.gmaps.places(location=location, query="boate", language=language)
    place_nearby_result = None

    if(radius != None):
      place_nearby_result = self.gmaps.places_nearby(location=location, radius=radius, type=p_type, language=language)
    else:
      place_nearby_result = self.gmaps.places_nearby(location=location, type=p_type, rank_by=rank_by, language=language)

    #check if the response have been success
    if(place_nearby_result["status"] != "OK"):
      return -1

    return place_nearby_result


class UtensilMaps(Gmaps):
  def __init__(self, key):
    super().__init__(key)

  def topFiveNearbyFoodPlace(self, address):
    if(address == None):
      return "missing address"

    #1) convert adress to lat-long
    coordinates = self.latlongToAddress(address=address)
    tuple_coordinates = (coordinates["lat"], coordinates["long"])
    
    #2) obtatin results with more closer
    nearby_restaurants = self.placeNearby(location=(tuple_coordinates)) 

    #3) take only five
    result = nearby_restaurants["results"][0:4] if nearby_restaurants != -1 else -1

    return result
     


if __name__ == '__main__':
  import json

  # gmaps = Gmaps(ENV.GMAPS_API_TWO)

  # geocoding_result_test = gmaps.latlongToAddress("Avenida Paulista, SP")
  # print(geocoding_result_test)
  # place_nearby_result_test = gmaps.placeNearby(location=(-23.5525567, -46.64398449999999), radius=30, p_type="restaurant", rank_by="distance")
  # with open("place_nearby_response.json", "w+") as file:
    # json.dump(place_nearby_result_test, file) # encode dict into JSON
  # with open("geocoding_response.json", "w+") as file:
    # json.dump(geocoding_result_test, file) # encode dict into JSON
  
  utensilMaps = UtensilMaps(ENV.GMAPS_API_TWO)
  print(utensilMaps.topFiveNearbyFoodPlace("Avenida Paulista, SP"))