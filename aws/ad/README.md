# AWS Managed Microsoft AD

## test

* 완전 관리형 AD
* Windows Server 2012 R2 구동
* 도메인 컨트롤러는 VPC 내의 서로 다른 서브넷 (서브넷은 서로 다른 가용영역에서 동작)
```
TCP/UDP 53 - DNS (DNS 도메인 통신 프로토콜)
TCP/UDP 88 - Kerberos authentication (커베로스는 "티켓"을 기반으로 동작하는 컴퓨터 네트워크 인증 암호화 프로토콜로)
UDP 123 - NTP (네트워크 타임 프로토콜)
TCP 135 - RPC (한 프로그램이 네트웍 상의 다른 컴퓨터에 위치하고 있는 프로그램에 서비스를 요청하는데 사용되는 프로토콜)
UDP 137-138 - Netlogon (NetBios)
TCP 139 - Netlogon (NetBios)
TCP/UDP 389 - LDAP (LDAP)
TCP/UDP 445 - SMB (데이터 공유)
TCP 636 - LDAPS (LDAP over TLS/SSL) (보안)
TCP 873 - Rsync (데이터 공유)
TCP 3268 - Global Catalog
TCP/UDP 1024-65535 - Ephemeral ports for RPC
```
* NetBios = Windows 에서 중요시되는 통신프로토콜이며, 컴퓨터 이름을 교환하거나 매핑하는 역할을 한다(조금더 자세하게 확인해봐야 겠다.)
* NAT 사용이 적용되지 않는다.
* 멀티팩터 인증의 경우에는 온프라미스 클라우드 기반의 RADIUS 설치해야한다. (RADIUS 표준 포트는 1812)
* gMSA (그룹관리 계정) [gMSA](https://docs.aws.amazon.com/ko_kr/directoryservice/latest/admin-guide/ms_ad_key_concepts_gmsa.html)

---

* AD 연동

* Standard Edition: AWS Managed Microsoft AD (Standard Edition)는 직원이 5,000명 이하인 중소기업의 기본 디렉터리로 최적화되어 있습니다. 이 에디션은 사용자, 그룹, 컴퓨터 등 디렉터리 객체를 최대 30,000*개까지 지원하는 데 충분한 스토리지 용량을 제공합니다.
* Enterprise Edition: AWS Managed Microsoft AD (Enterprise Edition)는 최대 500,000개의* 디렉터리 객체를 보유한 엔터프라이즈 조직을 지원하도록 설계되었습니다.
* AWS AD이 생성되는 서브넷은 별도 분리 조치를 해야한다 (그렇지 않을 경우에는 AWS AD에 대한 별도 보안그룹이 없기 때문에 전체 허용처리된다.)