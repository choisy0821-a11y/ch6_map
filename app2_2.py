import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import math

# 1. 앱 제목 설정
st.title("🚇 부산 지하철 역별 이용객 수 지도 분석")
st.write("CSV 파일을 업로드하여 호선별 필터링 및 이용객 수 시각화를 확인해보세요!")

# 2. 호선별 마커 색상 정의 (1호선: 주황, 2호선: 초록, 3호선: 갈색, 4호선: 파랑)
line_colors = {
    '1호선': '#FF7F00',  # 주황색
    '2호선': '#00B050',  # 초록색
    '3호선': '#A55200',  # 갈색
    '4호선': '#0070C0'  # 파랑색
}

# 3. 파일 업로드 기능 (CSV)
uploaded_file = st.file_uploader("busan_subway.csv 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # CSV 파일 읽기
    df = pd.read_csv(uploaded_file)

    # ① 호선 필터 (multiselect)
    all_lines = sorted(df['호선'].unique())
    selected_lines = st.multiselect("보려하는 호선을 선택하세요", options=all_lines, default=all_lines)

    # 선택한 호선에 해당하는 데이터만 필터링
    filtered_df = df[df['호선'].isin(selected_lines)]

    # ② 데이터 미리보기 (표)
    st.subheader("📊 데이터 미리보기")
    st.dataframe(filtered_df)

    # ③ 이용객 상위 5개 역 표 표시
    st.subheader("🏆 이용객 상위 5개 역")
    top5_df = filtered_df.sort_values(by='이용객수', ascending=False).head(5)
    st.dataframe(top5_df[['호선', '역명', '이용객수']])

    # ④ 지도 생성 (부산 중심 좌표: 위도 35.179558, 경도 129.075641)
    st.subheader("🗺️ 역별 이용객 수 지도")
    m = folium.Map(location=[35.179558, 129.075641], zoom_start=11)

    # 필터링된 데이터프레임의 행을 하나씩 돌며 지도에 원 마커 추가
    for index, row in filtered_df.iterrows():
        # 이용객 수에 비례하도록 제곱근(math.sqrt)을 사용하여 반지름 계산
        radius_size = math.sqrt(row['이용객수']) * 0.05

        # 호선에 맞는 색상 가져오기 (지정되지 않은 호선은 기본 검은색)
        line_color = line_colors.get(row['호선'], '#000000')

        # Folium CircleMarker 추가
        folium.CircleMarker(
            location=[row['위도'], row['경도']],  # 마커 위치 (위도, 경도)
            radius=radius_size,  # 원 반지름 (이용객 수 기반)
            tooltip=f"[{row['호선']}] {row['역명']}",  # 마우스 올렸을 때: 호선 및 역명
            popup=f"{row['역명']} ({row['호선']}): {row['이용객수']:,}명",  # 클릭했을 때: 상세 정보
            color=line_color,  # 테두리 색상 (호선별 지정 색상)
            fill=True,  # 원 안쪽 채우기
            fill_color=line_color,  # 채우기 색상
            fill_opacity=0.6  # 불투명도 (0~1)
        ).add_to(m)

    # Streamlit 화면에 Folium 지도 출력
    st_folium(m, width=700, height=500)

else:
    st.info("💡 위에서 `busan_subway.csv` 파일을 업로드하면 지도가 나타납니다.")