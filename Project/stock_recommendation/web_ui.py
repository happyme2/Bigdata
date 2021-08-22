from recommendation import recommendation
from pandas import DataFrame
import streamlit as st

st.title("주식 종목 추천시스템")
input_text = st.text_input("ID를 입력해주세요.")  #str

source = st.selectbox("추천 받으실 종목의 갯수를 선택해주세요.",("3개","5개","10개")) #str
check_url = st.checkbox('네이버 금융 사이트와 함께 보기')
btn_ok = st.button("추천받기")

if btn_ok : #추천받기 버튼을 누르면
    st.markdown(f"입력하신 id는 [{input_text}]로, 등락률 상위{source} 종목을 추천드리겠습니다. ")
    st.markdown("추천 완료까지 약 1분 정도 소요됩니다.")
    
    if source == '3개':
        num=3
    elif source == '5개':
        num=5
    elif source =='10개':
        num=10
    
    result = recommendation(input_text,num) #(str,int)
    result_show = result.style.format({'시작일 기준가':'{0:,}원','종료일 종가':'{0:,}원','대비':'{0:,}원','등락률':'{:,.2f}%','거래량':'{0:,}주','거래대금':'{0:,}원'})
    st.table(result_show)

    if check_url :
        code_list = result['종목코드'].values.tolist()
        #name_list = result['종목명'].values.tolist()
        st.markdown("자세한 종목 확인은 아래 링크를 통해 확인하실 수 있습니다.")

        for code in code_list:
            url = "https://finance.naver.com/item/main.nhn?code={}".format(code)
            st.write(f"종목코드 : {code}[네이버 금융 link](url)")