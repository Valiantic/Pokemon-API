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
    

# Function to fetch Pokémon species data for description
def get_pokemon_species_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
# FUNCTION TO PROCESS THE DATA INFO OF A POKEMON 

def pokemonInfo(pokemon):
    data = getPokemonData(pokemon)
    species_data = get_pokemon_species_data(pokemon)
    
    if data:
        
        # extract details
        print(f"Name: {data['name'].capitalize()}")
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")
        print(f"Base Experience: {data['base_experience']}")
    
        # prints the types of the pokemon
        types = [t['type']['name'] for t in data['types']]
        print(f"Types: {', '.join(types)}")
        
        # Print the description if available in species data
        if species_data:
            flavor_texts = species_data['flavor_text_entries']
            for entry in flavor_texts:
                if entry['language']['name'] == 'en':
                    description = entry['flavor_text'].replace('\n',' ')
                    print(f"Description: {description}")
                    print('')
                    break
        else:
            print("Description not available.")
            
            
            
        # show all moveset 
        
        moveset = [m['move']['name'] for m in data['moves']]
        print(f"All moves: {', '.join(moveset)}")
        
        
        
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
    
    
    




    
    
    
    
    
    