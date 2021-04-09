
# 30. 내가 만든 스크립트를 다른 경로에서 불러오기(해결)

import sys              # 시스템과 관련된 모듈
#print(sys.path)         # sys.path 는 파이썬 모듈할 수 있는 경로들 저장한 리스트

sys.path.append("D:\\Python\\kg_workspace\\1_Pycode\\day19")        # 경로들어가서 복사 붙여넣기. 역슬래시 하나씩 더 추가
# sys.path.append("경로추가")는 모듈할 경로를 직접 추가해서 저장
print(sys.path)     # 경로 생긴것 확인 할 수 있음

import day19_실습