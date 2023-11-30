#include "include/Graph.h"

#include <iostream>

int main() {
    GraphNode* graph = new GraphNode(5);
    std::cout << graph->getValue() << std::endl;
    GraphNode* newNode = new GraphNode(2);
    graph->addNeighbour(newNode, 1);
    std::cout << graph->getNeighbours().size() << std::endl;
    graph->removeNeighbour(0);
    std::cout << graph->getNeighbours().size() << std::endl;\
    graph->addNeighbour(newNode, 1);
    std::cout << graph->getNeighbours().size() << std::endl;\
    graph->removeNeighbour(newNode);
    std::cout << graph->getNeighbours().size() << std::endl;\

    return 0;
}