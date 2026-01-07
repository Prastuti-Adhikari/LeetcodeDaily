# Question is: Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = hour % 12
        hour_angle = hour * 30 + minutes * 0.5
        minute_angle = minutes * 6
        angle = abs(hour_angle - minute_angle)
        if angle > 180:
            angle = 360 - angle
        return angle