# Streamlit Demo using Churn Analysis

## Setup

```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ streamlit run app.py
```

## Heroku Deployment

This part is based on this [tutorial](https://towardsdatascience.com/quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83).

- Create Heroku account
- Install Heroku [Command Line Interface (CLI)](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
- Login to Heroku: in this repo folder, and run `heroku login`
- Create an instance: `heroku create st-churn-demo`
- Create a `setup.sh` file: this file creates the following two files
`~/.streamlit/credentials.toml` and `~/.streamlit/config.tomlon the server` to:
    - set a basic credential with an email (any email should work)
    - set headless = true, enableCORS=false, and port = $PORT

    Refer to https://discuss.streamlit.io/t/how-to-use-streamlit-in-docker/1067
- Create a `Procfile`: Heroku apps include a Procfile that specifies the commands that are executed by the app on startup.
- Push the code of this repo to the new instance: `git push heroku master`
- Run `heroku ps:scale web=1` to ensure that at least one instance of the app is running
- Open the application in browser with `heroku open`
