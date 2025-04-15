import streamlit as st
from chains import Chain
from portfolio import Portfolio
from utils import clean_text
from langchain_community.document_loaders import WebBaseLoader

st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")

st.title("Cold Email Generator")

url_input = st.text_input(
    "Enter a URL:",
    value="https://www.google.com/about/careers/applications/jobs/results#!t=jo&jid=127025001&"
)

submit_button = st.button("Submit")

if submit_button:
    try:
        loader = WebBaseLoader([url_input])
        data = clean_text(loader.load().pop().page_content)

        chain = Chain()
        portfolio = Portfolio()
        portfolio.load_portfolio()

        jobs = chain.extract_jobs(data)
        for job in jobs:
            skills = job.get('skills', [])
            links = portfolio.query_links(skills)
            email = chain.write_mail(job, links)
            st.code(email, language='markdown')

    except Exception as e:
        st.error(f"An Error Occurred: {e}")
