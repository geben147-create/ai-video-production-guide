# 변환 프롬프트를 강화하는 방법

## 먼저 원인을 분리한다
해상도=픽셀 수, 디테일=재질이 남는 정도, 시간 안정성=프레임 사이 형태 유지, 연출=운동과 정보 공개, 연결=앞뒤 컷의 시선·운동 일치다. 768p라도 건축이 녹거나 공간이 튀면 품질이 낮다. 실제 같은 소스·같은 길이로 비교하지 않은 모델 우열은 단정하지 않는다.

## 1. 시작 이미지의 공간을 지킨다
원본에 있는 한 공간에서 카메라가 어디서 어디까지 가는지 쓴다. 통로가 없는데 사람 사이 관통, 닫힌 벽 통과, 보이지 않는 항구→시장→궁전의 연쇄 공개를 한 번에 요구하지 않는다. 공간이 달라질 때는 편집 컷으로 분리한다. 원경의 보이지 않는 면은 재구성이라 정확한 연속성으로 주장할 수 없다.

## 2. 속도와 복잡도를 구별한다
EXTREME를 반복하는 대신 전경이 스치는 방향·거리, 이동 목표, 고도 변화 하나를 구체화한다. 기본 권장: 주 이동1개, 보조 행동1개, 큰 방향 변경1개, 주 공개1개. 하이라이트에서만 검증된 두 번째 공개를 허용한다. 카메라 속도를 낮추지 않고 동시에 바뀌는 사물 수를 줄인다. 모든 컷에 5단계 급강하→회전→상승을 복붙하지 않는다.

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
5 하나의 강한 공개와 피사체 행동.
6 고정 기하·재질·광원.
7 종료 방향과 다음 앵커.
8 꼭 필요한 제외 항목만.

### 범용 영어 템플릿
`[Scene and purpose]. Starting from the supplied image, the camera is already moving rapidly [direction] toward [visible target]. [One near foreground object] sweeps past [side] with strong parallax. The camera [one controlled bank/rise] to reveal [one information-bearing destination] while keeping forward momentum. [Subject action if necessary]. Preserve [named geometry/materials] and the fixed [light direction]. End moving [direction] with [anchor] at [screen position]. No talking faces, no HUD, no morphing materials, no slow start or frozen end.`

### 개선 예시: 포룸
`Rome AD117, Trajan's Forum. Starting beneath the existing red canopy, the camera is already moving rapidly forward through the clear aisle. The canopy fringe whips above the lens. One shallow upward bank reveals the equestrian statue framed by the existing marble colonnade. Keep columns, rooflines and statue rigid; keep daylight from camera-left. Small pedestrians remain in the middle distance, with no face close-ups. Carry forward motion toward the statue at center-right. No HUD, material morphing, slow start or frozen end.`
과거 요청의 광장 진입·바닥 다이브·동상 상승·파사드 돌진을 한 공간/한 공개로 줄인 제작 제안이다. 아직 생성 성공 검증을 한 예시는 아니다.

### 개선 예시: 벽돌 도장
`A close lateral tracking shot along the supplied Roman brick sample. The camera is moving immediately; nearby clay grains pass quickly across the bottom edge. A short rack focus reveals the existing stamped impression under fixed raking light. Keep the brick stationary, its edges and clay material unchanged. Do not invent lettering or turn the surface into metal. Finish with the stamp at center. No face, overlay or material morph.`
실제 도장 글자 판독은 원본 자료로 하고 생성 영상이 새 글자를 만들어 증거가 되게 하지 않는다.

## 모델 변경 시
현재 실제 OpenAPI 필드를 다시 확인한다. Wan 프롬프트를 H3로 옮기더라도 해상도/오디오/종료프레임 지원을 별도 확인한다. 장식적 형용사보다 구체적 공간 지시를 유지한다. H3 768p가 현재 프로젝트의 무료 해상도라는 사실과 품질 우위는 별개다.
