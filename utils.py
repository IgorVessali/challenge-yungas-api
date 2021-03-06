#===============================================================================================================================
#   File with all shared functions
#===============================================================================================================================
import re
from flask import json, Response
#Formats the phone informed to the international standard
# 'people'-'required'-> Person who will have their phone formatted 
# 'nameItem'-'required'-> index of the list that the phone is
# 'nameNewItem'-'required'-> index where the phone will be
def formatPhone(people, nameItem, nameNewItem):
  if nameItem in people:
    try:
      people[nameNewItem] = []
      phone = re.sub("[^0-9]", "", people[nameItem])
      if len(phone) == 10 or len(phone == 11): phone = '+55' + phone
      people[nameNewItem].append(phone)
    except Exception as e:
      print(e)

# Removes the index from the list according to the parameters reported
# 'lst'-'required'-> the list with the data
# 'nameItem'-'required'-> index to be deleted
def removeItem(lst, nameItem):
  try:
    if nameItem in lst: lst.pop(nameItem)
  except:
    pass

# Paging the data informed according to the parameters informed
# 'date'-'required'-> the list that will be paged
# 'page_size'-'required'->  number of items per page
# 'page'-'required'->  of the current page
def paginate(data, page_size, page): 
  if data and page_size and page:
    paginated = [ data [ i:i + page_size] for i in range(0, len(data), page_size)]
    # Valid if the reported page is valid if it does not redirect to the first page
    if len(paginated) <= page -1 or page < 1:
      page = 1
      print('The reported page does not exist, you will be redirected to the page 1.')
    #  Select the itens from the current page
    selected_itens = paginated[page -1]
    json_data = {"page": page,
                  "page_size": page_size,
                  "total_itens": len(data),
                  "total_pages": len(paginated),
                  "itens": selected_itens}
    json_string = json.dumps(json_data, indent=2, ensure_ascii = False)
    #creating a Response object to set the content type and the encoding
    response = Response(json_string, content_type="application/json; charset=utf-8" )
    return response