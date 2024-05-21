import json, streamlit as st
import request


with open('settings.json') as f:
    settings = json.load(f)

api_key = settings.get('OPENAI_API_KEY')
assert api_key is not None, "OpenAI API key not found."

def display_log(log_data):
    st.text_area("Resumo", log_data, height=200)

request.set_api_key(api_key)

def main():
    st.title("Resumir Texto")
    log_text = st.text_area("Texto", height=300)

    if st.button("Enviar"):
        response = request.send_summary(log_text)
        
        display_log(response)

if __name__ == "__main__":
    main()