import streamlit as st
from googletrans import Translator, LANGUAGES
import time

st.title("🌍 Multilanguage Translator")

translator = Translator()
language_list = list(LANGUAGES.values())

source_lang = st.selectbox("Select Source Language:", language_list, index=language_list.index("english"))
target_lang = st.selectbox("Select Target Language:", language_list, index=language_list.index("spanish"))
user_text = st.text_area("Enter text to translate:", "")

if st.button("Translate"):
    if user_text:
        try:
            source_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(source_lang)]
            target_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_lang)]

            # Retry mechanism
            for attempt in range(3):
                try:
                    translated_text = translator.translate(user_text, src=source_code, dest=target_code).text
                    st.success(f"**Translated Text:** {translated_text}")
                    break
                except Exception as e:
                    st.warning(f"Retrying... ({attempt+1}/3)")
                    time.sleep(2)  # Wait before retrying
            else:
                st.error("Translation failed. Try again later.")
        
        except Exception as e:
            st.error(f"Translation error: {e}")
    else:
        st.warning("Please enter text to translate.")
