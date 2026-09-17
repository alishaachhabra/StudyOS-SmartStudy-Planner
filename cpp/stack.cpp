#include "stack.h"
#include <iostream>

using namespace std;

/*=========================
        PUSH
=========================*/

void StudyStack::push(Task task)
{
    stack.push_back(task);
}

/*=========================
         POP
=========================*/

void StudyStack::pop()
{
    if(!stack.empty())
        stack.pop_back();
}

/*=========================
          TOP
=========================*/

Task StudyStack::top()
{
    if(stack.empty())
        return Task();

    return stack.back();
}

/*=========================
        EMPTY?
=========================*/

bool StudyStack::isEmpty()
{
    return stack.empty();
}

/*=========================
          SIZE
=========================*/

int StudyStack::size()
{
    return stack.size();
}

/*=========================
        DISPLAY
=========================*/

void StudyStack::display()
{
    cout << "\n======= RECENT TASKS =======\n\n";

    for(int i = stack.size() - 1; i >= 0; i--)
    {
        cout << stack[i].taskName
             << " ("
             << stack[i].subject
             << ")\n";
    }

    cout << endl;
}