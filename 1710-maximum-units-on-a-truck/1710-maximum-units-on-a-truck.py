class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxes = []
        for box in sorted(boxTypes, key=lambda x: x[1], reverse=True):
            for bx in range(box[0]):
                boxes += [box[1]]
        
        return sum(boxes[0:truckSize])