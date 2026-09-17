#include <iostream>
#include <fstream>
#include <vector>

#include "task.h"
#include "scheduler.h"

using namespace std;

int main()
{
    ifstream fin("input.txt");

    ofstream fout("output.txt");

    if(!fin.is_open())
    {
        cout<<"Unable to open input.txt";

        return 0;
    }

    int n;

    fin>>n;

    vector<Task> tasks;

    for(int i=0;i<n;i++)
    {
        Task t;

        fin>>t.id;

        fin>>t.subject;

        fin>>t.taskName;

        fin>>t.deadline;

        fin>>t.estimatedTime;

        fin>>t.importance;

        fin>>t.mandatory;

        tasks.push_back(t);
    }

    int availableTime;

    fin>>availableTime;

    Scheduler scheduler;

    scheduler.loadTasks(tasks);

    vector<Task> plan =
        scheduler.generateStudyPlan(
            availableTime
        );

    fout<<plan.size()<<endl;

    for(Task task:plan)
    {
        fout
        <<task.id<<" "
        <<task.subject<<" "
        <<task.taskName<<" "
        <<task.deadline<<" "
        <<task.estimatedTime<<" "
        <<task.importance<<" "
        <<task.mandatory<<" "
        <<task.priorityScore
        <<endl;
    }

    fin.close();

    fout.close();

    return 0;
}