# README

👀주의 사항👀

> git push origin master 하지  말것 !!!

### <git 관리 시나리오>

1.  git clone https://github.com/nate1994/algorithm.git
2.  git branch '자신의 영어이니셜 3글자' **ex) LSJ** 
3. git checkout '자신의 branch명' 
4. 자신의 이니셜에 맞는 폴더에서만 작성
5. git add '자신의 폴더명'
6. git commit
7. git  remote add portfolio(origin만 빼고 아무거나) 'git주소'   (개인 잔디심기 + 포트폴리오 주소로 연결해주세요)  
8. git push origin '자신의 branch명'  (😒 **절대 master 하면 안됩니다.... **)
9. git push portfolio master 



### 추가 내용들

밑에 있는 것들은 git하면서 필요한 명령어랑 branch 개념을 조금이나마 설명하기 위해서 작성 해봤습니다.





+)git 명령어 

[https://velog.io/@hidaehyunlee/Git-add-commit-push-%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0

- **브랜치의 목록을 볼 때**

  git branch

- **브랜치를 생성할 때** 

  git branch "새로운 브랜치 이름"  

- **브랜치를 삭제할 때**

  git branch -d

- **병합하지 않은 브랜치를 강제 삭제할 때** 

  git branch -D

- **브랜치를 전환(체크아웃)할 때**

  git checkout "전환하려는 브랜치 이름"

- **브랜치를 생성하고 전환까지 할 때** 

  git checkout -b "생성하고 전환할 브랜치 이름"





1. git init (master)
2.  a.txt 생성 -> 1 작성 
3.  git add a.txt-> git commit : master 버전에서는 1이 기록된다.
4.  git branch exp    (master)
   - git branch로 결과를 확인 

---



5. git checkout exp (exp)
   - exp 라는 브랜치로 전환
6. a.txt  - >  2를 추가로 수정  
7. git add a.txt -> git commit   
   - exp 버전에서는 1,2 가 적혀있는 것으로 기록



---



8. git checkout master (master)
   - master버전으로 다시 관리 하면서 a.txt 파일을 보면 1만 남아있는 것을 확인가능하다.





## git branch 정보 비교

- **브랜치 간에 비교할 때**

  ​	- git log "비교할 브랜치 명 1".."비교할 브랜치 명 2"

- **브랜치 간의 코드를 비교 할 때** 

  ​	- git diff "비교할 브랜치 명 1".."비교할 브랜치 명 2"

- **로그에 모든 브랜치를 표시하고, 그래프로 표현하고, 브랜치 명을 표시하고, 한줄로 표시할 때** 

  ​	- git log --branches --graph --decorate --oneline



```bash

d@DESKTOP-R6TL6SN MINGW64 ~/Desktop/gitbranch (master)
$ git log --branches --graph --decorate --oneline
* fee33e0 (b) 1 2 3
| * 2cfaf46 (a) 1 2
|/ # 의미 : log 1의 분기점으로 (a)와 (b)로 나뉘어졌다는 것을 확인가능
* 9015003 (HEAD -> master) 1


```

```bash
$ git log master..a
commit 2cfaf46f9c31b1933c4415990cd9da6725f599cb (a)
Author: nate1994 <nate199458@gmail.com>
Date:   Wed Aug 19 06:32:59 2020 +0900

    1 2

# a에는 있고 master에는 없는 것을 알려줌
# 반대로 적용 가능
$ git log a..master 
# master에는 있고 a에는 없는 것을 알려줌
```





## branch 병합하기

 **A 브랜치로 B 브랜치를 병합할 때 (A ← B)**

​	git checkout A
​	git merge B

ex) a 의 내용을 master에 병합하기

```bash
d@DESKTOP-R6TL6SN MINGW64 ~/Desktop/gitbranch (master)
$ git merge a
Updating 9015003..2cfaf46
Fast-forward
 git.txt | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

d@DESKTOP-R6TL6SN MINGW64 ~/Desktop/gitbranch (master)
$ git log
commit 2cfaf46f9c31b1933c4415990cd9da6725f599cb (HEAD -> master, a)
Author: nate1994 <nate199458@gmail.com>
Date:   Wed Aug 19 06:32:59 2020 +0900

    1 2

commit 9015003ad68071162c971f2fe6eaf425e152df20
Author: nate1994 <nate199458@gmail.com>
Date:   Wed Aug 19 06:32:09 2020 +0900

    1
```



#### merge 충돌의 경우

같은 파일의 같은 부분을 다르게 수정했을 때, 

-> CONFLICT 문구를 확인 가능하다

-> `git status` 를 통해 어떤 파일이 문제인지 확인이 가능



- 해결
  - 충돌난 부분을 수정 







## git stash 명령어 사용하기

https://gmlwjd9405.github.io/2018/05/18/git-stash.html

설명이 잘되어있기 때문에 이것을 보고 사용할것 







----

push 예시

```bash

d@DESKTOP-R6TL6SN MINGW64 ~/Desktop/gitbranch
$ git init
Initialized empty Git repository in C:/Users/d/Desktop/gitbranch/.git/

d@DESKTOP-R6TL6SN MINGW64 ~/Desktop/gitbranch (master)
$ git remote add origin https://github.com/nate1994/branchpractice.git

d@DESKTOP-R6TL6SN MINGW64 ~/Desktop/gitbranch (master)
$ git add .

d@DESKTOP-R6TL6SN MINGW64 ~/Desktop/gitbranch (master)
$ git commit -m '1'
[master (root-commit) fc5cadd] 1
 1 file changed, 1 insertion(+)
 create mode 100644 a/b.txt

d@DESKTOP-R6TL6SN MINGW64 ~/Desktop/gitbranch (master)
$ git push origin master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Writing objects: 100% (4/4), 235 bytes | 235.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/nate1994/branchpractice.git
 * [new branch]      master -> master

d@DESKTOP-R6TL6SN MINGW64 ~/Desktop/gitbranch (master)
$ git checkout -b a
Switched to a new branch 'a'

d@DESKTOP-R6TL6SN MINGW64 ~/Desktop/gitbranch (a)
$ git add .

d@DESKTOP-R6TL6SN MINGW64 ~/Desktop/gitbranch (a)
$ git commit -m '2'
[a 2c4cd9a] 2
 1 file changed, 1 insertion(+)
 create mode 100644 b/c.txt

d@DESKTOP-R6TL6SN MINGW64 ~/Desktop/gitbranch (a)
$ git log
commit 2c4cd9a58fff9f21d315f23e1c63ad75419859f4 (HEAD -> a)
Author: nate1994 <nate199458@gmail.com>
Date:   Wed Aug 19 08:09:21 2020 +0900

    2

commit fc5cadd1f5c3ea367bc68167430ab5d8d70b3f90 (origin/master, master)
Author: nate1994 <nate199458@gmail.com>
Date:   Wed Aug 19 08:07:41 2020 +0900

    1

d@DESKTOP-R6TL6SN MINGW64 ~/Desktop/gitbranch (a)
$ git push origin a
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 6 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (4/4), 289 bytes | 289.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'a' on GitHub by visiting:
remote:      https://github.com/nate1994/branchpractice/pull/new/a
remote:
To https://github.com/nate1994/branchpractice.git
 * [new branch]      a -> a

```

