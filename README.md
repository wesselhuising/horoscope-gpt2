# The (Dutch) Horoscope Generator
This is the official repository for the tool hosted at https://horoscope.wesselhuising.nl.
The tool uses a GPT-2 model pre-trained on Dutch text and fine-tuned on 10.000 scraped Dutch horoscopes to generate new horoscopes based on a small amount of input.

The app consists of two Docker containers. One for running the actual webapp built in Flask and one API for serving the GPT-2 Horoscope model built with FastAPI. 

## Article
To find more information on how this concept came to life, please read the full article.

https://wesselhuising.medium.com/creating-a-horoscope-generator-in-dutch-using-deep-learning-45d6ff11f269

## Contents

    │
    ├── api
    ├──── Dockerfile 
    ├──── app
    ├────── main.py                 <- the fastapi application code
    ├────── model.py                <- the model wrapper class used for serving the GPT-2 model
    ├────── model
    ├──────── config.json           <- pytorch config for the model
    ├──────── pytorch_model.bin     <- the actual model including the weights 
    ├── flask
    ├──── Dockerfile
    ├──── app
    ├────── app.py                  <- the flask application code
    ├────── static 
    ├──────── style.css             <- the stylesheet
    ├──────── images                <- images directory
    ├────── templates
    ├────────  index.html           <- the landingpage
    ├────────  generate.html        <- the resultpage
    ├── docker-compose.yml          <- where the magic happens

For compiling the horoscope generator run the following command in the root folder: `docker-compose up`.