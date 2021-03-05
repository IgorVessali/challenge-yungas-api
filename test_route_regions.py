#===============================================================================================================================
#   File with all tests for route regions
#===============================================================================================================================

from app import *

# Tests the return status
def test_get_regions_status():   
  client = app.test_client()
  url = '/peoples'

  response = client.get(url)
  assert response.status_code == 200
# Tests the return content-type
def test_get_regions_content_type():   
  client = app.test_client()
  url = '/peoples'

  response = client.get(url)
  assert response.status_code == 200
  assert response.content_type == 'application/json'
# Tests the return instance
def test_get_regions_istance():   
  client = app.test_client()
  url = '/peoples'

  response = client.get(url)
  assert response.status_code == 200
  assert isinstance(response.json, dict)
# Tests the return of the route with the default pagination
def test_get_regions_pagination_default():   
  client = app.test_client()
  url = '/regions'
  
  response = client.get(url)
  assert response.status_code == 200
  assert set(response.json.keys()) >= {'page', 'page_size', 'total_itens', 'itens'}
  assert response.json['page'] == 1
  assert response.json['page_size'] == 20
# Checks if the return of the route is paged past the desired values
def test_get_regions_set_pagination():   
  client = app.test_client()
  url = '/regions?page_size=2&page=2'
  
  response = client.get(url)
  assert response.status_code == 200
  assert set(response.json.keys()) >= {'page', 'page_size', 'total_itens', 'itens'}
  assert response.json['page'] == 2
  assert response.json['page_size'] == 2
# Checks whether the route is returning to default item quantities
def test_get_regions_count_itens_default():   
  client = app.test_client()
  url = '/regions'
  
  response = client.get(url)
  assert response.status_code == 200
  assert len(response.json['itens']) == 5
# Checks whether the route is returning the reported item quantities
def test_get_regions_count_itens_set_pagination():   
  client = app.test_client()
  url = '/regions?page_size=3&page=1'
  
  response = client.get(url)
  assert response.status_code == 200
  assert len(response.json['itens']) == 3
