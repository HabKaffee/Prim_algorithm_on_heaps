#include "../include/binaryHeap.h"

BinaryHeap::BinaryHeap(std::vector<GraphNode *> graph, bool isMaxHeap) {
  this->heap = graph;
  this->isMaxHeap = isMaxHeap;
  // if we have Max Heap then we should perform siftdown
  if (this->isMaxHeap)
    for (int i = this->heap.size() / 2; i >= 0; --i) {
      siftDown(i);
    }
  // Otherwise siftup (because Min Heap)
  else {
    for (int i = this->heap.size() / 2; i >= 0; --i) {
      siftUp(i);
    }
  }
}

std::function<bool(int a, int b)> BinaryHeap::compareNodes(int firstNode,
                                                           int secondNode) {
  if (this->isMaxHeap) {
    return std::greater<int>();
  }
  return std::less<int>();
}

std::vector<GraphNode *> BinaryHeap::getHeap() { return this->heap; }

bool BinaryHeap::isHeapCorrect() {
  std::queue<int> indexQueue;
  indexQueue.push(0);

  int heapSize = this->heap.size();

  while (!indexQueue.empty()) {
    int parent = indexQueue.front();
    indexQueue.pop();
    int leftChild = 2 * parent + 1;
    int rightChild = 2 * parent + 2;
    if (leftChild < heapSize) {
      indexQueue.push(leftChild);
    }
    if (rightChild < heapSize) {
      indexQueue.push(rightChild);
    }
    // If child index is out of range that means that we are looking at leaf
    // node
    bool leftCorrect = (leftChild >= heapSize) ||
                       compareNodes(this->heap[parent]->getValue(),
                                    this->heap[leftChild]->getValue());
    bool rightCorrect = (rightChild >= heapSize) ||
                        compareNodes(this->heap[parent]->getValue(),
                                     this->heap[rightChild]->getValue());
    if (!leftCorrect || !rightCorrect) {
      return false;
    }
  }
  return true;
}

void BinaryHeap::insertElement(GraphNode *element) {
  this->heap.push_back(element);

  int insertedElementIndex = this->heap.size() - 1;
  siftUp(insertedElementIndex);
}

void BinaryHeap::siftUp(int idx) {
  int parentIndex = (idx - 1) / 2;
  while (compareNodes(this->heap[idx]->getValue(),
                      this->heap[parentIndex]->getValue())) {
    std::swap(this->heap[idx], this->heap[parentIndex]);
    idx = parentIndex;
    parentIndex = (idx - 1) / 2;
  }
}
void BinaryHeap::siftDown(int idx) {
  while (2 * idx + 1 < this->heap.size()) {
    int leftChild = 2 * idx + 1;
    int rightChild = 2 * idx + 2;
    int neededChild =
        (rightChild < this->heap.size() && compareNodes(leftChild, rightChild))
            ? rightChild
            : leftChild;
    if (compareNodes(this->heap[idx]->getValue(),
                     this->heap[leftChild]->getValue()) &&
        compareNodes(this->heap[idx]->getValue(),
                     this->heap[rightChild]->getValue())) {
      break;
    }

    std::swap(this->heap[idx], this->heap[neededChild]);
    idx = neededChild;
  }
}

bool BinaryHeap::search(GraphNode *target) {}

void BinaryHeap::deleteElement(int idx) {}

void BinaryHeap::increaseKey(int idx, int newKey) {}
void BinaryHeap::decreaseKey(int idx, int newKey) {}

GraphNode *BinaryHeap::returnMax() {
  if (this->isMaxHeap) {
    return this->heap[0];
  }
  return *std::max_element(this->heap.begin(), this->heap.end(),
                           [&](std::pair<GraphNode *, dist_t> first,
                               std::pair<GraphNode *, dist_t> second) {
                             return first.first->getValue() >
                                    second.first->getValue();
                           });
}

GraphNode *BinaryHeap::returnMin() {
  if (!this->isMaxHeap) {
    return this->heap[0];
  }
  return *std::min_element(this->heap.begin(), this->heap.end(),
                           [&](std::pair<GraphNode *, dist_t> first,
                               std::pair<GraphNode *, dist_t> second) {
                             return first.first->getValue() <
                                    second.first->getValue();
                           });
}