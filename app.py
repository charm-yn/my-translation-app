import streamlit as st
from google import genai  # new google-genai library

# --- API設定 ---
# Streamlit Secrets から API キーを読み込む
API_KEY = "AIzaSyC4_fx7Im0WyefunWzjIeFx8wkD7_p5H8A"

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-1.5-flash"  # or change later if you want Flash

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

# --- 翻訳処理 ---
if st.button("翻訳する") and source_text:
    target_lang = LANG_OPTIONS[target_lang_label]

    prompt = (
        f"Translate the following text into {target_lang}. "
        "Only output the translation, with no explanation.\n\n"
        f"Text:\n{source_text}"
    )

    with st.spinner("翻訳中..."):
        # google-genai のシンプルな呼び方（types は使わない）
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )
        translation = response.text

    st.subheader("翻訳結果")
    st.write(translation)
