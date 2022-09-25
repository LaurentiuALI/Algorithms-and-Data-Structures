#include "node.h"

class circular_list{
private:
    node* head;
    node* last;
    int length;
public:
    circular_list();
    void add_node(int new_node);
    void display_list() const;
    void delete_from_list(int new_node);
    void set_head_position(int position);
    void josephus(int position, int skipping);
};
