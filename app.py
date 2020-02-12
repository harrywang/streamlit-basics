import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Customer Churn Analysis')
# load dataset
df = pd.read_csv('customer-churn-example-simple.csv')
df['churn'] = df['churn'].apply(str)
data_load_state = st.text('Loading data...')
st.write(df)
data_load_state.text('Checkout the dataset:')

st.subheader('Churn Rate')

churn_count = df['churn'].value_counts()
st.text(f'Churn rate = {churn_count.values[1]/sum(churn_count):.2%}')
sns.barplot(churn_count.index, churn_count.values) # note: inbalanced data with much less True than False
st.pyplot()

st.subheader('Decision Tree Classifier')


# load models
import pickle

# load models
with open('cat_encoder.pickle', 'rb') as f:
    cat_encoder = pickle.load(f)
with open('scaler.pickle', 'rb') as f:
    scaler = pickle.load(f)
with open('final_model.pickle', 'rb') as f:
    final_model = pickle.load(f)

df[['state', 'international plan']] = cat_encoder.transform(df[['state', 'international plan']])
y = df['churn']
df.drop(['churn'], axis=1, inplace=True)
X = scaler.transform(df)


y_pred = final_model.predict(X)


from sklearn.metrics import confusion_matrix
clf_tree_conf_matrix = confusion_matrix(y, y_pred)

plt.figure(figsize = (10,7))
plt.title('Decision Tree');
sns.heatmap(clf_tree_conf_matrix, annot=True, fmt="d"); #fmt="d" string formatting
st.text('Confusion Matrix')
st.pyplot()

st.subheader('Making Prediction')
st.markdown('Note: change total customer calls to 4 or more to see the prediction result')

st.markdown("Please provide customer information:")

state = st.text_input("State", 'IN')
acct_length = int(st.number_input("Account Length", 0, 500, 165))
inter_plan = st.selectbox("International Plan", ["yes", "no"])
total_day_minutes = int(st.number_input("Total Daytime Minutes", 0, 1000, 100))
total_day_calls = int(st.number_input("Total Daytime Calls", 0, 1000, 30))
service_calls = int(st.number_input("Total Customer Service Calls", 0, 100, 1))

prediction_state = st.text('calculating...')
# when customer service call >=4, churn, holding other features same
x =pd.DataFrame([[state, acct_length, inter_plan, total_day_minutes, total_day_calls, service_calls]])
x
x.iloc[:, [0, 2]] = cat_encoder.transform(x.iloc[:, [0, 2]])
x=scaler.transform(x)
y_pred = final_model.predict(x)
#y_pred
if y_pred == 'True':
    msg = 'This customer is a churn customer.'
else:
    msg = 'This customer is a loyal customer.'

prediction_state.text(msg)
