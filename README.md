# 📧 Cold Mail Generator

**Cold Mail Generator** is a smart outreach tool for service-based companies, enabling teams to generate personalized cold emails for companies actively hiring. With the help of **GROQ**, **LangChain**, and **Streamlit**, the app identifies job opportunities directly from career pages like **Google Careers**, and crafts context-rich cold emails backed by portfolio evidence.

---

## 🧠 Use Case

Let’s say **Google** is hiring a *Software Engineer* and has a live job listing here:


Instead of cold guessing, a business development rep from a software services firm like **Atliq** can:

1. Paste this link into the app.
2. Let the tool fetch job details and understand the role.
3. Automatically generate a cold email tailored to Google’s exact need, with relevant portfolio projects linked inside.

**The result?**

Sharper outreach, stronger alignment, and better conversion.

---

## 🏗️ How It Works

1. **Paste a Careers Page URL**  
   Example: Google’s job listing for a software engineer.

2. **Job Description Extraction**  
   The app scrapes or parses the page and retrieves the full job description (title, responsibilities, qualifications).

3. **Portfolio Matching via Embeddings**  
   It compares the job description to your portfolio data (stored in a vector DB) to identify matching case studies or projects.

4. **Cold Email Generation**  
   A well-crafted, personalized cold email is generated using large language models via GROQ and LangChain.


---

## Set-up
1. To get started we first need to get an API_KEY from here: https://console.groq.com/keys. Inside `app/.env` update the value of `GROQ_API_KEY` with the API_KEY you created. 


2. To get started, first install the dependencies using:
    ```commandline
     pip install -r requirements.txt
    ```
   
3. Run the streamlit app:
   ```commandline
   streamlit run app/main.py
   ```
