#include "uthash.h"
#include <stdio.h>

typedef struct elem {
  int key;
  int value;
  UT_hash_handle hh;
} elem;

void incr(elem *search, elem *hashtbl, int key, int *max) {
  HASH_FIND_INT(hashtbl, &key, search);

  if (search != NULL) {
    search->value += 1;
    printf("key = %d with count %d\n", key, search->value);

    if (search->value > *max) {
      *max = search->value;
    }

  } else {
    elem *e = malloc(sizeof(elem));
    e->key = key;
    e->value = 1;
    HASH_ADD_INT(hashtbl, key, e);
  }
};

void clear_hashtbl(elem *hashtbl) {
  elem *curr, *tmp;

  for (curr = hashtbl; curr != NULL; curr = tmp) {
    tmp = curr->hh.next;
    HASH_DEL(hashtbl, curr);
    free(curr);
  }
}

int leastInterval(char *tasks, int tasksSize, int n) {

  if (tasksSize == 0) {
    return 0;
  }

  elem *counter = malloc(sizeof(elem));
  elem *search = malloc(sizeof(elem));
  int key;
  int *maxvl = malloc(sizeof(int));
  *maxvl = 1;

  for (int i = 0; i < tasksSize; i++) {
    key = tasks[i] - '0';
    incr(search, counter, key, maxvl);
  }

  int counts = 0;
  elem *s;

  for (s = counter; s != NULL; s = s->hh.next) {
    if (s->value == *maxvl) {
      counts += 1;
    }
  }

  int pauses = (*maxvl - 1) * (n + 1) + counts;
  clear_hashtbl(counter);
  clear_hashtbl(search);
  free(maxvl);
  return pauses > tasksSize ? pauses : tasksSize;
}