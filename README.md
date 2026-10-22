# AI-Powered Student Academic Assistant

A Streamlit web version of the Python mini project.

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   streamlit run app.py
   ```

Streamlit will print a local URL (usually http://localhost:8501).

## Publish it online with Streamlit Community Cloud

1. Create a GitHub account if you do not have one.
2. Create a new **public** GitHub repository, for example `student-academic-assistant`.
3. Upload `app.py` and `requirements.txt` from this folder to the repository root.
4. Open https://share.streamlit.io/ and sign in with GitHub.
5. Choose **Create app**, select your repository, branch (usually `main`), and main file path `app.py`.
6. Click **Deploy**. When the build finishes, Streamlit provides a public URL you can share.

## Notes

- This project uses a rule-based FAQ chatbot with predefined answers; it does not call an external AI model.
- Do not publish private credentials or personal information in a public repository.
