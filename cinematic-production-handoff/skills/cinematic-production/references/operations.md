# 무료 생성·검증·인계

1. 모델 목록과 정확한 image2video OpenAPI를 조회한다. 지원하지 않는 필드를 임의로 넣지 않는다.
2. 현재 계정에서 동일한 brand/model/input/numOutputs 요청을 제출 직전 두 번 조회한다.
3. 두 결과 모두 discountCost=0, activityInfo.discountCredit=0, activityMode=unlimited여야 한다. 값 누락·화면 충돌은 제출 금지. 구독 Ultra, Free 배지, 과거 무료 기간은 대신할 수 없다.
4. 정확한 요청 JSON의 SHA256, 두 원본 견적, UTC 확인 시각, 예상0, 응답 task ID를 저장한다. 비용을 수동 0으로 재작성하지 않는다.
5. 최대4 슬롯. 제출 전 scene_id/task_id/파일 존재를 확인한다. 제출 응답 유실은 불확실 상태로 두고 Assets를 조정 확인한 뒤 재시도한다. 두 세션의 동시 writer를 금지한다.
6. 실제 Assets 결과 URL로 저장. ffprobe, 전체 ffmpeg decode, SHA256, 마지막 프레임 추출. 실제 비용 차감 여부는 확인 가능한 기록으로만 표시하며 unavailable을 0으로 바꾸지 않는다.
7. planned→prepared→quoted→submitted→provider_succeeded→downloaded→decode_verified→visually_reviewed. failed와 blocked_cost는 별도. 완료 정의를 명시한다.
8. 보고: 완료 n/100 · 남은 n · 제출 중 n. 토큰 미제공이면 미제공. 생성시간은 submit→provider 완료, turnaround는 submit→저장으로 구분. 무료 차단 중 ETA는 재개 시점 불명으로 표시한다.
9. 예약은 실제 제출/저장 처리용이어야 한다. 상태만 반복 보고하지 않는다. 무료 차단이면 준비작업을 하되 변경 없는 알림을 반복하지 않는다. 인계 시 기존 예약을 일시중지하고 새 세션 하나만 소유하게 한다.

관측된 API: Wan alibaba/wan-v3-0 5초480p16:9 무음. H3 minimax/minimax-h3는 image,prompt,duration(4~15),resolution(480p/768p/2K) 지원; aspectRatio/generateAudio 필드는 해당 조회 스키마에 없음. 무음/비율은 실제 결과 검증 필요. 모델 스키마는 다음 실행에서 다시 조회한다.
