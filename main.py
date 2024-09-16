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
    
# FUNCTION TO PROCESS THE DATA INFO OF A POKEMON 

def pokemonInfo(pokemon):
    data = getPokemonData(pokemon)
    
    if data:
        
        # extract details
        print(f"Name: {data['name'].capitalize()}")
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")
        print(f"Base Experience: {data['base_experience']}")
        
        # prints the types of the pokemon
        types = [t['type']['name'] for t in data['types']]
        print(f"Types: {', '.join(types)}")
    else:
        print(f"Pokemon '{pokemon}' not found.")




def main():
    # get user input
    pokedex = input("\nEnter the name of the Pokemon: ")
    
    # display pokemon info
    pokemonInfo(pokedex)
    
if __name__ == "__main__":

    while True:
        main()
    
    
    




    
    
    
    
    
    