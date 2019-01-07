# jenkisn 작업등록

## Code Example

---
1. 별도의 github repo 생성
2. github tokens 생성
3. jnekins Credentials
    1. system
    2. global credentials
    3. username with password / global / git사용자명 / token 입력
4. jenkins 새작업 등록
![jenkins-setup-1](/images/jenkins-setup-1.png)
![jenkins-setup-2](/images/jenkins-setup-2.png)
* helloworld 응용프로그램 구현하기 (사전에 생성한 github repo) [helloworld-github](https://github.com/Moon-Tae-Kwon/helloworld)
    * git clone https://github.com/Moon-Tae-Kwon/helloworld.git
    * cd helloworld
    * git checkout -b initial-baranch
    * touch helloworld.js
> 테스트 기반 개발 방법 (TDD) 적용을 위한 아래의 작업 진행
PC에 nodejs 및 npm 이 설치 되어있어야 한다.
```
npm init --yes #npm 초기화
npm install mocha@2.5.3 --save-dev
npm install mocha@5.0.3 --save-dev
```
* package.json 파일 부분 변경
```
"scripts": {
    "test": "node_modules/mocha/bin/mocha"
},
```
* mkdir test # touch test/helloworld_test.js
```
var Browser = require('zombie')
var assert = require('assert')
var app = require('../helloworld')

/*
  * localhost:3000 으로 접속하기전에 before 가로채기 함수를 사용하여 
  it 호출하는 코드앞에 헤드리스 부라우저가 적절한 서버를 가리키도록 설정
*/
describe('main page', function() { 
  before(function() {
    this.browser = new Browser({ site: 'http://localhost:3000' })
  })
  before(function(done) {
    this.browser.visit('/', done)
  })
  it('should say hello world', function() { 
    assert.ok(this.browser.success)
    assert.equal(this.browser.text(), "Hello World")
  })
})
```
* 테스트 && 테스트 확인
```
npm test
#helloworld.js 파일을 업데이트 하고 테스트 해당 파일은 helloworld repo
npm test
```

* jenkins 파이브라인 생성
1. 일반적으로 웹페이지를통한 생성이 아닌, helloworld repo에 있는 jenkinsfile-J 를 생성하여 아래와 같이 입력.
```
#!groovy 

node {
   stage 'Checkout'
        checkout scm

   stage 'Setup'
        sh 'npm install'

   stage 'Mocha test'
        sh './node_modules/mocha/bin/mocha'

   stage 'Cleanup'
        echo 'prune and cleanup'
        sh 'npm prune'
        sh 'rm node_modules -rf'
}
```
* github add / commit / push
* 이후 jenkisn 서버 에서의 nodejs 버전업그레이드 작업
```
sudo -i
yum remove nodejs -y
curl --silent --lication https://rpm.nodesource.com/setup_6.x | bash -
yum -y install nodejs
```
* jenkisn 오류 발생시
```
cd /var/lib/jenkins/workspace/깃주소-hellowrld-master-**
sudo rm -f node_modules
```
* 이후 아래와 같이 github 에서 진행
1. 브라우저 깃허브 접속 helloworld repo 이동
2. 브랜치 클릭 initial-branch
3. New pull request 클릭 @ 사용자 지정
4. Create pull request 진행
5. 파이프라인 설정이 되어야 하며, 통합 이슈가 없어야 한다.
6. jenkins 들어가서 빌드 진행 내용확인.