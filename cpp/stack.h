#ifndef STUDY_STACK_H
#define STUDY_STACK_H

#include <vector>
#include "task.h"

using namespace std;

class StudyStack
{
private:

    vector<Task> stack;

public:

    void push(Task task);

    void pop();

    Task top();

    bool isEmpty();

    int size();

    void display();
};

#endif