#include "priority_queue.h"
#include <algorithm>
#include <iostream>

using namespace std;

/*=========================
        HEAPIFY UP
=========================*/

void PriorityQueue::heapifyUp(int index)
{
    while(index > 0)
    {
        int parent = (index - 1) / 2;

        if(heap[parent].priorityScore >= heap[index].priorityScore)
            break;

        swap(heap[parent], heap[index]);

        index = parent;
    }
}

/*=========================
      HEAPIFY DOWN
=========================*/

void PriorityQueue::heapifyDown(int index)
{
    int size = heap.size();

    while(true)
    {
        int left = 2 * index + 1;
        int right = 2 * index + 2;

        int largest = index;

        if(left < size &&
           heap[left].priorityScore > heap[largest].priorityScore)
        {
            largest = left;
        }

        if(right < size &&
           heap[right].priorityScore > heap[largest].priorityScore)
        {
            largest = right;
        }

        if(largest == index)
            break;

        swap(heap[index], heap[largest]);

        index = largest;
    }
}

/*=========================
        INSERT
=========================*/

void PriorityQueue::insert(Task task)
{
    heap.push_back(task);

    heapifyUp(heap.size() - 1);
}

/*=========================
      EXTRACT MAX
=========================*/

Task PriorityQueue::extractMax()
{
    if(heap.empty())
    {
        cout << "Priority Queue Empty!" << endl;

        return Task();
    }

    Task highest = heap[0];

    heap[0] = heap.back();

    heap.pop_back();

    if(!heap.empty())
        heapifyDown(0);

    return highest;
}

/*=========================
         PEEK
=========================*/

Task PriorityQueue::peek()
{
    if(heap.empty())
        return Task();

    return heap[0];
}

/*=========================
        EMPTY?
=========================*/

bool PriorityQueue::isEmpty()
{
    return heap.empty();
}

/*=========================
         SIZE
=========================*/

int PriorityQueue::size()
{
    return heap.size();
}

/*=========================
        DISPLAY
=========================*/

void PriorityQueue::display()
{
    cout << "\n========= Priority Queue =========\n";

    for(Task task : heap)
    {
        cout << "Task : " << task.taskName << endl;

        cout << "Subject : " << task.subject << endl;

        cout << "Priority : "
             << task.priorityScore << endl;

        cout << "Deadline : "
             << task.deadline << endl;

        cout << "Estimated Time : "
             << task.estimatedTime << " mins" << endl;

        cout << "-----------------------------" << endl;
    }

    cout << endl;
}