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