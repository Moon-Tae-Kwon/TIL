# run-instances

## Code Example

* Amazon Linux 신규 버전 확인.
```awscli
aws ec2 describe-images --filters "Name=description,Values=Amazon Linux AMI * x86_64 HVM GP2" --query 'Images[*].[CreationDate, Description, ImageId]' --output text | sort -k 1 | tail
```
* VPC 확인.
```awscli
aws ec2 describe-vpcs
```
* 보안 그룹 설정 및 확인
```awscli
aws ec2 create-security-group --group-name HelloWorld --description "Hello World Demo" --vpc-id vpc-a58190cd
aws ec2 authorize-security-group-ingress --group-id sg-03ac00f97a6286a69 --protocol tcp --port 22 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-id sg-03ac00f97a6286a69 --protocol tcp --port 3000 --cidr 0.0.0.0/0
aws ec2 describe-security-groups --group-id sg-03ac00f97a6286a69 --output text
```
* 키페어 생성
```awscli
aws ec2 create-key-pair --key-name EffectiveDevOpsAW
```
* 인스턴스 작동 및 확인
```awscli
aws ec2 run-instances --instance-type t2.micro --key-name EffectiveDevOpsAWS --security-group-ids sg-03ac00f97a6286a69 --image-id ami-d9b616b7 --subnet-id subnet-af030fc7
aws ec2 describe-instance-status --instance-ids i-0cddd3941adc97358
```
* IP 확인
```awscli
ec2 describe-instances --instance-ids i-0cddd3941adc97358 --query "Reservations[*].Instances[*].PublicIpAddress"
```
* AWS Instances 접속
```local-터미널
ssh -i ~/.ssh/EffectiveDevOpsAWS.pem ec2-user@13.209.85.26
```
* instances node install 웹사이트 작성 [sourcecode](/TIL/node/helloworld.js)
```instances console
sudo yum install --enablerepo=epel -y nodejs
node -v
vim helloworld.js # TIL node folder
node helloworld.js
```
* http://13.209.85.26:3000 #public IP (완료)

* linux upstart를 적용하여 node 실행유지 [sourcecode](/TIL/node/helloworld.conf)
> [TIP] AWS의 경우 ENI기반으로 네트워크 서비스가 시작디기 전에 응용프로그램이 시작된다면 네트워크에 정상적으로 접속 하지 못할 수도 있다
```instances console
sudo vim /etc/init/helloworld.conf # TIL node folder
sudo start helloworld
```
* node 종료 및 instances 종료(삭제)
```instance console
sudo stop helloworld
ec2-metadata --instance-id
```
```local 터미널
aws ec2 terminate-instances --instance-ids i-0cddd3941adc97358
```