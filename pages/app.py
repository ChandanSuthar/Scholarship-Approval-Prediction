import streamlit as st
# import pickle
import joblib
import numpy as np


# import the model
# pipe = pickle.load(open('pipe.pkl','rb'))
# df = pickle.load(open('df.pkl','rb'))

df = joblib.load('df2.lb')
rdf = joblib.load('rdf.lb', mmap_mode='r')


st.title("Scolarship Approval Predictor")

education = st.selectbox('education',df['Education Qualification'].unique())
gender = st.selectbox('gender',df['Gender'].unique())
community = st.selectbox('community',df['Community'].unique())
religion = st.selectbox('religion',df['Religion'].unique())
exservicemen = st.selectbox('exservice-men',df['Exservice-men'].unique())
disability = st.selectbox('Disability',df['Disability'].unique())
sports = st.selectbox('Sports',df['Sports'].unique())
annualpercentage = st.selectbox('Annual-Percentage',df['Annual-Percentage'].unique())
income = st.selectbox('ncome',df['Income'].unique())
india = st.selectbox('India',df['India'].unique())

if st.button('Predict Scolarship'):
    if education == 'Undergraduate':
        education = 1
    elif education == 'Postgraduate':
        education = 2
    else:
        education = 3
    
    if gender == 'Male':
        gender = 1
    else:
        gender = 2
   
    if exservicemen == 'Yes':
        exservicemen = 1
    else:
        exservicemen = 2

    if disability == 'Yes':
        disability = 1
    else:
        disability = 2

    if sports == 'Yes':
        sports = 1
    else:
        sports = 2
    
    if india == 'In':
        india = 1
    else:
        india = 2

    if annualpercentage == '90-100':
        annualpercentage = 1
    elif annualpercentage == '80-90':
        annualpercentage = 2
    elif annualpercentage == '70-80':
        annualpercentage = 3
    else:
        annualpercentage = 4
    
    if income == 'Upto 1.5L':
        income = 1
    elif income == '1.5L to 3L':
        income = 2
    elif income == '3L to 6L':
        income = 3
    else:
        income = 4

    if community == 'General':
        community = 1
    elif community == 'OBC':
        community = 2
    elif community == 'ST/SC':
        community = 3
    else:
        community = 4
    
    if religion == 'Hindu':
        religion = 1
    elif religion == 'Muslim':
        religion = 2
    elif religion == 'Chirstian':
        religion = 3
    else:
        religion = 4
    
    query = np.array([education, gender, community, religion, exservicemen, disability, sports,annualpercentage, income, india])

    query = query.reshape(1, -1)
    
    prediction = rdf.predict(query)

    value = int(prediction[0])

    if value == 0:
            result = 'Approved 😉'
    else:
            result = 'Rejected ☠️'

    st.write(f'The predicted scholarship outcome is: {result}')

