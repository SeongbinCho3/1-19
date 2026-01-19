import pandas as pd
import numpy as np

# 0. 데이터 불러오기 (한글 깨짐 방지를 위해 UTF-8 인코딩 사용)
# 만약 여전히 에러가 난다면 encoding='cp949'로 바꿔보세요.
df = pd.read_csv('raw_trade_data.csv', encoding='utf-8')

# ---------------------------------------------------------
# [과제 1] 특정 품목의 수출입 현황 보고서 준비하기
# ---------------------------------------------------------

# 1. HS코드 앞 2자리가 '85'인 데이터 추출
# 숫자로 되어있는 hs_code를 문자열로 변환하여 앞 2자리를 체크합니다.
df['hs_code_str'] = df['hs_code'].astype(str)
semi_df = df[df['hs_code_str'].str.startswith('85')].copy()

# 2. 국가명이 '미국' 혹은 '베트남'인 데이터만 필터링 (.isin() 활용)
semi_df = semi_df[semi_df['국가명'].isin(['미국', '베트남'])]

# 3. 수출금액이 0인 데이터 분석에서 제외 (0보다 큰 데이터만 추출)
semi_df = semi_df[semi_df['수출금액'] > 0]

# 4. 결과 출력 및 저장 (상위 10개)
print("--- [과제 1] 반도체 보고서 상위 10개 ---")
print(semi_df.head(10))

# csv 저장 (한글 깨짐 방지를 위해 utf-8-sig 사용)
semi_df.head(10).to_csv('semiconductor_report.csv', index=False, encoding='utf-8-sig')


# ---------------------------------------------------------
# [과제 2] 지저분한 무역 데이터 바로잡기 (클렌징)
# ---------------------------------------------------------

# 1. '중량' 컬럼 결측치 처리
# 각 품목(hs_code)별 평균 중량으로 채우고, 그래도 남은 곳은 0으로 채웁니다.
df['중량'] = df.groupby('hs_code')['중량'].transform(lambda x: x.fillna(x.mean()))
df['중량'] = df['중량'].fillna(0)

# 2. '수출입구분' 컬럼 영문 -> 국문 일괄 변경
df['수출입구분'] = df['수출입구분'].replace({'Import': '수입', 'Export': '수출'})

# 3. '수출금액_M_USD' 컬럼 생성 (단위: 백만 달러, 환율: 1,470원)
# 계산식: (원화 금액 / 1470) / 1,000,000
df['수출금액_M_USD'] = df['수출금액'] / 1470 / 1000000

# 4. 데이터 타입 확인 및 최종 결과 출력
print("\n--- [과제 2] 데이터 타입 확인 ---")
print(df.dtypes)

print("\n--- [과제 2] 정제된 데이터 상위 5개 ---")
print(df.head())

# 최종 정제 데이터 저장
df.to_csv('cleaned_trade_data.csv', index=False, encoding='utf-8-sig')