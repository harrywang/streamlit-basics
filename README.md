# Streamlit Basics

This repo demonstrates how to showcase your data science project as a web application using [Streamlit](https://www.streamlit.io/) both locally and remotely (AWS and Heroku).

Tested with Python 3.8

## Files

- `requirements.txt` and `requirements-dev.txt`: package requirements files
- `titanic_train.csv` and `tree-clf.pickle`: data file and pre-trained decision tree model
- `app.ipynb`: notebook for the analysis
- `app.py`: streamlit app file
- `Dockerfile` for docker deployment
- `Procfile` and `setup.sh`: heroku deployment files - they must be in the root folder
- `aws` folder: files used for AWS Fargate deployment using AWS CDK	

## Streamlit Data and Model

The data used in this repo is the [Titanic dataset from Kaggle](https://www.kaggle.com/c/titanic). The simple decision tree model is pre-trained using scikit-learn and is provided in `tree-clf.pickle` file. The related analysis code is the `app.ipynb` notebook. The code to load and visualize the data, make predictions, and present results using Streamlit is in `st-demo/app.py`

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

## AWS Deployment

Install AWS CLI: `pip install awscli`

Setup your aws credentials, 
```
$ aws configure
AWS Access Key ID [****************UP34]: AKIA6NPxxxxx
AWS Secret Access Key [****************3UE7]: JS38jueHmIt0xxxxx
Default region name [us-east-1]: 
Default output format [json]: 
```

Install AWS CDK: `npm install -g aws-cdk`

NOTE: Initially, you use the following commands to setup cdk app folder `aws`, which will create a python virtual environment in `.venv` automatically - you don't need to do this given we have `aws` folder already setup:
```
$ mkdir aws
$ cd aws
$ cdk init --language python
```

go to `aws` folder 
```
$ cd aws
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ pip install aws_cdk.aws_ec2 aws_cdk.aws_ecs aws_cdk.aws_ecs_patterns
```
stack information is specified in `aws/cdk/cdk_stack.py`:

```
$ cdk synth
```

Deploy the app using AWS Fargate while in `aws` folder:

`cdk.*` must be added to `st-demo/.dockerignore` file to avoid [this issue](https://github.com/aws/aws-cdk/issues/3899#issuecomment-580394612)

```
$ cdk bootstrap
$ cdk deploy
...
Outputs:
streamlit-demo.StreamlitDemoServiceLoadBalancerDNS7xxxD089 = strea-Strea-133IC47CGL4EZ-7748xxx3.us-east-1.elb.amazonaws.com
streamlit-demo.StreamlitDemoServiceServiceURLxxx9E60 = http://strea-Strea-133IC47CGL4EZ-774xxx3.us-east-1.elb.amazonaws.com
...
```

REMEMBER to delete your stack to stop any unexpected expenses!!

```
$ cdk destroy
```

## References

- Heroku part is based on this [tutorial](https://towardsdatascience.com/-quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83).
- AWS part is adapted based on this [tutorial](https://github.com/nicolasmetallo/legendary-streamlit-demo).