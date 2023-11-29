#include "../include/binaryHeap.h"

BinaryHeap::BinaryHeap(std::vector<int> graph, bool isMaxHeap) {
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

std::vector<int> BinaryHeap::getHeap() { return this->heap; }

bool BinaryHeap::isHeapCorrect() {}

void BinaryHeap::insertElement(int element) {}

void BinaryHeap::siftUp(int idx) {}
void BinaryHeap::siftDown(int idx) {}

bool BinaryHeap::search(int target) {}

void BinaryHeap::deleteElement(int idx) {}

void BinaryHeap::increaseKey(int idx, int newKey) {}
void BinaryHeap::decreaseKey(int idx, int newKey) {}

int BinaryHeap::returnMax() {
  if (this->isMaxHeap) {
    return this->heap[0];
  }
  return *std::max_element(this->heap.begin(), this->heap.end());
}

int BinaryHeap::returnMin() {
  if (!this->isMaxHeap) {
    return this->heap[0];
  }
  return *std::min_element(this->heap.begin(), this->heap.end());
}