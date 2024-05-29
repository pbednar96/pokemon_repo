## Pokemon - OPENAI API

Welcome to the Pokémon API powered by OpenAI!

Gotta Catch 'Em All.

### Used technologies:
* Python 3.9
* Docker
* OPENAI API
* Python libs:
  * flask
  * openai
  * python-dotenv

    
### How to run:
Set your `.env` with your valid OPENAI API key.
(NOTE: add .env file to the root of project)

#### Example:
API_KEY="sk-proj-xxx"

##### How to docker:
```
docker build -t pokemon_container .

docker run -p 8080:8080 pokemon_container
```

#### Example request:
```
'POST'
URL: http://127.0.0.1:8080/structured 
BODY: {"text":"Bulbasaur is a small, squat Pokémon with blue-green skin and a big red bulb on its back. This bulb is actually a seed that will eventually blossom into a flower. Bulbasaur is a dual-type Grass and Poison Pokémon, and it's one of the first Pokémon you can choose as a starter in the classic Pokémon Red and Blue games.  It evolves into Ivysaur at level 16, and then Venusaur at level 32."}
```

#### Run unittests:
```
python -m unittest .\test_main.py
```

#### Description:
To convert unstructured data to structured data, I decided to use the OpenAI GPT-3.5 Turbo model with function calling.

#### TODO improvements:
The structured data can be extended for more fields.