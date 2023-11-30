#ifndef GRAPH_H
#define GRAPH_H

#include <algorithm>
#include <bits/stl_pair.h>
#include <cstdint>
#include <vector>

using dist_t = std::size_t;

class GraphNode {
private:
  int value;
  std::vector<std::pair<GraphNode *, dist_t>> neighbours;

public:
  GraphNode();
  GraphNode(int value) { this->value = value; }
  GraphNode(int value, std::vector<std::pair<GraphNode *, dist_t>> neighbours)
      : value(value), neighbours(neighbours) {}
  ~GraphNode() = default;
  
  int getValue() { return this->value; }
  std::vector<std::pair<GraphNode*, dist_t>> getNeighbours() {
    return this->neighbours;
  }
  void setValue(int newValue) {
    this->value = newValue;
  }
  void addNeighbour(GraphNode* neighbour, dist_t dist) {
    this->neighbours.push_back(std::pair<GraphNode*, dist_t>(neighbour, dist));
  }
  void removeNeighbour(int idx) {
    this->neighbours.erase(this->neighbours.begin() + idx);
  }
  void removeNeighbour(GraphNode* toRemove) {
    auto idx = std::find_if(this->neighbours.begin(), this->neighbours.end(), [&](std::pair<GraphNode*, dist_t> el) {
        return el.first == toRemove;
    });
    this->neighbours.erase(idx);
  }
};

#endif // GRAPH_H