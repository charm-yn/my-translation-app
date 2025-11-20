import streamlit as st
import google.generativeai as genai

# --- API設定 ---
GOOGLE_API_KEY = "AIzaSyC4_fx7Im0WyefunWzjIeFx8wkD7_p5H8A"
genai.configure(api_key=GOOGLE_API_KEY)

# Gemini 3 model name
MODEL_NAME = "gemini-3-pro-preview"

# --- 言語オプション ---
LANG_OPTIONS = {
    "日本語 (Japanese)": "Japanese",
    "ミャンマー語 (Burmese / မြန်မာဘာသာ)": "Burmese",
}

# --- UI ---
st.title("ミャンマー語 ⇄ 日本語 翻訳アプリ")
st.write("ミャンマー語または日本語を入力して、翻訳先の言語を選んでください。")

source_text = st.text_area("翻訳したいテキストを入力してください")
target_lang_label = st.selectbox("翻訳先の言語", list(LANG_OPTIONS.keys()))

# --- 翻訳ボタン ---
if st.button("翻訳する") and source_text:
    target_lang = LANG_OPTIONS[target_lang_label]

    prompt = (
        f"Translate the following text into {target_lang}. "
        "Only output the translation with no explanation.\n\n"
        f"Text:\n{source_text}"
    )

    with st.spinner("翻訳中..."):
        response = genai.GenerativeModel(MODEL_NAME).generate_content(prompt)
        translation = response.text

    st.subheader("翻訳結果")
    st.write(translation)
