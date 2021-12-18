# Streamlit Basics

This repo demonstrates how to showcase your data science/machine learning project as a web application using [Streamlit](https://www.streamlit.io/) and how to host your app on Heroku for free.

Tested with Python 3.9

## Files

- `requirements.txt` and `requirements-dev.txt`: package requirements files
- `titanic.csv` and `clf-best.pickle`: data file and pre-trained decision tree model
- `app.ipynb`: notebook for generating the decision tree model
- `app.py`: streamlit app file
- `Dockerfile` for docker deployment
- `Procfile` and `setup.sh`: heroku deployment files - they must be in the root folder

## Streamlit Data and Model

The data used in this repo is the [Titanic dataset from Kaggle](https://www.kaggle.com/c/titanic). The simple decision tree model is pre-trained using scikit-learn and is provided in `clf-best.pickle` file (the related code is in the `app.ipynb` notebook). The code to load and visualize the data, make predictions, and present results using Streamlit is in `app.py`

## Run Demo Locally 

### Shell

you can directly run streamlit locally in the repo root folder as follows:

```shell
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements-dev.txt
$ streamlit run app.py
```
Open http://localhost:8501 to view the demo

### Docker

build and run the docker image named `st-demo`:

```
$ docker build -t st-demo .
$ docker run -it --rm -p '8501:8501' st-demo
```
`-it` keeps the terminal interactive
`--rm` removes the image once the command is stopped (e.g. using control + c)

go to http://localhost:8501/ to view the app.


## Streamlit Cloud Deployment
 
1. Put your app on GitHub (like this repo)
Make sure it's in a public folder and that you have a requirements.txt file.
 
2. Sign into Streamlit Cloud
Sign into share.streamlit.io with your GitHub email address, you need to have access to Streamlit Cloud service.
 
3. Deploy and share! 
Click "New app", then fill in your repo, branch, and file path, choose a Python version (3.9 for this demo) and click "Deploy", then you should be able to see your app.

https://share.streamlit.io/harrywang/streamlit-basics/app.py

<img width="838" alt="Screen Shot 2021-12-18 at 2 49 54 PM" src="https://user-images.githubusercontent.com/595772/146653960-664146b7-afcc-4b5d-b0aa-763bd5788482.png">

## Heroku Deployment

- Create a Heroku account: https://www.heroku.com/
- Install Heroku [Command Line Interface (CLI)](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
- Login to Heroku: in this repo root folder (don't go into the heroku sub-folder), and run `heroku login`
- Create an instance: `heroku create st-demo-harrywang` you should use a unique name for the app. a new git remote named `heroku` has been created, check with `git remote -v`
- Create a `setup.sh` file (done for you): this file creates the following two files
`~/.streamlit/credentials.toml` and `~/.streamlit/config.toml` on the server to:
    - set a basic credential with an email (any email should work)
    - set headless = true, enableCORS=false, and port = $PORT
- Create a `Procfile` (done for you): Heroku apps include a Procfile that specifies the commands that are executed by the app on startup. 
- Push the code of this repo to the new instance: `git push heroku master`
- Run `heroku ps:scale web=1` to `web=1` ensures that one instance (dynos) is running:
```
$ heroku ps:scale web=1
Scaling dynos... done, now running web at 1:Free
```
- Run `heroku open` to open the application at https://st-demo-harrywang.herokuapp.com/

## References

- Heroku part is based on this [tutorial](https://towardsdatascience.com/-quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83).
- For AWS deployment, checkout [tutorial](https://github.com/nicolasmetallo/legendary-streamlit-demo).