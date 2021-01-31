//input:  memory size, reference string
//output : page fault count
		//disk write count
		//disk head moving distance


#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

struct PAGE {
	int memory_location; //physical memory address
	int valid_bit; //whether page exists in physical memory
}; struct PAGE page[200000];

struct MEMORY {
	int page_num;	//location of page in memory
	int reference_bit;	//0->1 when page is referenced
	int dirty_bit;		//0->1 when write 
};

int main(int argc, char* argv[]) {

	int page_fault = 0;
	int disk_write = 0;
	int head_mvmt = 0;

	int pg, op;
	int c_point = 0, head = 0;
	int memory_size = atoi(argv[1]);
	FILE* input_file = fopen("a.txt", "r");
	struct MEMORY* memory = (struct MEMORY*)malloc(memory_size * sizeof(struct MEMORY));

	for (int i = 0; i < memory_size; i++) { //initialize memory
		memory[i].reference_bit = 0;
		memory[i].dirty_bit = 0;
	}

	for (int i = 0; i < 200000; i++) page[i].valid_bit = 0; //initialize page
	while (!feof(input_file)) {
		//read page number and operation(read/write) from reference string
		fscanf(input_file, "%d %d", &pg, &op);
		if (page[pg].valid_bit == 1) {	//page already exists in memory
			memory[page[pg].memory_location].reference_bit = 1;	//set reference bit = 1;
			if (op == 1) memory[page[pg].memory_location].dirty_bit = 1;	//write operation -> set dirty_bit = 1
		}
		else {
			page_fault++; //increase num of page_fault
			if (page_fault > memory_size) {	//memory full
				while (memory[c_point].reference_bit != 0) {
					memory[c_point].reference_bit = 0;
					c_point = ((c_point + 1) % (memory_size));
				}
				page[memory[c_point].page_num].valid_bit = 0;//delete current page
				if (memory[c_point].dirty_bit == 1) {	//if there were disk write operation
					disk_write++;	//increase disc_write
					head_mvmt += abs((int)(memory[c_point].page_num / 1000) - head);	//increase head mvmt
					head = (int)(memory[c_point].page_num / 1000);	//update head
				}
				memory[c_point].dirty_bit = 0;
			}
			head_mvmt += abs((int)(pg / 1000) - head);	//increase head mvmt
			head = (int)(pg / 1000);	//update head
			memory[c_point].page_num = pg;	//insert new page 
			memory[c_point].reference_bit = 0;	//set reference bit = 0 for newly inserted page
			if (op == 1) memory[c_point].dirty_bit = 1;	//write operation -> set dirty_bit = 1
			page[pg].memory_location = c_point;	//set memory location of page
			page[pg].valid_bit = 1;	//set valid bit to 1
			c_point = ((c_point + 1) % (memory_size));
		}
	}
	printf("%d\n%d\n%d\n", page_fault, disk_write, head_mvmt);
}