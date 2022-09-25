#include <iostream>
#include "circular_list.h"
circular_list l;
void display_message()
{
    std::cout << std::endl << std::endl << "1. Linked List." << std::endl;
    std::cout << "2. Josephus Problem." << std::endl;
    std::cout << "3. Exit." << std::endl;
}

void display_message_linked()
{
    std::cout << std::endl << "1. Display linked list." << std::endl;
    std::cout << "2. Add number to linked list." << std::endl;
    std::cout << "3. Delete number from linked list." << std::endl;
    std::cout << "4. Add the first n numbers to linked list." << std::endl;
    std::cout << "5. Exit" << std::endl;
}

void menu_linked(){
    int choice=0;
    display_message_linked();
    while(choice!=5)
    {
        std::cin>>choice;
        switch(choice)
        {
            case 1:
                l.display_list();
                display_message_linked();
                break;
            case 2:
                std::cout<<"Enter the value you wish to add to the list: ";
                int x;
                std::cin>>x;
                l.add_node(x);
                display_message_linked();
                break;
            case 3:
                std::cout<<"Enter the value you wish to delete from list: ";
                int y;
                std::cin>>y;
                l.delete_from_list(y);
                display_message_linked();
                break;
            case 4:
                std::cout<<"Enter the value for the n: ";
                int n;
                std::cin>>n;
                for(int i = 1; i <= n; i++)
                    l.add_node(i);
                display_message_linked();
                break;
            case 5:
                std::cout << "End of program." << std::endl;
                break;
            default:
                std::cout<<"Invalid choice... Please try again.";

        }
    }

}

void josephus(){
    int n;
    std::cout<<"Enter the number of prisoners:";
    std::cin>>n;
    std::cout<<std::endl;
    for(int i=1;i<=n;i++)
        l.add_node(i);
    int position, skip;
    std::cout<<"Enter the position you wish to start from:";
    std::cin>>position;
    std::cout<<std::endl;
    std::cout<<"Enter the position from where prisoners start to die (e.g. 1 mean prisoner no.1, 2 mean prisoner no. 2 etc): ";
    std::cin>>skip;
    std::cout<<std::endl;
    l.josephus(position,skip);
}

void menu_josephus() {
    int choice = 0;
    std::cout << "1. The classical problem. (41 prisoners, starting from position 1, every third element is eliminated."
              << std::endl;
    std::cout << "2. Custom problem." << std::endl;
    std::cout << "3. Exit." << std::endl;
    while (choice != 3) {
        std::cin >> choice;
        switch (choice) {
            case 1:
                for (int i = 1; i <= 41; i++)
                    l.add_node(i);
                l.josephus(1, 3);
                choice=3;
                break;
            case 2:
                josephus();
                choice=3;
                break;
            case 3:
                std::cout << "End of program." << std::endl;
                break;
            default:
                std::cout << "Invalid choice." << std::endl;
                break;

        }
    }
}

int main()
{
    int choice1;
    display_message();
    std::cin>>choice1;
    if(choice1==1)
    {
        menu_linked();
    }
    else if(choice1==2)
    {

        menu_josephus();
    }
    else if(choice1==3)
    {
        std::cout << "End of program." << std::endl;
    }
    return 0;
}