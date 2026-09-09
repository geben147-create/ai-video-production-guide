# 변환 프롬프트를 강화하는 방법

## 먼저 원인을 분리한다
해상도=픽셀 수, 디테일=재질이 남는 정도, 시간 안정성=프레임 사이 형태 유지, 연출=운동과 정보 공개, 연결=앞뒤 컷의 시선·운동 일치다. 768p라도 건축이 녹거나 공간이 튀면 품질이 낮다. 실제 같은 소스·같은 길이로 비교하지 않은 모델 우열은 단정하지 않는다.

## 1. 원래 세션의 동선을 먼저 보존한다
이 세션에서 사용했던 원문 프롬프트를 시작점으로 삼는다. 도시→하강→골목→전경 가림→새 공간 공개 같은 연쇄와 속도 표현을 요약하거나 삭제하지 않는다. 통로·대상·방향이 모호한 부분만 구체화한다. 서로 다른 공간의 생성적 재구성을 실측 지리로 주장하지 않는다.

## 2. 극도로 빠른 속도와 연속 공개가 기본이다
첫 프레임부터 EXTREME MOTION. 0.5~1.2초마다 전경 통과·방향·고도·규모·목표 변화를, 1.5~2.5초마다 강한 공개를 목표로 한다. 이는 설계 목표이며 실제 결과에서 검수한다. FAST→FASTER→BANK→REVEAL→DIVE→BOOST의 리듬을 유지한다. `한 이동·한 공개`로 제한하지 않는다. 속도의 종류를 바꾸되 전환 전에 감속하지 않는다.
재질·손·기둥 오류를 고치려고 카메라를 정지시키거나 평범한 팬·줌으로 바꾸지 않는다. 특정 오류 물체의 묘사·접촉·가림 위치만 수정한다. 모델이 동선을 구현하지 못하면 원래 리듬을 유지하는 컷 분할을 검토하며 역동성 축소를 자동 대안으로 사용하지 않는다.

## 3. 고정할 요소를 이름으로 적는다
`The marble columns, rooflines and paving remain rigid and retain their layout. The vase stays turquoise glass throughout.`처럼 핵심 구조·재질을 지정한다. 단순 `stable architecture`만으로 해결된다고 기대하지 않는다. 인물이 중요하지 않으면 배경 크기로 유지하고 얼굴로 접근하지 않는다. 모션블러는 빠른 가까운 전경에만 두고 목표 재질은 읽히게 한다.

## 4. 전경과 원근
앞쪽 밧줄 하나→중경 작업→뒤쪽 배. 가까운 전경이 빨리 움직이고 원경이 상대적으로 덜 움직이는 시차가 속도감을 준다. 먼 도시만 확대하면 줌처럼 보인다. 렌즈 숫자는 제안이며 실제 카메라 메타데이터가 아니다. 24mm라고 쓰기보다 낮은 카메라·근접 전경·먼 목표의 관계를 함께 적는다.

## 5. 광원과 재질
태양 방향 고정, 건물의 밝은 면과 어두운 면 고정. 돌은 돌, 금속은 금속, 천은 천으로 유지한다. 빛을 늘려 전부 밝히기보다 사광·반사·그림자로 표면을 읽힌다. 연기·꽃가루·물보라는 발생 이유가 있는 곳에서 짧게 가림에 사용한다. 지속적으로 화면을 덮어 변형을 숨기지 않는다.

## 6. 전환은 목적이 있어야 한다
기둥이 렌즈를 가림→동일 이동 방향으로 뒤 공간 공개. 다음 컷의 밝은 영역과 주 대상 위치를 맞춘다. 동일 소스를 반복 사용하면 매번 출발지로 되돌아가는 문제가 생긴다. 실제 마지막 프레임 연결 또는 명시적인 편집 전환을 택한다. imageTail은 선택사항이며 존재만으로 연속성을 보장하지 않는다. 새로운 imageTail을 쓰면 비용 재확인.

## 최종 프롬프트 순서
1 장면·한 가지 설명 목적.
2 시작 이미지에서 보이는 구도와 공간.
3 첫 프레임부터 이동할 방향과 목표.
4 렌즈 가까운 전경 통과.
5 연속적인 강한 공개·급강하·뱅크·규모 전환과 피사체 행동.
6 고정 기하·재질·광원.
7 종료 방향과 다음 앵커.
8 꼭 필요한 제외 항목만.

### 범용 영어 템플릿 — 속도와 연속 전환 보존
`[Scene and purpose]. The camera is already moving at extreme speed from frame one. It races [path A], with [foreground] whipping inches past the lens. Without slowing, it hard-banks [direction] and [occluder] wipes the frame, instantly revealing [space/target B]. It immediately dives toward [target C], skims [surface], then climbs into [scale reveal D]. Keep [named structures/materials] consistent and the light fixed. The final movement carries full velocity toward [next anchor and position]. Extreme parallax, rapid visual discoveries, no slow start, no hovering, no deceleration before turns, no frozen end, no talking face or HUD.`
괄호는 해당 소스·대본에 맞춘다. 모든 장면에 동일 동선을 복사하지 않고 원문 동선의 종류를 교차한다.

### 포룸: 이 세션 원래 동선을 유지한 예시
`Rome AD117 scene 048. Axial 18mm blockbuster reveal of Trajan's Forum. From the first frame the camera surges between the near red curtain and marble column, both sweeping past inches from the lens. It races behind the rear-facing visitors into the vast plaza, dives low over reflective imported marble, then rises toward the equestrian statue and Basilica Ulpia facade while retaining full forward momentum. Human figures show scale and never address the camera. Stable architecture, statue and floor pattern; no HUD, no text, no slow drone, no hover, no frozen end.`
이것은 원래 준비 프롬프트다. 광장 진입→바닥 다이브→동상·파사드 상승을 삭제하지 않는다. 추가 개선이 필요하면 대리석 재질 고정·기둥 배열 유지 등의 국소 제약을 덧붙인다.

## 모델 변경 시
현재 실제 OpenAPI 필드를 다시 확인한다. Wan 프롬프트를 H3로 옮기더라도 해상도/오디오/종료프레임 지원을 별도 확인한다. 원문의 extreme speed, dive, bank, rise, foreground wipe와 연속 reveal을 삭제·완화하지 않는다. 구체적 공간 지시를 추가해 의미를 유지한다. H3 768p가 현재 프로젝트의 무료 해상도라는 사실과 품질 우위는 별개다.
