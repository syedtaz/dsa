#include "uthash.h"

typedef struct elem {
  int key;
  int value;
  UT_hash_handle hh;
} elem;

void create_element(int key, int index, elem *el) {
  elem *e = malloc(sizeof(elem));
  e->key = key;
  e->value = index;
  memcpy(el, e, sizeof(elem));
}

void clear_hashtbl(elem *hashtbl) {
  elem *curr, *tmp;

  for (curr = hashtbl; curr != NULL; curr = tmp) {
    tmp = curr->hh.next;
    HASH_DEL(hashtbl, curr);
    free(curr);
  }
}

int *twoSum(int *nums, int numsSize, int target, int *returnSize) {
  elem *hashtbl = NULL;
  int *result = malloc(sizeof(int) * 2);
  elem *search = malloc(sizeof(elem));
  int diff;

  for (int i = 0; i < numsSize; i++) {
    diff = target - nums[i];
    HASH_FIND_INT(hashtbl, &diff, search);

    if (search != NULL) {
      result[0] = i;
      result[1] = search->value;
      clear_hashtbl(hashtbl);
      *returnSize = 2;
      return result;
    }

    elem *el = malloc(sizeof(elem));
    create_element(nums[i], i, el);
    HASH_ADD_INT(hashtbl, key, el);
  }

  clear_hashtbl(hashtbl);
  free(search);
  return result;
}