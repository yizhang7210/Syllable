with import <nixpkgs> {};
stdenv.mkDerivation rec {
  name = "syllable";
  env = buildEnv { name = name; paths = buildInputs; };
  buildInputs = [
    python37Full
    python37Packages.pip
  ];
}
