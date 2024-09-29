type Fn<T> = () => Promise<T>

function promiseAll<T>(functions: Fn<T>[]): Promise<T[]> {
  return new Promise((resolve, reject) => {
    switch (functions.length) {
      case 0:
        resolve([])
    }
  })
};