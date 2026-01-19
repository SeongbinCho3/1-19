import streamlit as st
import pandas as pd

# 웹 페이지 제목
st.title("🚢 무역 데이터 분석 및 클렌징 도구")

# 1. 파일 업로드 기능
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=['csv'])

if uploaded_file is not None:
    # 데이터 불러오기
    df = pd.read_csv(uploaded_file, encoding='utf-8')
    
    st.subheader("✅ 원본 데이터 확인")
    st.dataframe(df.head())

    # --- [과제 1 로직] ---
    st.divider()
    st.header("1. 반도체(HS 85) 분석 보고서")
    
    df['hs_code_str'] = df['hs_code'].astype(str)
    # 사용자가 직접 국가를 선택하게 만들 수도 있어요!
    countries = st.multiselect("분석할 국가를 선택하세요", ["미국", "베트남", "중국", "일본"], default=["미국", "베트남"])
    
    semi_df = df[
        (df['hs_code_str'].str.startswith('85')) & 
        (df['국가명'].isin(countries)) & 
        (df['수출금액'] > 0)
    ].copy()
    
    st.write(f"선택된 데이터 개수: {len(semi_df)}건")
    st.dataframe(semi_df.head(10))

    # --- [과제 2 로직] ---
    st.divider()
    st.header("2. 데이터 클렌징 및 단위 변환")
    
    # 정제 작업 수행
    df['중량'] = df.groupby('hs_code')['중량'].transform(lambda x: x.fillna(x.mean())).fillna(0)
    df['수출입구분'] = df['수출입구분'].replace({'Import': '수입', 'Export': '수출'})
    
    exchange_rate = st.number_input("현재 환율을 입력하세요 (원/$)", value=1470)
    df['수출금액_M_USD'] = df['수출금액'] / exchange_rate / 1000000
    
    st.success("데이터 정제가 완료되었습니다!")
    st.dataframe(df.head())
    
    # 3. 결과 다운로드 버튼
    csv = df.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
    st.download_button(
        label="정제된 데이터 다운로드 (CSV)",
        data=csv,
        file_name='cleaned_trade_data.csv',
        mime='text/csv',
    )