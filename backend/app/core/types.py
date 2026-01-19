# chuyển tọa độ thành JSON để frontend sử dụng

from typing import Dict, List, TypedDict

class Point(TypedDict): # tọa độ 
    x: int
    y: int

class SelectedPoint(TypedDict):
    height: List[Point] # 2 điểm
    width: List[Point] # 2 điểm
    depth: List[Point] # 2 điểm

class TextPostions(TypedDict):
    height: Point
    width: Point
    depth: Point