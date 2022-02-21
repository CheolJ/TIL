# pyinstaller

## What is pyinstaller
`python`이 없는 환경에서 `python` 기반으로 개발된 프로그램을 실행시키려고 할 때, 선택지가 몇가지 있는데, 그 중 하나가 `pyinstaller`이다. `pyinstaller`는 `python`이 없는 환경에서도 `python` 기반 프로그램이 실행시킬 수 있도록 `exe` 파일을 생성해주는 라이브러리이다.

## How to use?

1. 터미널[`pyinstaller`가 깔려있는 환경(혹은 가상환경)] 실행
2. `pyinstaller (file_name)` 코드 입력

쉬운 사용법이지만, 사용하면서 유용했던 점들을 아래 기술하였다.

```python
pyinstaller -F (file_name).py
```

`pyinstaller`를 사용하다보면 나는 `*.exe` 파일만 있으면 되는데, 정말 많은 파일들이 생성되는 것을 경험할 수 있다. 필자처럼 `*.exe` 파일만을 원한다면 `-F` 옵션을 통해 `*.exe` 파일만 생성하는 옵션을 선택하면 큰 도움이 될 것이다.
