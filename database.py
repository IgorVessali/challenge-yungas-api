#===============================================================================================================================
#   File with all data functions
#===============================================================================================================================


# JSON simulating data from the database
def database():
  return [
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "alagoas",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    }
  ]