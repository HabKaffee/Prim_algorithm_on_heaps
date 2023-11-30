#ifndef BINARY_HEAP_H
#define BINARY_HEAP_H

#include <algorithm>
#include <cmath>
#include <functional>
#include <queue>
#include <vector>

#include "Graph.h"

class GraphNode;

class BinaryHeap {
private:
  std::vector<GraphNode *> heap;
  bool isMaxHeap;
  std::function<bool(int a, int b)> compareNodes(int firstNode, int secondNode);

public:
  BinaryHeap() = default;
  BinaryHeap(std::vector<GraphNode *> graph, bool isMaxHeap = true);
  ~BinaryHeap() = default;

  std::vector<GraphNode *> getHeap();

  bool isHeapCorrect();
  GraphNode *returnMax();
  GraphNode *returnMin();

  void insertElement(GraphNode *element);

  void siftUp(int idx);
  void siftDown(int idx);

  bool search(GraphNode *target);

  void extractRoot();
  void deleteElement(int idx);

  void increaseKey(int idx, int newKey);
  void decreaseKey(int idx, int newKey);
};

#endif // BINARY_HEAP_H