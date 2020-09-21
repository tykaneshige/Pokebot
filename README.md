# Pokebot

*Thomas Kaneshige (tykaneshige.work@gmail.com)* </br>
*Ryan Tsukamoto (ryantsukamoto@yahoo.com)* </br>
*Kiane Wang* </br>
*Nicholas Yamamoto* </br>

---

## Command List

* All valid commands to the program will be prefixed with '!poke'. 
* Some commands are listed below:

```
!poke start <trainer_name>
-This command registers the user who made the request as a trainer.
-YOU MUST RUN THIS COMMAND IN ORDER TO START PLAYING.

!poke rename <trainer_name>
-This command renames the trainer who made the request to <trainer_name>.

!poke trainers
-This command returns a list of all trainers currently stored on the server.

!poke catch <pokemon>
-This command attempts to catch a pokemon.
-If the name matches a pokemon that is currently spawned in, the trainer will catch it.

!poke list
-This command shows the pokemon currently owned by the trainer who made the request.

!poke available
-This command shows all sprites of currently spawned pokemon.
```

---

## TODO LIST
* Pokebot.py
  * Implement renaming Pokemon functionality.
  * Implement leveling functionalities.

* Trainer.py
  * Implement releasing functionality.
  * Implement pokemon sorting algorithm.

* Pokemon.py
  * Implement pokedex data retrieval.

* PokeAPI.py
  * Implement moveset retrieval.
  * Implement total moveset retrieval.
  * Implement evolution calculations.
  * Implement shinies and more extensive sprite retrieval.

