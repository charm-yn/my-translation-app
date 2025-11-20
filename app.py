import streamlit as st
import google.generativeai as genai

# --- APIキーの設定 ---
# Streamlit Secrets から API キーを読み込む
GOOGLE_API_KEY = st.secrets="AIzaSyC4_fx7Im0WyefunWzjIeFx8wkD7_p5H8A"
genai.configure(api_key=GOOGLE_API_KEY)

model = "gemini-3-pro-preview"


# --- 言語オプション ---
LANG_OPTIONS = {
    "日本語 (Japanese)": "Japanese",
    "ミャンマー語 (Burmese / မြန်မာဘာသာ)": "Burmese",
}

# --- UI 部分 ---
st.title("ミャンマー語 ⇄ 日本語 翻訳アプリ")
st.write("上のボックスにミャンマー語または日本語を入力して、翻訳先の言語を選んでください。")

source_text = st.text_area("翻訳したいテキストを入力してください")

target_lang_label = st.selectbox(
    "翻訳先の言語",
    list(LANG_OPTIONS.keys())
)

# --- ボタンが押された後の処理 ---
if st.button("翻訳する") and source_text:
    target_lang = LANG_OPTIONS[target_lang_label]

    # Gemini へのプロンプト
    prompt = (
        f"Translate the following text into {target_lang}. "
        "Only output the translation, no explanations.\n\n"
        f"Text:\n{source_text}"
    )

    with st.spinner("翻訳中..."):
        # GenerativeModel は使わず、トップレベルの generate_text を使う
        response = genai.generate_text(
            model="gemini-pro",
            prompt=prompt,
        )
        translation = response.result  # ここに翻訳結果のテキストが入る

    st.subheader("翻訳結果")
    st.write(translation)
