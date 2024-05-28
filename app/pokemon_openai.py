from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

my_api_key = os.getenv('API_KEY')

client = OpenAI(api_key=my_api_key)

MODEL = "gpt-3.5-turbo-0125"
TEMP = 0.7

def get_response_openai(input_data):
    """Generate a response using the OpenAI chat model.

       This function uses the OpenAI chat model to generate a response based on the input data provided.

       Args:
           input_data (str): The input text data to be used for generating the response.

       Returns:
           dict: A dictionary containing structured data about a Pokémon based on the input text.
               The structured data includes the name of the Pokémon, its main color, types, and abilities.
       """
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "Your main job is convert unstructured text to structured JSON."
                           "Data will be related with Pokemons."
            },
            {
                "role": "user",
                "content": input_data
            }
        ],
        functions=[
            {
                "name": "extract_pokemon_info",
                "description": "Return structured data of pokemon",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_pokemon": {
                            "type": "string",
                            "description": "Name of pokemon"
                        },
                        "color": {
                          "type": "string",
                          "description": "Main color of pokemon",
                        },
                        "type": {
                            "type": "array",
                            "description": "Return type of pokemon e.g. [Green], [Fire, Green]",
                            "items": {
                                "type": "string"
                            }
                        },
                        "ability_name": {
                            "type": "array",
                            "description": "Return type of pokemon e.g. [Cut], [Jump, Hypnosis]",
                            "items": {
                                "type": "string"
                            }
                        },
                    },
                "required": ["name_pokemon"]
                }
            }
        ],
        function_call="auto",
        temperature=TEMP,
        top_p=1
    )
    return completion.choices[0].message.function_call.arguments

# print(get_response_openai("Bulbasaur is a small, squat Pokémon with blue-green skin and a big red bulb on its back. "
#                           "This bulb is actually a seed that will eventually blossom into a flower. Bulbasaur is a "
#                           "dual-type Grass and Poison Pokémon, and it's one of the first Pokémon you can choose as "
#                           "a starter in the classic Pokémon Red and Blue games.  It evolves into Ivysaur at level 16,"
#                           " and then Venusaur at level 32. Skill Jump and Overkill"))
