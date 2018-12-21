# codedeploy 설정

## Code Example

---

* IAM 설정 추가.
```
aws iam create-role --role-name CodeDeployServiceRole --assume-role-policy-document https://raw.githubusercontent.com/Moon-Tae-Kwon/TIL/master/aws/codedeploy/CodeDeploy-Trust.json
iam attach-role-policy --role-name CodeDeployServiceRole --policy-arn arn:aws:iam::aws:policy/service-role/AWSCodeDeployRole
```
* codedeploy setup

![codedeploy-setup-1](/TIL/images/codedeploy-setup-1.png)
![codedeploy-setup-2](/TIL/images/codedeploy-setup-2.png)
![codedeploy-setup-3](/TIL/images/codedeploy-setup-3.png)
![codedeploy-setup-4](/TIL/images/codedeploy-setup-4.png)