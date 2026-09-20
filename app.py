import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="連隊回報清查系統")
st.title("ROTC 臺北大學教育中心")
st.header("準據暨授課通知回報清查系統")

DEFAULT_NAMES = [
    "周奕豪","林凱亮","王柏貫","朱楷文","何昀哲","吳宜儒","林青松","黃泓仁","鄭睬蓁","羅于倢",
    "王思鈞","蔡駿佳","馬德康","張軒昂","林佑愷","林傳逸","楊邵勛","鄭智文","彭康鎰","王鈺凱",
    "洪靖杰","步長潤","郭鎮寧","江冠逸","陳耀文","洪彥翔","周萬明","王聖捷","郭育丞","張博凱",
    "胡劭懷","林芯妤","陳佳君","洪筠芯","張惟恩","李吉峰","張人仁","古原嘉","朱俞安","柯冠佑",
    "黃定凱","鍾文璽","林育章","林雨呈","李子均","吳耀宗","許恩睿","辛巧伃","蘇靖雅"
]

st.sidebar.header("建制名單（115-1: R23-25）")
members_text = st.sidebar.text_area("建制人員名單（請適時修改）", value="\n".join(DEFAULT_NAMES), height=250)
everybody_names = [n.strip() for n in members_text.split("\n") if n.strip()]
num_everybody = len(everybody_names)

uploaded_file = st.file_uploader("請上傳『連回報表單.csv』", type=["csv"])

if uploaded_file is not None:
    df_form = pd.read_csv(uploaded_file)
    name_column = st.selectbox("請選擇姓名欄位：", df_form.columns, index=0)
    list_reported = df_form[name_column].dropna().astype(str).str.strip().tolist()

    reported = [n for n in everybody_names if n in list_reported]
    nonreported = [n for n in everybody_names if n not in list_reported]
    out_of_everybody = [n for n in list_reported if n not in everybody_names]

    st.subheader("📢 回報詞")
    report_text = (
        f"報告值星班長，全連應到人數 {num_everybody} 員，除\n"
        f"未回報 {len(nonreported)} 員、建制外 {len(out_of_everybody)} 員外\n"
        f"實到 {len(reported)} 員，完畢。"
    )
    st.code(report_text)

    officer_text = f"報告副主任，學生報備本周日行動準據，未回報人員共 {len(nonreported)} 員，分述如後：{'、'.join(nonreported)}"
    st.code(officer_text)

    st.subheader("❌ 未回報名單")
    st.write("、".join(nonreported))
#-------------------------文字說明------------------------
st.sidebar.markdown("""
1. **上傳 CSV 檔案**：將**回報表單**匯出的 `.csv` 檔拖曳至右側區塊。
2. **核對欄位**：確認選擇的欄位名稱為「姓名（勿錯字）」。
3. **複製回報詞**：系統自動生成回報詞後，可點選右上角圖示一鍵複製貼至群組。
4. **人員異動**：若有退訓或新進人員，可直接在上方框框修改名單。
5. **檔案名稱**：一定要是**連回報表單.csv**
""")
st.sidebar.divider()  # 加一條分隔線
with st.sidebar.expander("📖 系統使用說明"):
    st.markdown("""
    **【日常操作】**
    1. 匯出 Google 表單為 CSV 檔。
    2. 上傳至本系統即可自動清查。
    
    **【名單維護】**
    * 若人員有異動，直接在上方文字框修改，一人一行。
    * 修改後系統會自動更新建制總人數。
    """)
with st.sidebar.expander("📖 關於搭配表單"):
    st.markdown("""
    **【使用google表單進行回報】**
    1. 建立一個表單
    2. 第一題使用單一選擇題，將全連的姓名都設成一個選項
    3. 第二題也是單一選擇題「我已詳閱行動準據」
    4. 截止時間一到，將表單輸出成「csv」檔案，並上傳系統即可
    5. 檔案名稱一定要是：連回報表單.csv\n
    備考：初代系統是使用簡答題，讓他們輸入自己的名字，但是會有打錯字的風險，導致錯誤判讀（害該員要軍紀再教育）
    """)
with st.sidebar.expander("📖 聯繫創作者"):
    st.markdown("""
    大學儲備軍官訓練團24期　陳耀文\n
    **【電子郵件】**chaelong239@gmail.com
    """)
