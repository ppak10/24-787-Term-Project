# 24-787-Term-Project
Term Project Repository

## Getting Started
1. Clone repository and submodules
    ```shell
    git clone --recurse-submodules https://github.com/ppak10/24-787-Term-Project.git
    ```
2. Create `.env` from `.env.example` and fill in fields.
    * Setting `JUPYTER_TOKEN` will be your login password for web-based Juypter notebook.
3. Install docker and run
    ```
    docker-compose up -d
    ```
4. Reopen VSCode in dev-container.

## Notes
1. Include newly installed conda packages with `conda env export > environment.yml`.

## Troubleshooting
1. If submodule folder are empty run, clone all submodules with:
    ```shell
    git submodule update
    ```
