{
  description = "Wealth development shell";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";

  outputs = { self, nixpkgs }: let
    system = "x86_64-linux";
    pkgs = import nixpkgs { inherit system; };
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = [
        pkgs.nodejs_20
        pkgs.pnpm
        pkgs.python312Full
        pkgs.poetry
        pkgs.git
      ];
    };
  };
}
