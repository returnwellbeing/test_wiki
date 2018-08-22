# git wiki의 sidebar를 자동으로 생성해주는 스크립트

* git clone https://github.com/returnwellbeing/test_wiki.git

* cd test_wiki

* cp -R .githooks {path/to/your_wiki.git}/.githooks

* cd {path/to/your_wiki.git}

* git config core.hooksPath .githooks

* git commit 할때 마다 _Sidebar.md 내용을 업데이트 해준다
