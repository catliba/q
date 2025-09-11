# Non fast and slow pointer approach

def find(self, num):
    found_nums = set()
    curr_sum = self.num_sum(num)
    if curr_sum == 1:
      return True
    while curr_sum != 1:
      curr_sum = self.num_sum(curr_sum)
      if curr_sum in found_nums:
        return False
      else:
        found_nums.add(curr_sum)
    return True
  
# find the number equal to the sum of the square of all of its digits
def num_sum(self, num):
    num = str(num)
    sq_sum = 0
    for i in num:
      sq_sum += int(i)*int(i)
    return sq_sum

# fast and slow pointer approach
def find(self, num):
    slow, fast = num, num
    while True:
      slow = self.find_square_sum(slow)  # move one step
      fast = self.find_square_sum(self.find_square_sum(fast))  # move two steps
      if slow == fast:  # found the cycle
        break
    return slow == 1  # see if the cycle is stuck on the number '1'


def find_square_sum(self, num):
    _sum = 0
    while (num > 0):
      digit = num % 10
      _sum += digit * digit
      num //= 10
    return _sum