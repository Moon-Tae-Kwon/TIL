## EIP (Engineer Information Processing)

## History

---

5장 데이터 통신

- CSMA/CD 방식
    - CSMA 방식에서 출돌이 발생하는 문제점을 해소하기 위해 CSMA 방식에 충돌 검출기능과 충돌 발생 시 재송신하는 기능을 부가한 방식
    - 통신 회선이 사용 중이면 일정 시간 동안 대기하고, 통신 회선상에 데이터가 없을때에만 데이터를 송신하며ㅡ 송신 중에도 전송로의 상태를 계속 감시
    - 송신 도중 충돌이 발생하면 손신을 중지하고ㅡ 모든 노드에 충돌을 알린 후 일정 시간이 지난 다음 데이터를 재송신 한다
    - 버스형 LAN에 가장 일반적으로 이용 된다.
    - 전송량이 적을 때 매우 효율적이고 신뢰성이 높다
    - 알고리즘이 간단하다.
    - 노드 장애가 시스템 전체에 영향을 주지 않으며, 장애 처리가 간단하다.
    - 일정 길이 이하의 데이터를 송신할 경우 충돌을 검출할 수 없다.
    - 전송량이 많아지면 충돌이 잦아져서 채널의 이용률이 떨어지고 전송 지연 시간이 급격히 증가한다.

- TDM (시분할 다중화)
    - 다수의 타임 슬롯으로 하나의 프레임이 구성되고, 각 타임 슬롯에 채널을 할당하여 다중화하는 것

- 동기식(Synchronous)TDM
    - 타임 슬롯을 모든 사용자에게 규칙적으로 할당
    - 별도의 데이터를 보내지 않아도 각 채널에 타임 슬롯을 미리 할당하고 고정 시킨다.
    - 구현이 간단 / 입력이 없는 채널은 대역폭 낭비

- 비동기식(Asynchronous)TDM
    - 입력에 버퍼를 두고 입력이 있는 채널에만 타임슬롯을 할당
    - 각 채널마다 헤더를 삽입하기 때문에 구현이 복잡

- OSI 7계층
    - 응
    - 표
    - 세
    - 전: TCP, UDP
    - 네: X.25, IP
    - 데: HDLC, LAPB, LLC, LAPD, PPP
    - 물: RS-232C, X.21

- X.25
    - DTE와 DCE간의 인터페이스를 제공하는 프로토콜로, 통신을 원하는 두 단말장치 가 패킷 교환망을 통해 패킷을 원활히 전달하기 위한 통신 절차.
    - 특징
        - X.25는 ITU-T에서 제정한 국제 표준 프로토콜로 우수한 호환성을 가진다
        - 강력한 오류 체크 기능으로 신뢰성이 높다
        - 한 외선에 장애가 발생하더라도 저상적인 경로를 선택하여 우회 전송이 가능하다.
        - 디지털 전송을 기본으로 하므로 전송 품질이 우수하다.
        - 가상 회선 방식을 이용하여 하나의 물리적 회선에 다수의 논리 채널을 할당하므로 효율성이 높다.
        - 축적 교환 방식을 사용하므로, 전송을 위한 처리 지연이 발생할 수 있다.

- HDLC 프레임 구조
    - 플래그 (Flag): 프레임의 시작과 끝을 나타내는 고유한 비트 패턴(01111110)
    - 주소부 (Address Field): 송. 수신국을 식별하기 위해 사용, 불특정 다수에게 전송하는 방송용은(Broadcast) 11111111 / 실험용 00000000
    - 제어부 (Control Field): 프레임의 종류를 식별하기 위해 사용, 제어부의 첫번째 두번째 비트를 사용하여 다음과같이 프레임 종류를 구별함
        - I 프레임: infomation 프레임 제어부가 0으러 시작하는 프레임, 사용자 데이터를 전달하는 역할을 함
        - S 프레임: Supervisor 프레임 제어부가 10으로 시작하는 프레임, 오류 제어와 흐름 제어를 위해 사용
        - U 프레임: Unnumbered 프레임 제어부가 11로 시작하는 프레임으로, 링크 동작 모드 설정과 관리를 함
    - 정보부 (Information Field): 실제 정보 메시지가 들어 있는 부분으로, 송. 수신 측 간의 협의에 따라 길이와 구성이 정해짐
    - FCS(Frame Check Sequence Field): 프레임 내용에 대한 오류 검출을 위해 사용되는 부분으로, 일반적으로 CRC 코드가 사용 됨.
    - 동작 모드
        - NRM = Normal Response Mode
        - ARM = Asynchronous Response Mode
        - ABM = Asynchronous Balanced Mode

