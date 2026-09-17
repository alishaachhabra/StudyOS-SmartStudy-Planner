#ifndef GRAPH_H
#define GRAPH_H

#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Graph
{
private:

    unordered_map<string, vector<string>> adjList;

    void DFSHelper(
        string node,
        unordered_map<string,bool>& visited
    );

public:

    void addSubject(string subject);

    void addDependency(
        string subject,
        string prerequisite
    );

    void DFS(string start);

    void BFS(string start);

    void display();
};

#endif