# Matplotlib

## Anatomy of Figure
`matplotlib`을 사용하다보면, 기본적인 레이아웃에 대해서 반복적으로 찾아보는 경우들이 많아진다. 좋은 그래프(좋은 시각화 자료) 제작을 위해서는 각 부분의 명칭을 알아두고 이를 편집할 수 있으면 정말 유용하다. [~~사실 본 위키는 필자의 시간을 낭비하지 않기 위한 정리글 이기도 하다~~]  

<p align="center"><img src="https://user-images.githubusercontent.com/50191848/156300508-f40ab857-f3fa-4816-bb31-a44430787c92.png" alt="anatomy of figure" width="50%" height="50%"></p> 

## Figure
- 그래프를 그리는 창을 의미함
- 그림 그리는 걸 비유하면, 캔버스를 정의하는 부분

## Axes
- 창 내부에 그래프를 그리는 공간을 의미함
- 창 안에는 여러개의 그래프를 그리기 위해서는, 각 그래프 별 공간을 정의해줘야한다. 하나의 공간에 여러개의 그래프를 그릴 수도 있지만, 하나의 창에 여러개의 그래프를 각각 따로 그려야할 경우도 있기에 본 기능을 이해해두면 좋음

## Major and minor tick
- 각 축(x축, y축, ...)에서 일정 간격을 나타내는 부분
- 일정한 큰 간격을 표시한 것을 `major tick`, 큰 간격을 다시 일정한 간격으로 나눈 것을 `minor tick`이라고 부름
- 각 축의 값을 나타내고 그 값을 설정하는 옵션이 `major tick label`, `minor tick label`

## Grid
- 그려진 그래프 위의 값들을 이해하기 쉽도록 그려놓은 보조선
- 각 축에서 수평 혹은 수직하게 그려진는 축으로 보통 `major tick`으로부터 그어짐

## Spine
- 각 축을 나타내는 선들의 옵션을 설정하는 기능
- 축을 보여줄 수도 있고, 안보이게 조정할 수도 있음

## Legend
- axes에 그려진 그래프들의 범례를 나타내는 부분
- legend의 세부사항들을 조정할 수 있음

## Reference
[matplotlib](https://matplotlib.org/3.1.1/gallery/showcase/anatomy.html)