- IPv4를 IPv6로 전환하는 전략
    - Dual Stack
    - Tunneling
    - Header Translation

- 자동 반복 요청 (ARQ, Automatic Repeat reQuset)
    - 오류 발생 시 수신 측은 오류 발생을 송신 측에 통부하고, 송신 측은 오류 발생 블록을 재전송하는 모든 절차를 의미한다.
    - 종류
        - Stop-and-Wait: 송신 측에서 한 개의 블록을 전송한 후 수신 측으로 부터 응답을 기다리는 방식 / 오류 발생한 경우 압서 송신했던 블록만 재전송하면 됨
        - Continuius ARQ: stop-and-wait가 갖는 오버레드를 줄이기 위해 연속적인 데이터 블록을 보내는 방식으로, 수신 측에서는 부정 응답(NAK)만 송신함
            - Go-Back-N: 여러 블록을 연속적으로 전송하고 수신 측에서 부정 응답(NAK)을 보내오면 송신 측이 오류가 발생한 블록 이후에 모든 블록을 재전송함
            - Selective Repeat: 연속적으로 전송하고 수신측에서 부정 응답(NAK)을 보내면 송신 측이 오류가 발생한 블록만을 재전송함 / 수신 측에서 데잍커를 처리하기 전에 원래 순서대러 조립해야 하므로, 더 복잡한 논리 회로와 큰 용량의 버퍼가 필요
        - Adaptive: 전송 효율을 최대로 하기 위해 데이터 블록의 길이를 채널의 상태에 따라 그때그때 동적으로 변경하는 방식

- Cyclic Redundancy Check (CRC)
    - 집단적으로 발생하는 오류에 대해 신뢰성 있는 오류 검출
    - 프레임 단위로 오류 검출을 위한 코드를 계산하여 프레임 끝에 부착하는데 이를 FCS라고 한다.

- 전송 제어 절차
    - 통신회선 접속 -> 데이터 링크 설정 -> 데이터 전송 -> 데이터 링크 해제 -> 통신 회선 절단

- 통신 방식
    - Simplex (단방향): 한쪽 방향으로만 전송이 가능한 방식 (예)라디오, TV
    - Half-Duplex (반이중): 양방향 전송이 가능하지만 동시에 양쪽 방향에서 전송할 수 없는 방식 (예)무전기, 모뎀을 이용한 데이터 통신
    - Full-Duplex (전이중): 동시에 양방향 전송이 가능한 방식 (예)전화, 전용선을 이용한 데이터 통신

- 변조방식
    - 아날로그 -> 아날로드: AM, FM, PM
    - 디지털 -> 아날로그: ASK(진폭), FSK(주파), PSK(위성), QAM
    - 아날로그 -> 데이터: PCM
    - 디지털 -> 디지털: 베이스밴드 전송

- Piggyback = piggybacking (피기백킹)
    - 데이터 프레임에 확인 응답을 포함시켜 전송하는 것

- 제어 전송 문자
    - SYN: 문자 동기
    - SOH(Start of Heading): 헤딩의 시작
    - STX(Start of TeXt): 본문의 시작 및 헤딩의 종료
    - ETX(End of TeXt): 본문의 종료
    - ETB(End of Transmission Block): 블록의 종료
    - EOT(End of Transmission): 전송 종료 및 데이터 링크의 해제
    - ENQ(ENQuiry): 상대편에 데이터 링크 설저 및 응답 요구
    - DLE(Data Link Escape): 전송 제어 문자 앞에 삽입하여 전송 데어 문자임을 알림
    - ACK(ACKnowledge): 수신된 메시지에 대한 긍정 응답
    - NAK(Negative Acknowledge): 수신된 메시지에 대한 부정 응답

- 라우팅 프로토콜

- IEEE 802의 주요 표준 규격

