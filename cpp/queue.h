#ifndef STUDY_QUEUE_H
#define STUDY_QUEUE_H

#include <vector>
#include "task.h"

using namespace std;

class StudyQueue
{
private:

    vector<Task> queue;

    int frontIndex;

public:

    StudyQueue();

    void enqueue(Task task);

    void dequeue();

    Task front();

    bool isEmpty();

    int size();

    void display();
};

#endif