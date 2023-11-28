#include <iostream>
#include <stack>
using namespace std;
int main()
{
    stack<int> myStack;

    // Push elements onto the stack
    myStack.push(1);
    myStack.push(2);
    myStack.push(3);

    // Print the top element of the stack
    cout << "Top element of the stack: " << myStack.top() <<endl;

    // Pop elements from the stack
    myStack.pop();
    // Check if the stack is empty
    if (myStack.empty())
    {
        cout << "Stack is empty." << endl;
    }
    else
    {
        cout << "Stack is not empty." << endl;
    }

    return 0;
}
