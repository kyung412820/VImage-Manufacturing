<br>


# [VImage Manufacturing] 비디오, 이미지 가공, 업스케일링 툴

<br>

<h2>목차</h2>

 - [소개](#소개) 
 - [팀원](#팀원) 
 - [개발 환경](#개발-환경)
 - [사용 기술](#사용-기술)
 - [핵심 기능](#핵심-기능)
   - [업스케일링](#업스케일링)
   - [이미지 가공](#이미지 가공)
   - [비디오 이미지 분할](#비디오 이미지 분할)
 - [Trouble Shooting](#trouble-shooting)


## 소개

**VImage Manufacturing**는 필요에 따라 비디오의 아미지를 가공, 업스케일링 하는 프로그램입니다. 그린 스크린 에서 물체를 인식, 물체의 중심값을 기준으로 잡아 원하는 크기의 이미지로 가공, 배경제거, 원한다면 자신이 합성하고자 하는  배경과 합성하는 이미지 학습 모델을 위한 보조 툴 입니다.<br>

## 팀원

<table>
   <tr>
    <td align="center"><b><a href="https://github.com/kyung412820">이경훈</a></b></td>
  <tr>
    <td align="center"><a href="https://github.com/kyung412820"><img src="https://avatars.githubusercontent.com/u/71320521?v=4" width="100px" /></a></td>
  </tr>
  <tr>
    <td align="center"><b>프로젝트 총괄</b></td>
</table>


## 개발 환경

 - Windows
 - Visual Code
 - GitHub



## 사용 기술 

- Library & Framework : Numpy, cv, PIL, glob, subprocess, ffmpeg, os
- Language : Python



## 핵심 기능

### 업스케일링

- 업스케일링은 ffmpeg를 사용, valkan api를 이용하여 업스케일일을 진행
- 
  - 업스케일링은 코드상에서 자동을 진행하도록 파이썬에서 os.system으로 호출해서 진행하였습니다.


### 이미지 가공

- 이미지를 cv2로 인식, image.fromarray로 불러와 컬러 이미지로 코드를 진행하도록 했습니다.

- 이미지는 각 색의 따라 inrange로 물체만 잘라내었으며 색이 가장 많이 인식되는 열을 중간값으로 계산하여 자동으로 몰체의 중심이미지를 잘라내도록 구성했습니다.

  - 이미지를 가공하기 위해 cvtColor함수를 이용, hsv 색공간으로 변환했습니다.

- 가공이 완료된 이미지는 필요 여부에 따라 추가적으로 배경을 합성하거나 그대로 출력되어 저장되게 됩니다.


### 비디오 이미지 분할

- cv2.CAP_PROP_FRAME_COUNT로 비디오의 길이를 반환, 반환한 길이만큼 이미지를 imwrite하여 비디오를 이미지로 분할 하였습니다.


## Trouble Shooting

- 이미지를 불러오는 과정에서 흑백으로 불러와 데이터를 처리하는데 문제가 있었습니다
- 
  - 위와 같이 cvtColor함수로 해결했습니다.


