# info

* 리눅스 ulimit
```
ulimit는 프로세스의 자원 한도를 설정하는 명령으로, soft한도와 hard한도 두가지가 있습니다.
soft : 새로운 프로그램을 생성하면 기본으로 적용되는 한도
hard : 소프트한도에서 최대로 늘릴 수 있는 한도

apache 와 같이 웹 서비스를 운영 시 동접자가 많은 경우 구동되는apache 프로세스 수와 해당  프로세스가 처리하게되는 파일 수 또한 증가 하게 됩니다.
이에 따라 시스템 적으로도 해당 요청에 대응 할 수 있도록 상향 설정이 필요로 하며, 해당 설정을 조정 하는 방법에 대해서 다루도록 하겠습니다.

각 항목의 설명

core file size          (blocks, -c) 0                        : 코어파일의 최대크기

data seg size           (kbytes, -d) unlimited          : 프로세스의 데이터 세그먼트 최대크기

scheduling priority             (-e) 0                        : 쉘에서 생성되는 파일의 최대 크기

file size               (blocks, -f) unlimited                         

pending signals                 (-i) 14943

max locked memory       (kbytes, -l) 64

max memory size         (kbytes, -m) unlimited    : resident set size의 최대 크기(메모리 최대크기)

open files                      (-n) 1024                         : 한 프로세스에서 열 수 있는 open file descriptor의 최대 숫자(열수 있는 최대 파일 수)

pipe size            (512 bytes, -p) 8                          : 512-바이트 블럭의 파이프 크기

POSIX message queues     (bytes, -q) 819200

real-time priority              (-r) 0

stack size              (kbytes, -s) 10240

cpu time               (seconds, -t) unlimited             : 총 누적된 CPU 시간(초)

max user processes              (-u) 1024                  : 단일 유저가 사용가능한 프로세스의 최대 갯수

virtual memory          (kbytes, -v) unlimited         : 쉘에서 사용가능 한 가상 메모리의 최대 용량

file locks                      (-x) unlimited
```
* 리눅스 OS 선택 기준
```
1. 필요한 조건과 환경에 따라서 버전을 사용
2. 각 OS에 대한 실질적인 운영에 필요한 어플리케이션의 성능 테스트 진행 (테스트 요소는 어플리케이션을 개발하는 개발팀으로 확인하는 방버 등.)
```
* AWS role / policy
```
AWS Role (역활)
역할을 사용하여 일반적으로 AWS 리소스에 액세스할 수 없는 사용자, 애플리케이션 또는 서비스에 액세스 권한을 위임할 수 있습니다
- 한 계정의 사용자는 동일한 또는 다른 계정의 역할로 전환할 수 있습니다. 사용자는 역할을 사용하는 동안 해당 작업만을 수행하고 해당 역할에서 허용한 리소스만 액세스할 수 있지만, 이들의 원래 사용자 권한은 일시 중지된 상태입니다. 사용자가 역할을 끝내면 원래 사용자 권한이 회복됩니다.
AWS Policy (정책)
정책은 개체 또는 리소스에 연결될 때 해당 권한을 정의하는 AWS의 객체입니다.
- 복수 문 및 복수정책 = 가장 좋은 방법은 리소스 유형에 따라 정책을 나누는 것입니다.
- 관리형 정책과 인라인 정책의 선택
권장은 관리형 정책으로 진행하며, 인라인 정책이 사용되는 경우에는 1:1매칭을 통한 관리가 필요할 경우
- 명시적 거부와 묵시적 거부 차이
적용 가능한 정책이 Deny 설명문을 포함한다면 요청은 명시적으로 거부됩니다. 정책이 Allow 설명문과 Deny 설명문을 포함한 요청에 적용된다면 Deny 설명문은 Allow 설명문에 우선합니다. 이 요청은 명시적으로 거부됩니다.
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": "aws-portal:*",
            "Resource": "*"
        }
    ]
}
적용 가능한 Deny 설명문이 없고 적용 가능한 Allow 설명문도 없다면 묵시적 거부가 발생합니다. IAM 사용자, 역할 또는 연합된 사용자가 기본적으로 액세스를 거부하기 때문에 명시적으로 작업을 허용해야 합니다. 그렇지 않으면 액세스는 묵시적으로 거부됩니다.
{
    "Version": "2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Action": [
            "iam:AttachUserPolicy",
            "iam:CreateUser",
            "iam:DeleteUser",
            "iam:DeleteUserPolicy",
            "iam:DetachUserPolicy",
            "iam:GetUser",
            "iam:GetUserPolicy",
            "iam:ListAttachedUserPolicies",
            "iam:ListUserPolicies",
            "iam:ListUsers",
            "iam:PutUserPolicy",
            "iam:UpdateUser"
        ],
        "Resource": "*"
    }
}
* Deny 문이없지만 Allow 설명문에도 없는 다른 권한들은 묵시적으로 거부
```
* AWS 구성도
1. 기본적인 아키텍처로 이중화 및 그 밖의 사항들을 확인 하지 않은 아키텍처 (cacco를 이용해 보고자 간단하게 만들어 봤다.)
![aws-cacco](/TIL/images/aws-game.png)