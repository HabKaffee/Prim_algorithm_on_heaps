#ifndef BINARY_HEAP_H
#define BINARY_HEAP_H

#include <algorithm>
#include <vector>

class BinaryHeap {
private:
  std::vector<int> heap;
  bool isMaxHeap;

public:
  BinaryHeap() = default;
  BinaryHeap(std::vector<int> graph, bool isMaxHeap = true);
  ~BinaryHeap() = default;
  
  std::vector<int> getHeap();

  bool isHeapCorrect();
  int returnMax();
  int returnMin();

  void insertElement(int element);

  void siftUp(int idx);
  void siftDown(int idx);

  bool search(int target);
   
  void deleteElement(int idx);
  
  void increaseKey(int idx, int newKey);
  void decreaseKey(int idx, int newKey);
};

#endif // BINARY_HEAP_H