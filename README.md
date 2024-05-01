# Fridge Contents Analyzer

## Description
This project allows its users to easily identify what dishes they can make while using the ingredients available to them. The user can simply upload a picture of the ingredients currently accessible to them, and then the program returns recipes for potential dishes that the user can make. The user will also have available to them a history of past pictures that they uploaded along with its corresponding recipes for future reference.

## Container Images
[MongoDB Container](https://hub.docker.com/_/mongo)

[App Container]()

## Configuration/Setup Instructions
To successfully setup the program, first clone the repository locally. Then in the "backend" folder, create a .env file. Here you will need to set the variable OPENAI_API_KEY. This should be set to a valid OpenAI key that has access to the gpt-4-turbo model.Then you can set the variable MONGO_URI, which should be set to the database connection string of the database that you are using. If not set, the default value for this is "mongodb://localhost:27017/". You can also set the variable MONGO_DB, which would specify which database you are using. The default value of this is "pictures". Then the program should be ready to be run. 

## Team Members
[Noah Zhou](https://github.com/nz792)

[Daniel Pang](https://github.com/danielpang35github)

[Niket Gautam](https://github.com/githubatit)

[Ellis Pinsky](https://github.com/ellispinsky)


