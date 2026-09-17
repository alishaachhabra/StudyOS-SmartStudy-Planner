#include <iostream>
#include <vector>

#include "task.h"
#include "scheduler.h"

using namespace std;

int main()
{
    Scheduler scheduler;

    vector<Task> tasks;

    tasks.push_back(
        Task(
            1,
            "DSA",
            "Heap Assignment",
            "2026-07-12",
            90,
            3,
            true
        )
    );

    tasks.push_back(
        Task(
            2,
            "Python",
            "Flask Project",
            "2026-07-15",
            120,
            2,
            true
        )
    );

    tasks.push_back(
        Task(
            3,
            "DBMS",
            "Normalization",
            "2026-07-20",
            60,
            1,
            false
        )
    );

    scheduler.loadTasks(tasks);

    vector<Task> plan =
        scheduler.generateStudyPlan(240);

    cout << "\n========== STUDY PLAN ==========\n\n";

    for(Task task : plan)
    {
        cout << "Subject        : "
             << task.subject << endl;

        cout << "Task           : "
             << task.taskName << endl;

        cout << "Priority Score : "
             << task.priorityScore << endl;

        cout << "Study Time     : "
             << task.estimatedTime
             << " mins\n";

        cout << "----------------------------------\n";
    }

    return 0;
}