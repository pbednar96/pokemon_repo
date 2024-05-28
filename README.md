## Pokemon - OPENAI API

Welcome to the Pokémon API powered by OpenAI!

Gotta Catch 'Em All.

#### How to run:
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