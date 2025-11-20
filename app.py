import streamlit as st
import google.generativeai as genai

# APIキーの設定
# TOMLのセクション名でアクセス
GOOGLE_API_KEY = st.secrets["GOOGLE"]["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY) 
model = genai.GenerativeModel("gemini-flash-latest")

# --- UI部分 ---
st.title("みんなでつくるAI翻訳アプリ") # タイトル

source_text = st.text_area("翻訳したいテキストを入力してください") # テキスト入力欄
target_lang = st.selectbox("翻訳先の言語", []) # セレクトボックス
submit_button = st.button("〇〇〇") # ボタン

# --- ボタンが押された後の処理 ---
if submit_button and source_text:
    # Geminiへの命令文を作成
    
    # APIを呼び出し
    
    # 結果を表示
    st.subheader("翻訳結果")
