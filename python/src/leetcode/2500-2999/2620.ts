function createCounter(n: number): () => number {
  let k = n - 1;
  return function() {
    k = k + 1
    return k
  }
}

