# ansible + jenkins + cloudformation + github

## Code Example (ansible galaxy-jenkins 파일 참조)

---

* jenkins 템플릿화
```
cp ansiblebase-cf-template.py jenkins-cf-template.py
```
* 젠킨스 호스트는 AWS와 상호작용이 필요해서 트로포스피어와 동일한 개발자가 작성한 또 다른 라이브러리를 사용해 인스턴스 프로파일을 생성
```
pip install awacs
```
* 파일 집진행.
```
"""Generating CloudFormation template."""
from ipaddress import ip_network

from ipify import get_ip

from troposphere import (
    Base64,
    ec2,
    GetAtt,
    Join,
    Output,
    Parameter,
    Ref,
    Template,
)
# AWS 관리 서비스 이용을 위한 추가적인 라이브러리 적용
from troposphere.iam import (
    InstanceProfile,
    PolicyType as IAMPolicy,
    Role,
)

from awacs.aws import (
    Action,
    Allow,
    Policy,
    Principal,
    Statement,
)

from awacs.sts import AssumeRole
# 어플리케이션 이름 및 통신포트 업데이트
ApplicationName = "jenkins"
ApplicationPort = "8080"

GithubAccount = "Moon-Tae-Kwon"
GithubAnsibleURL = "https://github.com/{}/ansible".format(GithubAccount)

AnsiblePullCmd = \
    "/usr/local/bin/ansible-pull -U {} {}.yml -i localhost".format(
        GithubAnsibleURL,
        ApplicationName
    )

PublicCidrIp = str(ip_network(get_ip()))

t = Template()

t.add_description("Effective DevOps in AWS: HelloWorld web application")

t.add_parameter(Parameter(
    "KeyPair",
    Description="Name of an existing EC2 KeyPair to SSH",
    Type="AWS::EC2::KeyPair::KeyName",
    ConstraintDescription="must be the name of an existing EC2 KeyPair.",
))

t.add_resource(ec2.SecurityGroup(
    "SecurityGroup",
    GroupDescription="Allow SSH and TCP/{} access".format(ApplicationPort),
    SecurityGroupIngress=[
        ec2.SecurityGroupRule(
            IpProtocol="tcp",
            FromPort="22",
            ToPort="22",
            CidrIp=PublicCidrIp,
        ),
        ec2.SecurityGroupRule(
            IpProtocol="tcp",
            FromPort=ApplicationPort,
            ToPort=ApplicationPort,
            CidrIp="0.0.0.0/0",
        ),
    ],
))

ud = Base64(Join('\n', [
    "#!/bin/bash",
    "yum install --enablerepo=epel -y git",
    "pip install ansible",
    AnsiblePullCmd,
    "echo '*/10 * * * * {}' > /etc/cron.d/ansible-pull".format(AnsiblePullCmd)
]))

t.add_resource(Role(
    "Role",
    AssumeRolePolicyDocument=Policy(
        Statement=[
            Statement(
                Effect=Allow,
                Action=[AssumeRole],
                Principal=Principal("Service", ["ec2.amazonaws.com"])
            )
        ]
    )
))

t.add_resource(IAMPolicy(
    "Policy",
    PolicyName="AllowCodePipeline",
    PolicyDocument=Policy(
        Statement=[
            Statement(
                Effect=Allow,
                Action=[Action("codepipeline", "*")],
                Resource=["*"]
            )
        ]
    ),
    Roles=[Ref("Role")]
))

t.add_resource(InstanceProfile(
    "InstanceProfile",
    Path="/",
    Roles=[Ref("Role")]
))

t.add_resource(ec2.Instance(
    "instance",
    ImageId="ami-d9b616b7",
    InstanceType="t2.micro",
    SecurityGroups=[Ref("SecurityGroup")],
    KeyName=Ref("KeyPair"),
    UserData=ud,
    IamInstanceProfile=Ref("InstanceProfile"),
))

t.add_output(Output(
    "InstancePublicIp",
    Description="Public IP of our instance.",
    Value=GetAtt("instance", "PublicIp"),
))

t.add_output(Output(
    "WebUrl",
    Description="Application endpoint",
    Value=Join("", [
        "http://", GetAtt("instance", "PublicDnsName"),
        ":", ApplicationPort
    ]),
))

print (t.to_json())
```
* 템플릿화
```
python jenkins-cf-template.py > jenkins-cf.template
```
* stack 실행
```
aws cloudformation create-stack --capabilities CAPABILITY_IAM --stack-name jenkins --template-body file://jenkins-cf.template --parameters ParameterKey=KeyPair,ParameterValue=EffectiveDevOpsAWS
```
* 상태 확인
```
aws cloudformation wait stack-create-complete --stack-name jenkins
aws cloudformation describe-stacks --stack-name jenkins --query 'Stacks[0].Outputs[0]'
```
> 테스트 당시 문제점
- cloudfromation 동작 중 인스턴스에서 진행되는 UserData 변수의 진행시에 /usr/local/bin/ansible-pull -U https://github.com/Moon-Tae-Kwon/ansible jenkins.yml -i localhost 명령어의 진행속도가 너무 느려져서 락이 걸리는 형태
    * top -c 명령어를 통한 기존의 실행되던 PID삭제 처리 및 수동 실행 이후 cron.d 폴더에 등록하는 ansible-pull echo 명령어도 수동 실행
* linux cron.d echo 동작시에 입력되는 코드는 아래의 코드이며 cron이 동작할 경우에는 bad username 의 error log 발생
```
echo '*/10 * * * * /usr/local/bin/ansible-pull -U https://github.com/Moon-Tae-Kwon/ansible jenkins.yml -i localhost' > /etc/cron.d/ansible-pull
```
* 위의 부분으로 jnekins 실행결과 버전이슈로 Credentials 메뉴는 확인이 불거능 해당 메뉴는 github 의 token을 사용하기위해 설치 필요
    * jenkisn version 업데이트는 진행 방법은 아래와 같이 진행
```
wget http://updates.jenkins-ci.org/download/war/2.156/jenkins.war # 테스트르르 위해 최신 파일로 다운로드
mv /usr/lib/jenkins/jenkins.war ./jenkins.war_old
cp jenkins.war /usr/lib/jenkins/ # war 내용을 다운로드 받은 파일과 교체
/etc/rc.d/init.d/jenkins stop
/etc/rc.d/init.d/jenkins start
/etc/rc.d/init.d/jenkins restart # java 버전 1.7로 구동되고 있던 내용이라 java version up 필요.
yum install java-1.8.0-openjdk # rodhet 계열이라 java 1.8 버전 다운로드 및 설치
alternatives --config java # java 1.7 버전에서 java 1.8 버전으로 교체
/etc/rc.d/init.d/jenkins restart #정상 구동 확인.
```
* [CI 준비](/TIL/jenkins/jenkins-cloudformation-setup.md)

