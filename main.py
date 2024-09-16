import requests
# library to fetch data 

# FUNCTION TO FETCH DATA 
def getPokemonData(pokemon):
    
    # url to fetch
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"
    
    # send get request to the API
    response = requests.get(url)
    
    # check if the response was succesful (status code 200)
    if response.status_code == 200:
        data = response.json()
        return data
    
    else:
        return None
    







    
    
    
    
    
    