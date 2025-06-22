# EC2-Switch

파이썬을 사용하여 간단하게 ec2 인스턴스를 키고 끌 수 있는 간단한 어플리케이션 

## 주요기능
- Ec2 상태확인 : 켜져있는 지, 꺼져있는 지 확인
- 인스턴스 On-Off : 인스턴스를 키고 끌 수 있습니다.
- Tkinter를 사용한 gui, pyinstaller를 사용한 exe 배포 

## 실행방법
### 로컬에서 실행하기
- config_manager.py의 get_path가 os.getcwd를 사용하는데 os.getcwd가 src를 반환합니다.
- 따라서 config.json을 src 디렉토리 아래에 배치해야합니다
  - 주의 ) config.json은 주요한 AWS KEY값을 포함하므로 노출되지 않게 조심하십시오
### 실행파일 빌드하기
```bash
pyinstaller --onefile --noconsole --name="EC2_Switch" --paths=./src src/main.py
```
이후 exe 파일과 같은 위치에 config.json을 집어넣으십시오.

## config.json
- config.json의 schema은 다음과 같다. 

```json
{
  "AWS_ACCESS_KEY_ID" : "",
  "AWS_SECRET_ACCESS_KEY" : "",
  "AWS_DEFAULT_REGION" : "",
  "INSTANCE_ID" : ""
}
```
