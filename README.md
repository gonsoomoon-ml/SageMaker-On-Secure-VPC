# Secure VPC에서 SageMaker 워크샵

---
# 전체 컨셉 구성도 (아래 워크샵 시나리오와 같이 보세요)
![secureVPC-demo1](img/secureVPC-demo1.png)


# 워크샵 시나리오
- 두개의 리젼에서 ML 워크로드가 실행이 됩니다.
    - 서울 리젼: No VPC 환경으로 On-premise환경을 가정하였습니다.
        - 데이타를 준비, 모델 빌딩, 모델 훈련 및 모델 배포 및 추론을 합니다.
        - 이후에 문제가 없다면, S3에 사용한 데이터 및 코드를 업로드 합니다.
    - 오리건 리젼: Secure VPC (인터넷 안됨) 환경으로 아래와 같은 작업을 합니다.
        - **[가정] 오리건 리젼에 Secure VPC가 이미 설치되었다고 가정 합니다.**
        - S3 에서 코드를 다운로드 합니다.
        - 모델 훈련을 합니다. 입력데이터의 위치는 S3 입니다.
            - 모델 훈련의 결과인 모델 아티펙트는 S3에 저장이 되어서, 이를 S3에 다운로드해서 On-premise에서 사용합니다.
        - 모델을 배포하고 추론합니다.
            - 데이터를 S3에서 다운로드를 하여 사용합니다.
            
---
## VPC 구성
### 실행 환경
* macOS 또는 Linux
* Python3
* AWS CDK (Cloud Development Kit)

### AWS CDK 설치
CDK 앱을 생성하고 관리하는 경우 AWS CDK CLI(명령줄 인터페이스)를 사용할 수 있습니다. 이 도구는 다음과 같이 빠르게 설치할 수 있습니다.
```
$ npm install -g aws-cdk
```

#### AWS 자격증명
[구성 및 자격 증명 파일 설정](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/cli-configure-files.html)의 내용을 참고하여 AWS CDK를 수행할 준비를 합니다. 자격 증명 키를 터미널 환경 변수에 등록하거나 설정 파일에 저장하여 CDK가 적절하게 AWS 자원을 생성할 수 있도록 만들어 주어야합니다.

### AWS CDK 실행
먼저, CDK를 실행할 수 있는 디렉토리로 이동합니다. 그리고 VPC를 생성하는 코드를 실행합니다. 스크립트 안에서 Python 가상환경, 의존성 설치, CDK 실행을 수행합니다. 작업이 완료되면 VPC와 VPC Endpoint들, VPC Peering이 생성됩니다.
```
$ cd aws-cdk/python/vpc
$ bash launch.sh
```

## 노트북(코드) 구성
아래왁 같이 순서대로 실행 하시면 됩니다.
#### NoVPC Side (예: 서울 리젼)
- 1.1.NoVPC-Prepare-Data.ipynb
    - [옵션] 2.0.NoVPC-Build-Model.ipynb
- 2.1.NoVPC-Train-Model.ipynb
- 3.1.ALL-Deploy_Model.ipynb
- 4.1.NoVPC-Upload-Data-Code.ipynb

#### VPC Side(에: 오리건 리젼)
- 9.0.VPC-Download-Code.ipynb
- 2.1.VPC-Train-Model.ipynb
- 3.1.ALL-Deploy_Model.ipynb

## VPC 제거
### AWS CDK 실행
```
$ cd aws-cdk/python/vpc
$ bash cleanup.sh
```
