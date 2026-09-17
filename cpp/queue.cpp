#include "queue.h"
#include <iostream>

using namespace std;

StudyQueue::StudyQueue()
{
    frontIndex = 0;
}

void StudyQueue::enqueue(Task task)
{
    queue.push_back(task);
}

void StudyQueue::dequeue()
{
    if(!isEmpty())
        frontIndex++;
}

Task StudyQueue::front()
{
    if(isEmpty())
        return Task();

    return queue[frontIndex];
}

bool StudyQueue::isEmpty()
{
    return frontIndex >= queue.size();
}

int StudyQueue::size()
{
    return queue.size() - frontIndex;
}

void StudyQueue::display()
{
    cout << "\n===== TODAY'S STUDY QUEUE =====\n\n";

    for(int i = frontIndex; i < queue.size(); i++)
    {
        cout << queue[i].taskName
             << " ("
             << queue[i].subject
             << ")\n";
    }

    cout << endl;
}