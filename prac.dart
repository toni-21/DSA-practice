int totalCost(arr) {
  arr.sort();
  int i = 0;
  int largest = arr[arr.length - 1];
  int cost = 0;

  while (i < arr.length - 1) {
    int left = arr[i];
    cost = cost + ((left + largest) / (largest - left + 1)).ceil();
    largest = left + largest;
    i++;
  }

  return cost;
}

getMinLength(String seq) {
  final List stack = [];
  for (int i = 0; i < seq.length; i++) {
    if (seq[i] == "A") {
      stack.add("A");
    } else {
      if (stack.isEmpty) {
        stack.add("B");
      } else {
        stack.removeLast();
      }
    }
  }
  return stack.length;
}

// getMinServers(
//   List<int> servers,
//   int expectedLoad,
// ) {
//   servers.sort((a, b) => b.compareTo(a)); // Sort servers in descending order
//   int count = 0;

//   for (int server in servers) {
//     while (expectedLoad >= server) {
//       if (expectedLoad == 0) return count;
//       expectedLoad -= server;
//       count++;
//     }
//   }
//   return count;
// }

int getMinServers(List<int> servers, int expectedLoad) {
  servers.sort((a, b) => b.compareTo(a)); // Sort servers in descending order
  int count = 0;
  print('init load is $expectedLoad');

  for (var i = 0; i < servers.length; i++) {
    int server = servers[i];
    if (expectedLoad >= server) {
      print('server is $server');
      if (expectedLoad == 0) return count;
      expectedLoad -= server;
      print('new load is $expectedLoad');
      count++;
    } else {
      break;
    }
  }

  print('load is $expectedLoad');
  if (expectedLoad > 0) {
    count++;
  }

  return expectedLoad == 0 ? count : -1;
}



int minServers(List<int> servers, int expectedLoad) {
  servers.sort((a, b) => b.compareTo(a)); // Sort servers in descending order
  double result = backtrack(servers, expectedLoad, 0, 0);
  return result == double.infinity ? -1 : result.toInt();
}

double backtrack(List<int> servers, int expectedLoad, int index, int count) {
  if (expectedLoad == 0) return count.toDouble();
  if (index == servers.length) return double.infinity;

  double minServers = double.infinity;
  for (int i = index; i < servers.length; i++) {
    if (servers[i] <= expectedLoad) {
      double res = backtrack(servers, expectedLoad - servers[i], i, count + 1);
      minServers = res < minServers ? res : minServers;
    }
  }
  return minServers;
}

int main() {
  List<int> servers = [5, 1, 1, 2, 4, 4]; // Example servers
  int expectedLoad = 10;
  int answer = getMinServers(servers, expectedLoad);

  print('answer is $answer');
  return 0;
}
