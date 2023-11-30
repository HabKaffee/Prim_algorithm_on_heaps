#include "../include/binaryHeap.h"

BinaryHeap::BinaryHeap(std::vector<GraphNode *> graph, bool isMaxHeap) {
  this->heap = graph;
  this->isMaxHeap = isMaxHeap;
  // if we have Max Heap then we should perform siftdown
  if (this->isMaxHeap)
    for (int i = this->heap.size() / 2; i >= 0; --i) {
      siftDown(i);
    }
  // Otherwise siftUp (because Min Heap)
  else {
    for (int i = this->heap.size() / 2; i >= 0; --i) {
      siftUp(i);
    }
  }
}

std::vector<GraphNode *> BinaryHeap::getHeap() { return this->heap; }

bool BinaryHeap::isHeapCorrect() {}

void BinaryHeap::insertElement(GraphNode *element) {}

void BinaryHeap::siftUp(int idx) {}
void BinaryHeap::siftDown(int idx) {}

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