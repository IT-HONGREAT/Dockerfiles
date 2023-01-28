# fastapi basic

* 변경사항 미적용시
  * `--no-cache` 적용해보기
  

### docker build process == layer 쌓는 방식
`docker build ~` for Dockerfile

1. 임시 컨테이너 생성 
2. 명령어 수행 (running) 
3. 이미지로 저장 
4. 임시 컨테이너 삭제 //
5. 새로 만든 이미지 기반 임시 컨테이너 생성 
6. 명령어 수행 
7. 이미지로 저장 
8. 임시 컨테이너 삭제 //


**1~8 과정을 반복 하면서 layer를 쌓는다.**

---
- todo
  - [ ] docker CI/CD
### docker CI/CD

- [ ] https://subicura.com/2016/06/07/zero-downtime-docker-deployment.html