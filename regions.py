#===============================================================================================================================
#   File with all regions functions
#===============================================================================================================================

# Returns the region corresponding to the reported state
# 'state' -> Name of the state you want to search for
def findRegion(state):
  regions = list_regions_and_state()
  region = [ x[0] for x in regions if state in x]
  return region[0]

# Returns the list of states and their region
def list_regions_and_state():
  return  [
            ["sul", "rio grande do sul"], 
            ["sul", "paraná"], 
            ["sul", "santa catarina"], 
            ["sudeste", "são paulo"], 
            ["sudeste", "minas gerais"], 
            ["sudeste", "rio de janeiro"], 
            ["sudeste", "espírito santo"], 
            ["centro-oeste", "mato grosso"], 
            ["centro-oeste", "distrito federal"], 
            ["centro-oeste", "mato grosso do sul"], 
            ["centro-oeste", "goiás"], 
            ["nordeste", "bahia"], 
            ["nordeste", "pernambuco"], 
            ["nordeste", "ceará"], 
            ["nordeste", "pará"], 
            ["nordeste", "maranhão"], 
            ["nordeste", "paraíba"], 
            ["nordeste", "rio grande do norte"], 
            ["nordeste", "alagoas"], 
            ["nordeste", "sergipe"], 
            ["nordeste", "piauí"], 
            ["norte", "amazonas"], 
            ["norte", "rondônia"], 
            ["norte", "tocantins"], 
            ["norte", "acre"], 
            ["norte", "amapá"], 
            ["norte", "roraima"] 
          ]
