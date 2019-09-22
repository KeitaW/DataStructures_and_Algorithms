import pytest
from .main import Solution, Node

root = Node(val=1, left=Node(val=2, left=Node(val=4), right=Node(
    val=5)), right=Node(val=3, left=Node(val=6), right=Node(val=7)))
