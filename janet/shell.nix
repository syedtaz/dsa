with (import <nixpkgs> {});

mkShell {
  buildInputs = [
    janet
  ];
  JANET_PATH = "./src/2024";
}
