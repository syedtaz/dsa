type CallbackFn = (
  next: (data: number, error: string) => void,
  ...args: number[]
) => void

type Promisified = (...args: number[]) => Promise<number>

function promisify(fn: CallbackFn): Promisified {

  return async function (...args) {

  };
};
