#include "graph.h"
#include <queue>

using namespace std;

/*=========================
      ADD SUBJECT
=========================*/

void Graph::addSubject(string subject)
{
    adjList[subject];
}

/*=========================
    ADD DEPENDENCY
=========================*/

void Graph::addDependency(
    string subject,
    string prerequisite
)
{
    adjList[prerequisite].push_back(subject);
}

/*=========================
      DISPLAY GRAPH
=========================*/

void Graph::display()
{
    cout << "\n======= SUBJECT GRAPH =======\n\n";

    for(auto node : adjList)
    {
        cout << node.first << " -> ";

        for(string child : node.second)
            cout << child << " ";

        cout << endl;
    }
}

/*=========================
      DFS HELPER
=========================*/

void Graph::DFSHelper(
    string node,
    unordered_map<string,bool>& visited
)
{
    visited[node]=true;

    cout << node << endl;

    for(string neighbour : adjList[node])
    {
        if(!visited[neighbour])
            DFSHelper(neighbour,visited);
    }
}

/*=========================
          DFS
=========================*/

void Graph::DFS(string start)
{
    unordered_map<string,bool> visited;

    DFSHelper(start,visited);
}

/*=========================
          BFS
=========================*/

void Graph::BFS(string start)
{
    unordered_map<string,bool> visited;

    queue<string> q;

    visited[start]=true;

    q.push(start);

    while(!q.empty())
    {
        string current=q.front();

        q.pop();

        cout << current << endl;

        for(string neighbour : adjList[current])
        {
            if(!visited[neighbour])
            {
                visited[neighbour]=true;

                q.push(neighbour);
            }
        }
    }
}