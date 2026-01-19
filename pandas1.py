import pandas as pd
import numpy as np  


dict_data = {"a": 1,"b": 2,"c": 3}
series_data =pd.Series(dict_data)
print(series_data)
print(type(series_data))

list_data=["2026-1-19",3.14,"abc",100,True]
series_data=pd.Series(list_data)
print(series_data)
print(type(series_data))

dict_data={"c0":[1,2,3],"c1":[4,5,6],"c2":[7,8,9],"c3":[10,11,12],"c4":[13,14,15]}
df=pd.DataFrame(dict_data)
print(type(df))
print(df)

# pandas 데이터내용 확인 
# .columns: 컬럼명 확인 
# .head(): 데이터 상단의 5개행 출력
# .tail(): 데이터 하단의 5개행 출력()안에 숫자 넣을 수 있음
# .sahpe:(행,열) 크기 확인 
# .info(): 데이터에 대한 전반적인 정보 제공
# 행과열의 크기
# 컬럼명
# 컬러별 결측치
# 컬럼별 데이터 타입
# .type(): 데이터 타입 확인

# 파일 불러오기
# 형식     읽기            쓰기
# csv     read_csv        to_csv
# excel   read_excel      to_excel    
# json    read_json       to_json
# html    read_html       to_html
# ./ 내가 있는 기준으로 하위폴더 이동 ./data/tsdditanic=pd.read_csv(".")
# ../ 내가 있는 기준으로 상위폴더 이동  ../../../


titanic = pd.read_csv("Titanic-Dataset.csv")
print(titanic)
print(titanic.columns)
print(titanic.head())
print(titanic.tail(10))
print(titanic.shape)
print(titanic.info())

print(type(titanic))

#pandas 에서 특정 열을 선택
# 열 1개 선택=Series 객체 반환:
#데이터 프레임의 열 데이터 1개만 선택할 때 2가지 방식
# 1) 대괄호 []안에 열 이름을 따옴표로 함께 입력
# 2) 도트. 다음에 열 이름 입력
# 열 n개 선택=DataFrame 객체 반환
# 데이터 프레임의 열 데이터 n개를 선택할 때는 1방식
# 이중대괄호[[]]안에 열 이름을 따옴표로 함께 입력
# ***만약에 열 1개를 데이터프레임 객체로 추출하려면 [[]] 사용가능



names = titanic["Name"]
print(names.head())
names=titanic.Name
print(names.head())
print(type(names))
print(names.shape)

double_columns = titanic[["Sex","Age"]]
print(double_columns.head( ))

print(type(double_columns))
print(double_columns.shape)

# pandas 데이터 필터링

# 1. boolean 인텍싱 True값을 가진 행만 추출
# 2. .isin() 각각의 요소가 데이터ㅍ프렘임 또는 시리즈에 존재 하는지 파악한후 True/False로 반환
# 3. .isna() 결측 값은 Ture, 그 외는 False
# 4. .notna() 결측 값은 False, 그 외는 True

print(double_columns["Age"] >= 35)
above35=double_columns[double_columns["Age"] >= 35]
print(above35.head())  #True값만 추출
names= titanic["Name"]
print(titanic[["Name", "Age"]].head())
print(above35.head()) #True

#성별 남자만 추출

above_male=double_columns[double_columns["Sex"]=="male"]
print(above_male.head())

print(titanic.head())
class1 = titanic[titanic["Pclass"].isin([1])]


print(class1.head())

print(double_columns.head())

age2040=double_columns[double_columns["Age"].isin(np.arange(20,41 ))]
print(age2040.head())

print(double_columns.head(7))
clas_2=double_columns["Age"].isna()
print(clas_2.head(7))    #비어있는 cell True반환


clas_3=double_columns["Age"].notna()
print(clas_2.head(7))    #비어있는 cell False반환

#결측 값을 제거한 누락되지 않은 값을 확인
#행제거

