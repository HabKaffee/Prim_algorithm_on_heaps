#ifndef BINARY_HEAP_H
#define BINARY_HEAP_H

#include <algorithm>
#include <vector>

#include "Graph.h"

class GraphNode;

class BinaryHeap {
private:
  std::vector<GraphNode*> heap;
  bool isMaxHeap;

public:
  BinaryHeap() = default;
  BinaryHeap(std::vector<GraphNode*> graph, bool isMaxHeap = true);
  ~BinaryHeap() = default;
  
  std::vector<GraphNode*> getHeap();

  bool isHeapCorrect();
  GraphNode* returnMax();
  GraphNode* returnMin();

  void insertElement(GraphNode* element);

  void siftUp(int idx);
  void siftDown(int idx);

  bool search(GraphNode* target);
   
  void deleteElement(int idx);
  
  void increaseKey(int idx, int newKey);
  void decreaseKey(int idx, int newKey);
};

#endif // BINARY_HEAP_H