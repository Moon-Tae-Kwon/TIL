## EIP (Engineer Information Processing)

## History

---

2장. 전자계산기 구조

- 플린(Flynn)의 분류
    - SISD(Single Instruction stream Single Data stream)
    - SIMD(Single Instruction stream Multi Data stream)
    - MISD(Multi Instruction stream Single Data stream)
    - MIMD(Multi Instruction stream Multi Data stream)

- 순서논리회로: 플립플롭, 카운터, 레지스터, RAM, CPU 등
- 조합논리회로: 반가산기, 전가산기, 병렬가산기, 반감산기, 전감산기, 디코더, 인코더, 멀티플렉서, 디멀티플렉서, 다수결회로, 비교기 등

- 패리티 검사 코드
    - 1bit의 패리티 체크비트 추가하는 것으로 1bit오류만 검출

- 해밍코드
    - 오류를 스스로 검출하여 교정이 가능한 코드
    - 2bit의 오류를 검출할 수 있고 1bit 오류를 교정할수 있다.

- 메모리 인터리빙
    - 단위 시간에 여러 메모리의 접근이 가능하도록 병행 접근하는 기법
    - 기억자치의 접근 시간을 효율적으로 높일 수 있으므로 캐시 기억장치, 고속 DMA 전송등에 많이 사용
    - CPU가 버스를 통해 주소를 전달하는 속도는 빠름
    - 메모리 모듈의 처리 속도가 느리기 떄문에 병행접근이 가능

- IC 성능 평가요소
    - 전파 지연 시간, 전력 소모, Fan Out, 잡음 허용치

- JK 플립플롭
    - 상태 무 ,공,일,보

- 매핑 프로세스의 종류
    - Direct (직접)
    - Associative (어소시에이티브)
    - Set-Associative (세트-어소시에이티브)

- 버스 사용 우선순위 (가변우선 순위 방식)
    - 회전 우선순위 (Rotating) / 임의 우선 순위 (Random Priorty) / 동등 우선순위 (Equal Priority) / 최소-최근 사용 (Least-recently used)

- SSD (Solid State Drive) 방식
    - SLC(Single Level Cell) = 셀 당 1bit
    - MLC(Multi Level Cell) = 셀 당 2bit
    - TLC(Triple Level Cell) = 셀 당 3bit

- CPU 메이저 상태 (마이크로 사이클)
    - Fetch, Indirect, Execute, Interrupt (인출, 간접, 실행, 인터럽트)

- 핀 수를 구하기
    - Address 핀 수: 워드의 개수와 관련이 있다, 워드의 개수가 1024일 경우에 2^10 즉 10개의 Address 핀이 필요.
    - data 핀 수: data 핀 수는 워드의 크기와 동일 8bit 일 경우 8개의 핀이 필요.
    - chip select bit: 선택할지 말지 결정하는 것이므로 1개의 핀만 있으먄 된다.

- 그레이코드 = 비가중 코드
    - 2진코드 변환 앞에 숫자는 그대로 사용하고 XOR 연산

- 접근 방식에 따른 분류

- 연산자 기능 

- 인터럽트 동작 원리

