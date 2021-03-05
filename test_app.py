from app import *

def test_get_peoples_status():   
  client = app.test_client()
  url = '/peoples'

  response = client.get(url)
  assert response.status_code == 200

def test_get_peoples_content_type():   
  client = app.test_client()
  url = '/peoples'

  response = client.get(url)
  assert response.status_code == 200
  assert response.content_type == 'application/json'

def test_get_peoples_istance():   
  client = app.test_client()
  url = '/peoples'

  response = client.get(url)
  assert response.status_code == 200
  assert isinstance(response.json, dict)

def test_get_regions_status():   
  client = app.test_client()
  url = '/peoples'

  response = client.get(url)
  assert response.status_code == 200

def test_get_regions_content_type():   
  client = app.test_client()
  url = '/peoples'

  response = client.get(url)
  assert response.status_code == 200
  assert response.content_type == 'application/json'

def test_get_regions_istance():   
  client = app.test_client()
  url = '/peoples'

  response = client.get(url)
  assert response.status_code == 200
  assert isinstance(response.json, dict)

def test_get_peoples_pagination_default():   
  client = app.test_client()
  url = '/peoples'
  
  response = client.get(url)
  assert response.status_code == 200
  assert set(response.json.keys()) >= {'page', 'page_size', 'total_itens', 'itens'}
  assert response.json['page'] == 1
  assert response.json['page_size'] == 20

def test_get_peoples_set_pagination():   
  client = app.test_client()
  url = '/peoples?page_size=2&page=2'
  
  response = client.get(url)
  assert response.status_code == 200
  assert set(response.json.keys()) >= {'page', 'page_size', 'total_itens', 'itens'}
  assert response.json['page'] == 2
  assert response.json['page_size'] == 2

def test_get_peoples_per_region_pagination_default():   
  client = app.test_client()
  url = '/peoples/sul'
  
  response = client.get(url)
  assert response.status_code == 200
  assert set(response.json.keys()) >= {'page', 'page_size', 'total_itens', 'itens'}
  assert response.json['page'] == 1
  assert response.json['page_size'] == 20 

def test_get_peoples_per_region_set_pagination():   
  client = app.test_client()
  url = '/peoples/sul?page_size=1&page=2'
  
  response = client.get(url)
  assert response.status_code == 200
  assert set(response.json.keys()) >= {'page', 'page_size', 'total_itens', 'itens'}
  assert response.json['page'] == 2
  assert response.json['page_size'] == 1

def test_get_regions_pagination_default():   
  client = app.test_client()
  url = '/regions'
  
  response = client.get(url)
  assert response.status_code == 200
  assert set(response.json.keys()) >= {'page', 'page_size', 'total_itens', 'itens'}
  assert response.json['page'] == 1
  assert response.json['page_size'] == 20

def test_get_regions_set_pagination():   
  client = app.test_client()
  url = '/regions?page_size=2&page=2'
  
  response = client.get(url)
  assert response.status_code == 200
  assert set(response.json.keys()) >= {'page', 'page_size', 'total_itens', 'itens'}
  assert response.json['page'] == 2
  assert response.json['page_size'] == 2

def test_get_peoples_count_itens_default():   
  client = app.test_client()
  url = '/peoples'
  
  response = client.get(url)
  assert response.status_code == 200
  assert len(response.json['itens']) == 20

def test_get_peoples_count_itens_set_pagination():   
  client = app.test_client()
  url = '/peoples?page_size=10&page=1'
  
  response = client.get(url)
  assert response.status_code == 200
  assert len(response.json['itens']) == 10

def test_get_peoples_per_region_count_itens_default():   
  client = app.test_client()
  url = '/peoples/sul'
  
  response = client.get(url)
  assert response.status_code == 200
  assert len(response.json['itens']) == 20

def test_get_peoples_per_region_count_itens_set_pagination():   
  client = app.test_client()
  url = '/peoples/sul?page_size=5&page=1'
  
  response = client.get(url)
  assert response.status_code == 200
  assert len(response.json['itens']) == 5

def test_get_regions_count_itens_default():   
  client = app.test_client()
  url = '/regions'
  
  response = client.get(url)
  assert response.status_code == 200
  assert len(response.json['itens']) == 5

def test_get_regions_count_itens_set_pagination():   
  client = app.test_client()
  url = '/regions?page_size=3&page=1'
  
  response = client.get(url)
  assert response.status_code == 200
  assert len(response.json['itens']) == 3
