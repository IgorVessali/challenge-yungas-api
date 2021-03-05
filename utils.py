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