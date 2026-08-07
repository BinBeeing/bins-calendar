# Bin's Calendar 자동 업데이트

## 설정 방법

### 1단계 — Kingslanding Deploy Key 생성
1. Kingslanding 대시보드 → 프로젝트 설정
2. **Generate Deploy Key** 버튼 클릭
3. 생성된 키 복사해두기

### 2단계 — GitHub 저장소 만들기
1. [github.com](https://github.com) 로그인
2. 우측 상단 `+` → **New repository**
3. 이름: `bins-calendar`, **Private** 선택 후 생성
4. zip 파일 압축 풀어서 파일 전체 업로드

### 3단계 — Deploy Key를 GitHub Secret에 등록
1. GitHub 저장소 → **Settings** → **Secrets and variables** → **Actions**
2. **New repository secret** 클릭
3. Name: `KL_DEPLOY_KEY`
4. Value: 1단계에서 복사한 키 붙여넣기
5. **Add secret** 클릭

### 4단계 — 완료!
- 매일 **한국 자정**에 자동으로 🔴 오늘 날짜 업데이트
- GitHub → **Actions** 탭에서 실행 결과 확인
- 수동 실행: Actions → "Update Today's Date" → **Run workflow**

## 파일 구조
```
bins-calendar/
├── all_in_one.html                        # 달력 HTML
├── update_today.py                        # 날짜 업데이트 스크립트
├── README.md                              # 이 파일
└── .github/
    └── workflows/
        └── update_calendar.yml            # 자동 실행 설정
```
