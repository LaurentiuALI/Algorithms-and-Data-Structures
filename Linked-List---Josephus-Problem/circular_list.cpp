#include "circular_list.h"
#include <iostream>
circular_list::circular_list()
{
    head=nullptr;
    last=nullptr;
    length=0;
}
void circular_list::add_node(int new_node)
{
    if(this->head==nullptr)
    {
        head=last=new node(new_node);
        length++;
    }
    else{
        last->next= new node(new_node);
        last = last->next;
        last->next=head;
        length++;
    }
}
void circular_list::display_list() const
{
    if(last == nullptr)
        std::cout<<"List is empty";
    else{
    node* temp = head;
    for(int i = 0; i< length-1; i++)
    {
        std::cout<<temp->node_value<<" - ";
        temp=temp->next;
    }
    std::cout<<temp->node_value<<std::endl;
    }
}
void circular_list::delete_from_list(int new_node){
    if(last == nullptr)
        std::cout<<"List is empty";
    node* temp=head;
    if(new_node==head->node_value){
        head=head->next;
        last->next=head;
        length--;
    }
    else if(new_node==last->node_value){
        for(int i=0;i<length;i++)
            if( ( (temp->next) -> node_value ) == (last->node_value) ){
                last=temp;
                last->next=head;
                length--;
            }
            else
                temp=temp->next;

    }
    else{
        for(int i=0;i<length;i++){
            if ( (temp->next)->node_value == new_node ){
                temp->next=(temp->next)->next;
                length--;
            }
            else
                temp=temp->next;
        }
    }
}
void circular_list::set_head_position(int position) {
     while(head->node_value != position){
         last=head;
         head=head->next;
     }
}
void circular_list::josephus(int position, int skipping) {
    set_head_position(position);
    node *temp=head;
    while(length>1){
        display_list();
        for (int j = 0; j<skipping-1; j++) {
            temp=temp->next;
        }
        delete_from_list(temp->node_value);
        temp=temp->next;
    }
    std::cout<<"The surviving position is : "<< temp->node_value;
}