#===============================================================================================================================
#   File with all shared functions
#===============================================================================================================================
import re
#Formats the phone informed to the international standard
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
def removeItem(lst, nameItem):
  try:
    if nameItem in lst: lst.pop(nameItem)
  except:
    pass

# Paging the data informed according to the parameters informed
# 'date' -> the list that will be paged
# 'page_size' -> number of items per page
# 'page' -> of the current page
def paginate(data, page_size, page): 
  if data and page_size and page:
    paginated = [data[i:i+page_size] for i in range(0, len(data), page_size)]
    # Valid if the reported page is valid if it does not redirect to the first page
    if len(paginated) <= page -1 or page < 1:
      page = 1
      print('The reported page does not exist, you will be redirected to the page 1.')
    #  Select the itens from the current page
    selected_itens = paginated[page -1]
  return {"page": page,
            "page_size": page_size,
            "total_itens": len(data),
            "total_pages": len(paginated),
            "itens": selected_itens
          }