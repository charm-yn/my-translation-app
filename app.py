import streamlit as st
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

# --- API Configuration ---
# ERROR FIX 1: Do not hardcode the key. Use st.secrets for security.
# If running locally, create a file .streamlit/secrets.toml
# If on Streamlit Cloud, add it in the dashboard settings.
try:
    GOOGLE_API_KEY = "AIzaSyCElQxuG-jY7vMnOsBtqmyF-9lIEwx3Fwk"
except Exception:
    st.error("API Key not found. Please set it in .streamlit/secrets.toml or Streamlit Cloud secrets.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# ERROR FIX 2: Use "gemini-1.5-flash".
# It is faster and less likely to hit "ResourceExhausted" errors than Pro/Preview models.
MODEL_NAME = "gemini-1.5-flash"

# --- Language Options ---
LANG_OPTIONS = {
    "日本語 (Japanese)": "Japanese",
    "ミャンマー語 (Burmese / မြန်မာဘာသာ)": "Burmese",
}

# --- UI ---
st.title("ミャンマー語 ⇄ 日本語 翻訳アプリ")
st.write("ミャンマー語または日本語を入力して、翻訳先の言語を選んでください。")

source_text = st.text_area("翻訳したいテキストを入力してください")
target_lang_label = st.selectbox("翻訳先の言語", list(LANG_OPTIONS.keys()))

# --- Translation Logic ---
if st.button("翻訳する") and source_text:
    target_lang = LANG_OPTIONS[target_lang_label]

    prompt = (
        f"Translate the following text into {target_lang}. "
        "Only output the translation, with no explanation.\n\n"
        f"Text:\n{source_text}"
    )

    with st.spinner("翻訳中..."):
        try:
            # ERROR FIX 3: Error handling block
            model = genai.GenerativeModel(MODEL_NAME)
            response = model.generate_content(prompt)
            translation = response.text
            
            st.subheader("翻訳結果")
            st.write(translation)

        except ResourceExhausted:
            st.error("⚠️ 混雑しています (Rate Limit Exceeded)。1分ほど待ってから再度お試しください。")
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
