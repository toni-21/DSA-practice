import 'dart:math';

int largestPrime(int number) {
  int divisor = 2;
  while (number > 1) {
    if (number % divisor == 0) {
      number ~/= divisor;
    } else {
      divisor++;
    }
  }
  return divisor;
}

int diagonalPrime(List<List<int>> nums) {
  int largest = 0;
  for (int i = 0; i < nums.length; i++) {
    int leftDiagonal = nums[i][i];
    int rightDiagonal = nums[i][nums.length - 1 - i];

    if (checkPrime(leftDiagonal)) {
      largest = max(leftDiagonal, largest);
    }

    if (checkPrime(rightDiagonal)) {
      largest = max(rightDiagonal, largest);
    }
  }
  return largest;
}

bool checkPrime(int num) {
  int count  = 0;
  if(num < 2){
    return false;
  }
  for (int i = 1; i*i <= num; i++) {
    if(num % i == 0){
      count += 2;
    }
  }
  return count == 2;
}

int main() {
  const nums = [
    [1, 2, 3],
    [5, 6, 7],
    [19, 10, 11]
  ];
  // int answer = largestPrime(number);
  // print('Largest Prime Number of $number is $answer');
  int answer = diagonalPrime(nums);
  print('answer is $answer');
  return 0;
}
