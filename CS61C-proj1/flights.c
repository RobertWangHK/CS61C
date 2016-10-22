/* 
 * CS61C Summer 2016
 * Name:
 * Login:
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "flights.h"
#include "timeHM.h"


airport_t* final;
schedule_t* _final;
schedule_t* _final_;

struct flightSys {
	struct airport *head;
};

struct airport {
	char* name; 
	struct airport * next;
	struct schedule *head;
};

struct schedule {
	char* destination;
	timeHM_t* departure;
	timeHM_t* arrival;
	int cost;
	struct schedule * next;
};
/*
   This should be called if memory allocation failed.
 */
static void allocation_failed() {
    fprintf(stderr, "Out of memory.\n");
    exit(EXIT_FAILURE);
}


/*
   Creates and initializes a flight system, which stores the flight schedules of several airports.
   Returns a pointer to the system created.
 */
flightSys_t* createSystem() {
    // Replace this line with your code
    flightSys_t *t = (flightSys_t*)malloc(sizeof(flightSys_t));
    if (t == NULL) {
	allocation_failed();
    }
    t->head = (airport_t*)malloc(sizeof(airport_t));
    
    //printf("%d", sizeof(t));
    return t;
    //return NULL;
}


/*
   Frees all memory associated with this system; that's all memory you dynamically allocated in your code.
 */
void deleteSystem(flightSys_t* s) {
//    airport_t *temp = (airport_t*)malloc(sizeof(airport_t));
//    while (s->head->next!=NULL){
//        temp=s->head;
//	s->head=s->head->next;
//        deleteAirport(temp);
//    }
    //deleteAirport(s->head);
//    free(s);
}

void deleteAirport(airport_t* s) {
//    schedule_t *temp = (schedule_t*)malloc(sizeof(schedule_t));
//    while (s->head->next!=NULL){
//        temp=s->head;
//	s->head=s->head->next;
//        free(temp);
//    }
    //deleteAirport(s->head);
//    free(s);
}



/*
   Adds a airport with the given name to the system. You must copy the string and store it.
   Do not store "name" (the pointer) as the contents it point to may change.
 */
void addAirport(flightSys_t* s, char* name) {
    airport_t *temp = (airport_t*)malloc(sizeof(airport_t));	
    if (temp == NULL) {
	allocation_failed();
    }
    temp->name = (char*)malloc(strlen(name));
    temp->head= (schedule_t*)malloc(sizeof(schedule_t));
    strcpy(temp->name, name);
    while (s->head->next!=NULL){
        s->head = s->head->next;
    }
    s->head->next = (airport_t*)malloc(sizeof(airport_t));
    memcpy(s->head->next,temp,sizeof(airport_t));
    free(temp);
}


/*
   Returns a pointer to the airport with the given name.
   If the airport doesn't exist, return NULL.
 */
airport_t* getAirport(flightSys_t* s, char* name) {
    final= (airport_t*)malloc(sizeof(airport_t));
    memcpy(final,s->head,sizeof(airport_t));
    while (final!= NULL) {
        if (strcmp(final->name,name)==0) {
	    return final;
        }
       final= final->next;
    }
    return NULL;
}


/*
   Print each airport name in the order they were added through addAirport, one on each line.
   Make sure to end with a new line. You should compare your output with the correct output
   in flights.out to make sure your formatting is correct.
 */
void printAirports(flightSys_t* s) {
    airport_t* temp = s->head;
    while (temp != NULL) {
        printf("%s\n", temp->name);
	temp = temp->next;
    }
}
/*
   Adds a flight to src's schedule, stating a flight will leave to dst at departure time and arrive at arrival time.
 */
void addFlight(airport_t* src, airport_t* dst, timeHM_t* departure, timeHM_t* arrival, int cost) {

    schedule_t *temp = (schedule_t*)malloc(sizeof(schedule_t));	
    if (temp == NULL) {
	allocation_failed();
    }
    temp->cost = cost;
    temp->destination= (char*)malloc(strlen(dst->name));
    temp->departure= (timeHM_t*)malloc(sizeof(timeHM_t));
    temp->arrival= (timeHM_t*)malloc(sizeof(timeHM_t));
    strcpy(temp->destination, dst->name);
    memcpy(temp->departure,departure,sizeof(timeHM_t));
    memcpy(temp->arrival,arrival,sizeof(timeHM_t));

    _final= (schedule_t*)malloc(sizeof(schedule_t));
    _final=src->head;
    while (_final->next!=NULL){
        _final = _final->next;
    }
    _final->next = (schedule_t*)malloc(sizeof(schedule_t));
    memcpy(_final->next,temp,sizeof(schedule_t));
    free(temp);
}


/*
   Prints the schedule of flights of the given airport.

   Prints the airport name on the first line, then prints a schedule entry on each 
   line that follows, with the format: "destination_name departure_time arrival_time $cost_of_flight".

   You should use printTime (look in timeHM.h) to print times, and the order should be the same as 
   the order they were added in through addFlight. Make sure to end with a new line.
   You should compare your output with the correct output in flights.out to make sure your formatting is correct.
 */
void printSchedule(airport_t* s) {
    printf("%s\n", s->name);
    _final= (schedule_t*)malloc(sizeof(schedule_t));
    _final=s->head;
    while(_final->next!=NULL){
        _final=_final->next;
	printf("%s ", _final->destination);
	printTime(_final->departure);
	printf(" ");
	printTime(_final->arrival);
	printf(" $%d\n", _final->cost);
    }
}

/*
   Given a src and dst airport, and the time now, finds the next flight to take based on the following rules:
   1) Finds the cheapest flight from src to dst that departs after now.
   2) If there are multiple cheapest flights, take the one that arrives the earliest.

   If a flight is found, you should store the flight's departure time, arrival time, and cost in departure, arrival, 
   and cost params and return true. Otherwise, return false. 

   Please use the function isAfter() from time.h when comparing two timeHM_t objects.
 */
bool getNextFlight(airport_t* src, airport_t* dst, timeHM_t* now, timeHM_t* departure, timeHM_t* arrival, int* cost) {
    int cheapest = 99999;
    _final= (schedule_t*)malloc(sizeof(schedule_t));
    _final_= (schedule_t*)malloc(sizeof(schedule_t));
    timeHM_t* best_arrival = (timeHM_t*)malloc(sizeof(timeHM_t));
    timeHM_t* best_departure = (timeHM_t*)malloc(sizeof(timeHM_t));
    _final=src->head;
    while(_final->next!=NULL){
	_final = _final->next;
        if(isAfter(_final->departure,now)&&strcmp(_final->destination,dst->name)==0){
	    if(cheapest>_final->cost){
                cheapest = _final->cost;
		memcpy(best_arrival,_final->arrival,sizeof(timeHM_t));
		memcpy(best_departure,_final->departure,sizeof(timeHM_t));  
	    }
        }
    }
    if(cheapest==99999){
	return false;
    }
    _final=src->head;
    while(_final->next!=NULL){
	_final = _final->next;
        if(_final->cost==cheapest){
	    if(isAfter(best_arrival,_final->arrival)&&strcmp(_final->destination,dst->name)==0){
	        cheapest = _final->cost;
		memcpy(best_arrival,_final->arrival,sizeof(timeHM_t));
		memcpy(best_departure,_final->departure,sizeof(timeHM_t));            
	    }               
	    }
    }
    memcpy(departure,best_departure,sizeof(timeHM_t));
    memcpy(arrival,best_arrival,sizeof(timeHM_t));
    memcpy(cost,&cheapest,sizeof(int));
    return true;
}
