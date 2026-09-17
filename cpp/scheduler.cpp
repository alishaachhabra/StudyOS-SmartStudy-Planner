#include "scheduler.h"
#include <iostream>

using namespace std;

/*=============================
      CALCULATE PRIORITY
=============================*/

int Scheduler::calculatePriority(Task &task)
{
    int score = 0;

    // Importance (Highest Weight)
    score += task.importance * 30;

    // Mandatory Task
    if(task.mandatory)
        score += 40;

    // Estimated Time
    if(task.estimatedTime <= 60)
        score += 20;
    else if(task.estimatedTime <= 120)
        score += 10;

    return score;
}

/*=============================
        LOAD TASKS
=============================*/

void Scheduler::loadTasks(vector<Task> tasks)
{
    while(!pq.isEmpty())
        pq.extractMax();

    for(Task task : tasks)
    {
        task.priorityScore = calculatePriority(task);

        pq.insert(task);
    }
}

/*=============================
    GENERATE STUDY PLAN
=============================*/

vector<Task> Scheduler::generateStudyPlan(int availableTime)
{
    vector<Task> plan;

    int usedTime = 0;

    while(!pq.isEmpty())
    {
        Task current = pq.extractMax();

        if(usedTime + current.estimatedTime <= availableTime)
        {
            plan.push_back(current);

            usedTime += current.estimatedTime;
        }
    }

    return plan;
}