"""Generating CloudFormation template.
트로포스피어 모듈로부터 여러 정의를 임포트 """
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
""" 신규 스크립트 작성시 코드의 나머지 부분을 쉽게 편집 할 수 있도록 첫 번째 변수를 정의 
+ ansible-> 응용프로그램명을 정의한다."""
ApplicationName = "helloworld"
ApplicationPort = "3000"
""" + ansible-> github 모듈사용을 위한 부분"""
GithubAccount = "Moon-Tae-Kwon"
GithubAnsibleURL = "https://github.com/{}/ansible".format(GithubAccount)

AnsiblePullCmd = \
    "/usr/local/bin/ansible-pull -U {} {}.yml -i localhost".format(
        GithubAnsibleURL,
        ApplicationName
    )
PublicCidrIp = str(ip_network(get_ip()))

t = Template()
""" 스택 식별을 위해 설명을 추가 기재 """
t.add_description("Effective DevOps in AWS: HelloWorld web application")
""" EC2 인스턴스를 띄울 때 사용할 키페어를 선택하도록 하는 매개변수.
매개변수가 최종 템플릿에 존재하도록 하기 위해 템플릿 클래스에 정의된 add_paramter() 함수도 사용할 것이다. """
t.add_parameter(Parameter(
    "KeyPair",
    Description="Name of an existing EC2 KeyPair to SSH",
    Type="AWS::EC2::KeyPair::KeyName",
    ConstraintDescription="must be the name of an existing EC2 KeyPair.",
))
""" 보안 그룹 포트 22포트는 작업한 대상 PC의 공인 IP만 허용, 3000은 앞에서 선언된 ApplicationPort 변수에 정의됐다.
이번에 정의된 정보는 이전과 같이 매개변수가 아닌 리소스이다.
따라서 add_resource() 함수를 이용해 새 리소스를 추가할 것이다. """
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
""" EC2 로그인 이후 작업을 위해 EC2가 제공하는 UserData 기능을 이용할 것이다. (가상 머신 생성 시 단 한번 싱행되는 일련의 명령어를 제공하는 UserData 매개변수)
base64로 인코딩해 API 호출에 추가해야 한다는 제약 사항이 존재 (아래 내용 삭제)
ud = Base64(Join('\n', [
    "#!/bin/bash",
    "sudo yum install --enablerepo=epel -y nodejs",
    "wget https://raw.githubusercontent.com/Moon-Tae-Kwon/TIL/master/node/helloworld.js -O /home/ec2-user/helloworld.js",
    "wget https://raw.githubusercontent.com/Moon-Tae-Kwon/TIL/master/node/helloworld.conf -O /etc/init/helloworld.conf",
    "sudo start helloworld"
]))
"""
"""+ ansible-> 새로 추가된 UserData 내용 깃 앤서블 설치 및 Ansible PullCmd 변수가 포함된
명령어를 실행하고 매 10분 마다 명령어를 다시 실행 하도록 구성된 내용"""
ud = Base64(Join('\n', [
    "#!/bin/bash",
    "yum install --enablerepo=epel -y git",
    "pip install ansible",
    AnsiblePullCmd,
    "echo '*/10 * * * * root {}' > /etc/cron.d/ansible-pull".format(AnsiblePullCmd)
]))
""" 테스크를 위한 하드 코딩된 내용으로 진행
클라우드포메이션에서는 Ref 키워드를 사용해 템플릿의 기존 하위 영역을 참조할 수 있다.
트로포스피어는 Ref() 함수를 호출해 이를 수행한다. """
t.add_resource(ec2.Instance(
    "instance",
    ImageId="ami-d9b616b7",
    InstanceType="t2.micro",
    SecurityGroups=[Ref("SecurityGroup")],
    KeyName=Ref("KeyPair"),
    UserData=ud,
))
""" 스택을 띄위는 동안 생성된 유용한 정보를 출력할 수 있다.
두 가지 유용한 정보를 기재 웹응용프로그램에 접속하는 URL / 다른 하나는 필요 시 SSH로 인스턴스에접근할 수있는 공인 IP
위의 정보를 얻기위해 클라우드포메이션은 Fn::GetAtt을 사용해야 한다. 트로포스피어는 GetAttr() """
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
