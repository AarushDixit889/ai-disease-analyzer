import streamlit as st
from groq import Groq
import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(data):
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

# Create GROQ
chat=Groq(api_key="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")

st.set_page_config("AI Disease Analyzer")
st.title("👨🏻‍⚕️AI Disease Analyzer💀💊")

file=st.file_uploader("Image",label_visibility="hidden")

    
if st.button("Generate Analysis"):
    with st.spinner("Generating medicine"):
            semantics=query(file)
            output_format="""
            ## Report
            <GIVE A REPORT TO DESCRIBE DISEASE>
            ## Home Treatment
            <GIVE A FIRST AID HOME TREATMENT THAT CAN HEAL SOME OF THE PROBLEM ALSO CONSIDER USE ITEMS THAT IS PRESENTED AT EVERY HOME>
            ## Medicines to take
            <GIVE BUNCH OF MEDICINES TREATMENT TO THE PATIENT(COMMA SEPERATED)>
            ## Overall Analysis
            <GIVE A OVERALL ANALYSIS>
            ## Recommendation
             <GIVE RECOMMENDATIONS HERE>
             ## Where it caused?
             <Give comma seperated reasons from where this disease caused>
             **LEVEL OF DISEASE**-<LEVEL OF PROBLEM in LOW,MEDIUM,HIGH>
            """
            prompt=f" Generate medical report with issue description.Image Semantics is provided here - {semantics}.Use this output format - '{output_format}'.Note-If image is not clear then you can say 'Image is not clear but don't give any wrong treatment'.Don't use output format according to yourself.My persona is I am a normal person who don't know about medication"
            answer=chat.chat.completions.create(messages=[
                 {
                      "role":"user",
                      "content":prompt
                 }],
                 model="mixtral-8x7b-32768",
                 temperature=0
            ).choices[0].message.content
            st.write(answer)
if file:
    st.image(file,width=500)
