# USWS-Project of Simulating social platform with generative agents
authors: Annas & Alan

By Running the project you are generating with openai conversations on a daily basis between the generative agents based on the choosen topic, intructions of each agents, older conversations that were stored by chromadb and the high-level reflections also generated by openai based on the conversations.

**(You can look up for the output in the file named "results")**

Unternehmenssoftware Projekt 
-
- aus dem Modul Unternehmenssoftware  Prof. Dr. Axel Hochstein
- Thema 1: Simulation of social platform with generative agents



How to Run the project:
- 
1.  Make sure every neccessary packages are installed (python, openai, chromadb)
2.  To Use openai, register to openai and credit your acc with the mininum amount (5€) so you can use openai
3.  After that follow the documents of openai documentation or create an api key on your openai site
4.  create file in root named "api_key" and copy it into it
5.  configure path of line 9 from main.py so conversations getting stored in project
6.  configure also the path in chromdb.py
7.  you might need to read the documentary of chromadb, too.


Things you can change to experiment:
-
- changing topic in main.py on line 24
- changing rounds in main.py on line 25
- changing intructions of agents: prompt_templates > instructions (pick one agent and change the character description)
- adding more persons (in main.py on line 20 by adding a new name and new file in instructions regarding to the new name)
