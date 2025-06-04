{
  description = "development shell";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
      in {
          devShells.default = pkgs.mkShell {
            buildInputs = [
              pkgs.nodejs_20
              pkgs.pnpm
              pkgs.python312Full
              pkgs.poetry
              pkgs.git
              pkgs.pre-commit
              pkgs.black
              pkgs.nodePackages.prettier
            ];

          shellHook = ''
            echo "✅ dev shell ready (Node, Python, Poetry, PNPM)"
          '';
        };
      });
}
