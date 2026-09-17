#ifndef TASK_H
#define TASK_H

#include <iostream>
#include <string>

using namespace std;

struct Task
{
    int id;

    string subject;

    string taskName;

    string deadline;

    int estimatedTime;

    int importance;

    bool mandatory;

    int priorityScore;

    string status;

    // Default Constructor
    Task()
    {
        id = 0;
        subject = "";
        taskName = "";
        deadline = "";
        estimatedTime = 0;
        importance = 0;
        mandatory = false;
        priorityScore = 0;
        status = "Pending";
    }

    // Parameterized Constructor
    Task(
        int id,
        string subject,
        string taskName,
        string deadline,
        int estimatedTime,
        int importance,
        bool mandatory,
        string status = "Pending"
    )
    {
        this->id = id;
        this->subject = subject;
        this->taskName = taskName;
        this->deadline = deadline;
        this->estimatedTime = estimatedTime;
        this->importance = importance;
        this->mandatory = mandatory;
        this->status = status;
        this->priorityScore = 0;
    }
};

#endif