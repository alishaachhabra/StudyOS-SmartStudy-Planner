#ifndef PRIORITY_QUEUE_H
#define PRIORITY_QUEUE_H

#include <vector>
#include "task.h"

using namespace std;

class PriorityQueue
{
private:

    vector<Task> heap;

    void heapifyUp(int index);

    void heapifyDown(int index);

public:

    void insert(Task task);

    Task extractMax();

    Task peek();

    bool isEmpty();

    int size();

    void display();
};

#endif