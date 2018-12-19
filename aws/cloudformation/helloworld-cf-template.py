"""Generating CloudFormation template."""
# 트로포스피어 모듈로부터 여러 정의를 임포트
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
# 신규 스크립트 작성시 코드의나머지 부분을 ㄱ쉽게 편집 할 수 있도록 첫 번째 벼수를 정의
ApplicationPort = "3000"
PublicCidrIp = str(ip_network(get_ip()))

t = Template()
# 스택 식별을 위해 설명을 추가 기재
t.add_description("Effective DevOps in AWS: HelloWorld web application")
# EC2 인스턴스를 띄울 때 사용할 키페어를 선택하도록 하는 매개변수.
# 매개변수가 최종 템플릿에 존재하도록 하기 위해 템플릿 클래스에 정의된 add_paramter() 함수도 사용할 것이다.
t.add_parameter(Parameter(
    "KeyPair",
    Description="Name of an existing EC2 KeyPair to SSH",
    Type="AWS::EC2::KeyPair::KeyName",
    ConstraintDescription="must be the name of an existing EC2 KeyPair.",
))
# 보안 그룹 포트 3000은 앞에서 선언된 ApplicationPort 변수에 정의됐다.
# 이번에 정의된 정보는 이전과 같이 매개변수가 아닌 리소스이다.
# 따라서 add_resource() 함수를 이용해 새 리소스를 추가할 것이다.
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
# EC2 로그인 이후 작업을 위해 EC2가 제공하는 UserData 기능을 이용할 것이다. (가상 머신 생성 시 단 한번 싱행되는 일련의 명령어를 제공하는 UserData 매개변수)
# base64로 인코딩해 API 호출에 추가해야 한다는 제약 사항이 존재
ud = Base64(Join('\n', [
    "#!/bin/bash",
    "sudo yum install --enablerepo=epel -y nodejs",
    "wget http://bit.ly/2vESNuc -O /home/ec2-user/helloworld.js",
    "wget http://bit.ly/2vVvT18 -O /etc/init/helloworld.conf",
    "start helloworlsd"
]))

t.add_resource(ec2.Instance(
    "instance",
    ImageId="ami-a4c7edb2",
    InstanceType="t2.micro",
    SecurityGroups=[Ref("SecurityGroup")],
    KeyName=Ref("KeyPair"),
    UserData=ud,
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

print t.to_json()
