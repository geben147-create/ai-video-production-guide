# 영상 프롬프트 설계

## 이미지와 모션 분리
이미지는 시작 상태, 영상은 시간에 따른 변화다. source_image, image_prompt, video_prompt, 실제 provider_input을 각각 보존한다. source를 보지 않고 공간을 추측하지 않는다. 원본 이미지 바깥 새 공간의 공개는 생성적 재구성이며 실측된 공간 연속성으로 주장하지 않는다.

## 설명하는 이동
Cause → movement → discovery → reaction → consequence → next cause. 카메라가 왜 이동하는지 한 문장으로 설명한다. 배→화물→상인→동전→시장처럼 인과 관계를 이동 목표로 쓴다. 아치 가림 뒤에는 새로운 정보가 나와야 한다.

## 초고속 모드(선택적 프로젝트 설정)
로마 프로젝트 최신 override는 첫 프레임부터 고속. 0.5~1.2초마다 전경 통과/규모/고도/목표 변화를, 1.5~2.5초마다 큰 공개를 목표로 한다. 이는 제작 목표이지 생성 결과 측정값이 아니다.
0.0~0.4 이전 관성 유지 → 0.4~1.2 근접 통과 → 1.2~2.0 공개 → 2.0~3.0 bank/drop/climb → 3.0~4.0 규모 변화 → 4.0~4.6 가림 → 4.6~5.0 다음 운동 전달.
모든 5초 클립에 불가능한 다중 공간을 강요하지 않는다. 구조 붕괴 시 하나의 주 이동과 한두 번의 방향 변화로 줄이고 편집 컷으로 나눈다. 속도감은 가까운 전경의 상대 운동으로 만든다. 회전·급상승·극근접을 기계적으로 반복하지 않는다.

## 템플릿
`[scene ID, 시대/장소]. [시작 구도와 고정된 공간]. Camera already moving rapidly from frame one. [시간/첫 이동 + 가까운 전경 통과]. [공개할 정보]. [이동 원인 + 새 목표로 bank/dive/climb]. [인물/사물 행동]. [가림 또는 마지막 앵커 + 종료 방향]. [고정 기하·광원·얼굴 제한].`
Negative 의미: no slow start, no hover, no gradual acceleration, no frozen end, no random morphing, no changing architecture, no HUD, no talking face. 모델에 negative 필드가 없으면 prompt에 필요한 의미만 넣는다.

## 실제 연속성
velocity_out/in, direction, camera_height, bank_angle, horizon, target_position, foreground_motion, light_direction을 기록한다. 이전 영상의 실제 마지막 디코드 프레임과 해시를 다음 입력으로 사용한다. 계획상의 마지막 이미지로 바꾸지 않는다. 새 클립 초반 0.3~0.5초의 관성을 검수한다. 마지막 프레임 입력만으로 연결 성공으로 판정하지 않는다.
독립 소스 클립은 `editorial_motion_match`로 표시한다. 장면 간 시공간 변경을 가짜 단일 비행으로 주장하지 않는다. 문이 닫힌 상태라면 다음 컷에서 갑자기 열린 상태로 이어지지 않게 한다.

## 사운드와 편집
ambience/action/transition/music/silence를 별도 설계한다. 무음 생성에도 편집용 sound cue는 보존한다. 0.2초 정적→충격은 효과가 필요한 구간만 사용한다. 나레이션의 실제 길이에 맞춰 conform한다. 5초 생성 100개가 510초 대본과 자동 일치하지 않는다.

## 검수 점수
Spectacle: 깊이2+운동2+정보공개2+감정2+소리1+연결1; 목표7 이상.
Speed: 첫운동2+전경2+변화빈도2+방향1+규모1+hard reveal1+관성1; 초고속 목표8 이상.
생성 전 점수는 design_score, 실제 관찰 후 measured_review를 분리한다. 전체 decode 성공은 영상 내용·얼굴·속도·고증 검수 성공이 아니다.
