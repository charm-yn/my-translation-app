import streamlit as st
import google.generativeai as genai

# --- APIキーの設定 ---
# Streamlit Secrets に保存したキーを読み込む
GOOGLE_API_KEY = "AIzaSyC4_fx7Im0WyefunWzjIeFx8wkD7_p5H8A"
genai.configure(api_key=GOOGLE_API_KEY)

# 使用するモデル
model = genai.GenerativeModel("gemini-1.5-flash")

# --- 言語オプション ---
LANG_OPTIONS = {
    "日本語 (Japanese)": "Japanese",
    "ミャンマー語 (Burmese / မြန်မာဘာသာ)": "Burmese",
}

# --- UI 部分 ---
st.title("みんなでつくるAI翻訳アプリ")

source_text = st.text_area("翻訳したいテキストを入力してください")

target_lang_label = st.selectbox(
    "翻訳先の言語",
    list(LANG_OPTIONS.keys())
)

submit_button = st.button("翻訳する")

# --- ボタンが押された後の処理 ---
if submit_button and source_text:
    target_lang = LANG_OPTIONS[target_lang_label]

    # Gemini への指示文（プロンプト）
    prompt = f"""
    Please translate the following text into {target_lang}.
    Only output the translation, no explanations.

    Text:
    {source_text}
    """

    with st.spinner("翻訳中..."):
        response = model.generate_content(prompt)
        translation = response.text

    st.subheader("翻訳結果")
    st.write(translation)
