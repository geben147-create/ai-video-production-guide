# 새 세션 인계

## 복사해서 새 세션에 입력
이 패키지 SKILL.md와 project 자료를 읽고 로마 100컷 제작을 이어가라. 로컬 작업 폴더의 AGENTS.md를 우선 읽고 실제 파일/작업 ID를 대조하라. 현재 기록은 완료47/100, 남은53, 제출중0. 다음은048. MiniMax H3 전환은 사용자가 승인했지만 마지막 견적은12크레딧 할인 모드여서 제출하지 않았다. Wan 마지막 견적도15크레딧이었다. 매 요청 직전 동일 견적 두 번이 비용0/discountCredit0/unlimited일 때만 최대4개 제출하라. 유료·크레딧 사용·사진 모션 대체는 금지다. 이전 자동화는 인계를 위해 PAUSED다. 무료 상태를 확인한 뒤 새 세션 하나가 제출 소유권을 가져라.

## 로컬 재개 자료
원래 프로젝트 폴더: Documents/Codex/2026-09-09/dynamic-spectacle-video-director-skill-v1 (현재 OS 사용자 홈 아래).
outputs/images 원본100장, outputs/videos 결과, outputs/video_jobs 작업별 증거, outputs/video_plan.json 대본, outputs/scenes.json 이미지 프롬프트, work/requests_*.json 준비된 영상 요청, work/rome_video_workflow.py 저장·refresh 도구.
실제 영상은 001~047 저장 기록. 048~100 미제출. ffprobe/decode는 완료 판정에 사용했으나 영화적 품질·속도·연속성 전체 검수 및 최종 편집은 미완료.
002/003은 인물·침대 회피를 위해001 소스 재사용. 기존 초기 대사와 얼굴 없는 도입 화면의 일치 검토가 남아 있다. 예전 hybrid/70+30 배분, 눈뜨기 컷, 사진 모션 완료 카운트는 폐기됐다.

## 준비 상태의 정직한 범위
048~058 요청 파일이 존재. 059~062 업로드 기록은 대화에 있으나 요청 파일 지속성 확인 필요. 063~070 요청 JSON은 scene_id/image/prompt의 간단한 형식이며 제출용 input으로 감싸고 소스 시각 검수 필요. 071~082는 업로드 진행 기록만 있고 일부 confirm/URL 영구 저장/프롬프트가 누락됐다. 필요하면 원본에서 재업로드하라. 083~100은 준비 확인 필요. 준비됐다는 이전 보고를 제출 가능 완료로 해석하지 말 것.

## 비용 차단
2026-09-09 마지막 관측: Wan discountCost15/discountCredit15/unlimited, H3 discountCost12/discountCredit12/discount. 모두 제출 불가. 과거 권리 종료일/Ultra 플랜만으로 무료를 선언하지 않는다. 계정 인증과 실시간 견적은 새 세션에서 필요하다.
기존 render_mode_policy required_model은 Wan이며 최신 사용자는 H3를 승인했다. 정책과 자동화에서 Wan 고정을 H3 승인으로 갱신하되 zero-cost 게이트는 유지한다.

## 재개 순서
1 실제 로컬 파일 수와 job 상태를 대조; 공개 snapshot을 실시간 진실로 쓰지 않는다.
2 소스와 프롬프트를 읽고048~051을 준비; 모델 스키마 조회.
3 비용0 두 번 검증; 아니면 blocked_cost를 기록하고 유료 요청 금지.
4 제출 성공 ID를 즉시 원본 응답과 기록; 빈 슬롯만 채운다.
5 Assets 실제 결과 저장·decode·마지막 프레임 검증, 그 후 다음 컷.
6 진행·metrics 단일 표 갱신; 토큰 미제공, 무료 재개시간 불명 시 ETA 불명.
7 최종은 영상 내용/얼굴/광원/관성 검수와 나레이션 길이 conform까지 수행.
