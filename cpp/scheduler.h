#ifndef SCHEDULER_H
#define SCHEDULER_H

#include <vector>
#include "task.h"
#include "priority_queue.h"

using namespace std;

class Scheduler
{
private:

    PriorityQueue pq;

    int calculatePriority(Task &task);

public:

    void loadTasks(vector<Task> tasks);

    vector<Task> generateStudyPlan(int availableTime);

};

#endif