print(double_columns.head(10))

age5=double_columns[double_columns["Age"].notna()]
print(age5.head(10) )

# 결측지 제거

# dropna(axls=0) ==.dropna()  : 결축 값들이 들어이는 행 전체 삭제
# dropna(axls=1) : 결측값이 들어 있는 열 전체 삭제

print(titanic.head())
print(titanic.dropna())

print(titanic.dropna(axis=1).head())

# pandas 이름과 인덱스로 특정 행광 열 선택

# .loc[] : 행이름과 열 이름 사용 DataFrame객체.loc[행이름, 열이름]
# .lloc[] : 행과  열 번호 사용 DataFrame객체.iloc[행번호, 열번호]

name35=titanic.loc[titanic["Age"] >=35, ["Name","Age"]]
print(name35.head())    


name35.iloc[[1,2,3],0] = "no name"
print(name35.head())


#판다스 데이터 통계

# .mean(): 평균갑
# .median(): 중앙값
# .describe(): 다양한 통계값 요약
#eman, std, min, max, 25%, 50%, 75% 등
# .agg(): 여러개의 열에 다양한 함수 적용
# 모든 열에 여러 함수를 매핑:group, 객체.agg([함수1, 함수2,함수3,...])
# 각 열마다 다른 함수를 매핑: group.객체.agg("열": [함수1, 함수2,...], "열2": [함수1, 함수2,...], ...)
# .groupby(): 그룹별 집계
# .value_counts(): 값의 개수 
print("--------평균 나이----")
print(titanic["Age"].mean())

print("------중앙값----")
print(titanic["Age"].median())

print("------다양한 통계 요약----")
print(titanic.describe())

print("------모든 열에 동일한 함수 적용----")
print(titanic[["Age","Fare"]].agg(["mean","std"]))

print("------나이와 요금의 평균및 표준편차----")
print(titanic[["Age","Fare"]].agg(["mean","std"]))

print("------열별 사용자 집계----")

agg_dict={
    "Age": ["mean","min","max"],
    "Fare": ["median","sum"]
}

print(titanic.agg(agg_dict))

print("------성별 기준으로 평균 나이 및 요금-----")
print(titanic.groupby("Sex") [["Age","Fare"]].mean())

print("-----객실 등급(Pclass)별 인원수-----")

print(titanic["Pclass"].value_counts())

print("-----성별 인원수-----")
print(titanic["Sex"].value_counts())

print("-----새로운 열 country 생성 USA-----")
titanic["Country"]="USA"
print(titanic)

print("-----기존의 열을 계산해서 새로운 열을 추가-----")
titanic["NewAge"]= titanic["Age"] +10
print(titanic)

#20세 미만이면 child, 아니면 adult
print("------20세 미만이면 child, 아니면 adult----")
titanic["Age_group"]= "Audlt"
titanic.loc[titanic["Age"] <20, "Age_group"]="Child"
print(titanic)

# 데이터 프레임의 가장 마지막 인덱스 확인 후 행 추가
new_index=len(titanic)
print(new_index)
print(titanic.head())

titanic.loc[new_index] =[992,1,1,"shin","female",53,0,0,"Pc123",50.0,"C123","S","USA",63,"Adult"]

new_data=pd.DataFrame({
    "Name":["Alice","Bob"],
    "Age": [25,30],
    "Sex": ["female","male"],
    "survived": [1,0]



})
titanic= pd.concat([titanic,new_data], ignore_index=True)
print(titanic.tail())

# titanic["Name"].str.startswith("Sa") #문자열이 데이터가 Sa시작하는 자료 추출
# titanic[titanic["Age"].astype(str),str.startswith("2")]
# titanic[titanic["Age"].astype(str),str.startswith("^82")]


# 파일 저장
titanic.to_csv("./sample1.csv", index=False)
titanic.to_excel("./sample1.xls", index=False)
print("파일 저장 완료")