# 🚇 부산 지하철 역별 이용객 수 지도 분석 앱

Streamlit과 Folium을 활용하여 부산 지하철 역별 이용객 수를 지도에 시각화하고 분석할 수 있는 웹 애플리케이션입니다. 

---

## 📌 주요 기능

1. **데이터 업로드 및 미리보기**: `busan_subway.csv` 파일 업로드 및 전체/필터링 데이터 표 확인
2. **호선별 필터링**: `multiselect`를 이용해 원하는 호선(1~4호선)만 선택하여 지도에 표시
3. **지능형 지도 시각화**:
   - 이용객 수의 제곱근($\sqrt{N}$)에 비례하는 원 크기(CircleMarker) 적용
   - 호선별 전용 색상 구분 (1호선: 주황, 2호선: 초록, 3호선: 갈색, 4호선: 파랑)
   - 마우스 호버 시 역명 표시 (Tooltip), 클릭 시 상세 이용객 수 표시 (Popup)
4. **상위 역 분석**: 현재 필터 조건에 따른 이용객 수 상위 5개 역 표 제공

---

## 📁 프로젝트 구조

```text
.
├── app.py              # Streamlit 메인 애플리케이션 코드
├── requirements.txt    # 의존성 라이브러리 목록
└── README.md           # 프로젝트 안내 문서
```

---

## 🛠️ 기술 스택 (Tech Stack)

- **Language**: Python 3.x
- **Web Framework**: Streamlit
- **Data Processing**: Pandas
- **Map Visualization**: Folium, Streamlit-Folium

---

## 🚀 실행 방법 (Local Execution)

### 1. 저장소 복제 (Clone)
```bash
git clone https://github.com/사용자이름/저장소이름.git
cd 저장소이름
```

### 2. 패키지 설치
```bash
pip install -r requirements.txt
```

### 3. Streamlit 앱 실행
```bash
streamlit run app.py
```

---

## 📊 CSV 데이터 형식 (`busan_subway.csv`)

업로드하는 CSV 파일은 아래와 같은 열(Column) 이름을 포함해야 합니다.

| 호선 | 역명 | 위도 | 경도 | 이용객수 |
| :--- | :--- | :--- | :--- | :--- |
| 1호선 | 서면 | 35.1577 | 129.0591 | 65432 |
| 2호선 | 해운대 | 35.1637 | 129.1636 | 32100 |
